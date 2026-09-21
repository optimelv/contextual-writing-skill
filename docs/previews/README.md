# Application template previews

These English PDFs and thumbnails are rendered from the editable Word templates in `skills/write-career-documents/assets/`. All profiles, achievements and application scenarios are fictional. Organisation names and German addresses remain proper names; grades retain the German grading scale.

When a Word template changes, regenerate its PDF and thumbnail together, inspect every page and confirm that the PDF still matches the editable source. Do not edit preview text separately from the Word source. Each current preview contains one A4 page with selectable text.

Refit typography and spacing after changing the content. The shorter CV uses larger body text than the dense CV; the cover letter has its own paragraph rhythm. Do not reuse a compressed layout when the revised text leaves much of the page empty.

With Poppler installed, `python3 scripts/run_tests.py` also checks these PDFs for page count, bottom clearance, underfill, and matching DOCX text. This checks the bundled examples, not a universal page-fill rule for applications. Visual review is still required.

The September 2026 previews were rendered with LibreOfficeDev 26.8 and Poppler. Font availability and rendering software can affect layout on another system.
