"""Check the shipped example PDFs, not arbitrary user application layouts."""
from collections import Counter
from pathlib import Path
import re
import shutil
import subprocess
import unicodedata
import unittest
import xml.etree.ElementTree as ET
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
NAMES = ('generic-cv-template', 'generic-cv-template-early-career',
         'generic-cover-letter-template')
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def tokens(text):
    return Counter(re.findall(r'\w+', unicodedata.normalize('NFKC', text)))


@unittest.skipUnless(shutil.which('pdftotext'), 'Preview checks require Poppler pdftotext')
class TemplatePreviewTests(unittest.TestCase):
    def test_preview_layout_and_text_match_the_word_assets(self):
        for name in NAMES:
            with self.subTest(template=name):
                pdf = ROOT / 'docs/previews' / (name + '.pdf')
                result = subprocess.run(['pdftotext', '-bbox', str(pdf), '-'],
                                        capture_output=True, check=True)
                tree = ET.fromstring(result.stdout)
                pages = tree.findall('.//{*}page')
                self.assertEqual(len(pages), 1, 'Bundled example must remain one page')
                page = pages[0]
                height, width = float(page.attrib['height']), float(page.attrib['width'])
                self.assertAlmostEqual(height, 841.9, delta=1)
                self.assertAlmostEqual(width, 595.3, delta=1)
                words = page.findall('.//{*}word')
                self.assertTrue(words, 'PDF must contain selectable text')
                bottom = max(float(word.attrib['yMax']) for word in words)
                lower, upper = (.80, .92) if 'cover-letter' in name else (.85, .94)
                self.assertGreaterEqual(bottom / height, lower, 'Example page is underfilled')
                self.assertLessEqual(bottom / height, upper, 'Leave a normal bottom margin')
                for word in words:
                    self.assertGreaterEqual(float(word.attrib['xMin']), 18)
                    self.assertLessEqual(float(word.attrib['xMax']), width - 18)
                    self.assertGreaterEqual(float(word.attrib['yMin']), 18)
                with ZipFile(ROOT / 'skills/write-career-documents/assets' / (name + '.docx')) as docx:
                    body = ET.fromstring(docx.read('word/document.xml'))
                source = ' '.join(node.text or '' for node in body.iter(W + 't'))
                rendered = ' '.join(word.text or '' for word in words)
                self.assertEqual(tokens(source), tokens(rendered),
                                 'PDF and DOCX must contain the same words and numbers')

    def test_sparse_example_uses_larger_body_type(self):
        sizes = {}
        for name in NAMES:
            with ZipFile(ROOT / 'skills/write-career-documents/assets' / (name + '.docx')) as docx:
                body = ET.fromstring(docx.read('word/document.xml'))
            values = [int(size.attrib[W + 'val']) / 2
                      for size in body.findall('.//' + W + 'rPr/' + W + 'sz')]
            sizes[name] = Counter(values).most_common(1)[0][0]
        self.assertGreater(sizes['generic-cv-template-early-career'], sizes['generic-cv-template'])
        self.assertGreaterEqual(sizes['generic-cv-template'], 10.5)
        self.assertGreaterEqual(sizes['generic-cover-letter-template'], 11)


if __name__ == '__main__':
    unittest.main()
