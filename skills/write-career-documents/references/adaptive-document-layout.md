# Adaptive document layout

Use this reference for Word or PDF CVs, resumes and cover letters.

## Template precedence

1. Use the user's current native template when supplied.
2. Reuse an older user template only when the current template lacks a needed component or the user asks for the older design.
3. Otherwise use the relevant anonymized native asset when its market and document type fit.
4. Fall back to the Markdown structure only when no appropriate native template is available.

Never overwrite a source template. Work from a copy. Replace every example, placeholder and fictional claim before presenting a real application document.

## Content-driven fit

Page count is a consequence of market, career stage, evidence and submission constraints. Do not force one page universally.

Treat the template's typography, spacing and margins as a starting point, not fixed settings. Fit in both directions: expand an underfilled page and compact an overfull page. Recheck after translation, shortening, or replacing the example text; the old layout may no longer suit the new content.

For the bundled one-page examples, aim for a well-filled page with a normal bottom margin. As a local visual target, the last content line should normally sit around 85 to 94 percent of the A4 page height for the CVs and 80 to 92 percent for the letter. These are review aids for these examples, not universal application rules or targets to reach at any cost. Check the distribution of text too: a large internal gap or an isolated signature at the bottom does not count as a well-filled page.

Keep adjustments bounded. For these Times New Roman templates, normally use 10.5 to 12 pt CV body text and 11 to 12 pt letter body text. CV leading is usually about 1.05 to 1.25 times the body size; letter leading about 1.15 to 1.5. Keep role gaps around 3 to 8 pt and section gaps around 6 to 14 pt. Letter paragraph gaps should normally remain within 8 to 18 pt. These are working ranges, not permission to move every setting to its maximum. Prefer a slightly underfilled page over oversized type, excessive leading, or stretched spacing. User templates and submission rules may require other values.

When content does not fit:

1. Remove low-relevance or repetitive content without weakening verified evidence.
2. Tighten excess paragraph or section spacing in small increments.
3. Shorten bullets or prose while preserving claim, ownership, qualifier and metric locks.
4. Reduce body font in small increments. For the bundled CVs, normally work within 10.5 to 12 pt; do not go below 9 pt even for exceptional constraints, and reject sizes that are uncomfortable in the actual font. For the bundled cover letter, normally work within 11 to 12 pt and do not go below 10 pt.
5. Reduce margins only after the earlier steps. For a dense A4 CV, do not go below 7 mm. Keep cover-letter margins wide enough for comfortable reading and normal business-letter conventions.
6. If the document remains overfull, use an additional page or ask which evidence to prioritize. Do not create unreadable density.

When the page is materially underfilled:

1. Increase body font in 0.5 pt steps within a comfortable range for the typeface. A shorter CV should usually use larger text than a dense CV, not the same compressed settings.
2. Increase line spacing and paragraph spacing proportionately. Keep related entry lines closer together than separate roles or sections.
3. Increase section and role gaps modestly and adjust margins if this improves line length and balance. Do not fill the page through huge gaps, oversized headings, or a detached skills block.
4. For a cover letter, enlarge body text and line spacing before stretching the address block or signature gap. Keep the letter's header, paragraphs, closing, and signature visually connected.
5. Render again and compare the whole page. Only accept substantial unused space when the available content cannot fill the page naturally within readable settings, or when the user or submission format requires it. Never invent or repeat content to reach a visual target.

Use paragraph styles and controlled spacing rather than extra empty paragraphs. A DOCX template is not an automatic fitting engine: after its content changes, repeat the fit and render review before calling the document finished.

### Sparse early-career CVs

Use the early-career variant when a student or recent graduate has materially less verified evidence than the dense consulting-style template can hold. If no suitable user template exists, start from `assets/generic-cv-template-early-career.docx` instead of stretching the dense template.

- Put education first for Bachelor students and comparable early-career applicants unless the target convention or stronger experience supports another order.
- Keep two or three evidence-rich bullets per internship and one or two per extracurricular role. Do not repeat duties merely to fill the page.
- Retain secondary education only when it remains proportionate and useful for the career stage or market.
- Do not invent metrics or add a generic profile, weak coursework, irrelevant projects, skill bars, decorative graphics, or inflated interests to occupy space.
- Begin around 11.5 to 12 pt body text with modestly wider margins and more section spacing than the dense variant. Preserve a clear hierarchy and adjust one variable at a time.
- Accept deliberate lower-page whitespace only after trying the underfill adjustments and checking that further expansion would look strained. If the result is still too sparse, ask only for relevant, verifiable projects, coursework, employment, volunteering, awards, or responsibilities that may actually be missing.

Change one layout variable at a time. Render after every meaningful adjustment so the cause of each change remains visible.

## Render gate

For every final Word or PDF deliverable:

- render every page to an image and inspect it at 100 percent zoom
- confirm the intended page count and page size
- check clipping, overlaps, orphaned headings, broken bullets, awkward wraps, tab alignment, section rules and visual balance
- check for underfill as well as overflow; a one-page export alone is not a layout pass
- confirm that text remains selectable and machine-readable
- scrub source metadata and search the package for source-template personal data
- inspect relationships, macros, embedded objects, comments, tracked changes, custom properties, absolute paths and unexpected external links before delivery
- deliver only the requested final files, not the QA renders

## Formatting consistency

Treat punctuation and date notation as part of the template system, not as incidental prose. Audit all date ranges, separators, indentation, tab stops, bullet markers, capitalization and section rules before delivery. When the native CV template uses compact month and year ranges, use `MM/YYYY – MM/YYYY` with a spaced en dash. For an expected completion date, preserve uncertainty in a consistent suffix such as `MM/YYYY – MM/YYYY (voraussichtlich)` or `MM/YYYY – MM/YYYY (expected)`. Do not mix this with `bis`, hyphens or unspaced dashes in the same document. Use `heute`, `present` or another current-state label consistently with the document language.

If rendering is unavailable, state that visual QA could not be completed. Do not imply that the file passed the render gate.
