<p>
  <img src="docs/assets/hero.png" alt="Contextual Writing. Your context. Your voice. Writing shaped by the reader and the evidence. Context, evidence, voice, review. German and English. Ten skills, one shared source, for Claude and Codex." width="1200">
</p>

<p>
  <a href="https://github.com/optimelv/contextual-writing-skill/actions/workflows/validate.yml"><img src="https://github.com/optimelv/contextual-writing-skill/actions/workflows/validate.yml/badge.svg" alt="Validation status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-a3422e?labelColor=242421" alt="MIT license"></a>
</p>

Writing skills for **Claude and Codex**, in German and English. Use them for applications, academic writing, emails, research, and slide content, with rules suited to each format.

[Install](#install) · [Example](#see-the-difference) · [Templates](#template-gallery) · [Skills](#components) · [Validation](#validation)

## Install

### Claude Code: plugin installation

Inside Claude Code, add the marketplace and install the plugin:

```text
/plugin marketplace add optimelv/contextual-writing-skill
/plugin install contextual-writing@contextual-writing
```

<details>
<summary><strong>Update or uninstall</strong></summary>

```text
/plugin marketplace update contextual-writing
/plugin update contextual-writing@contextual-writing
```

```text
/plugin uninstall contextual-writing@contextual-writing
```

Restart Claude Code if prompted after an update.

</details>

### Codex and other agents: install with npx

From your project directory:

```bash
npx skills add optimelv/contextual-writing-skill --skill '*'
```

Choose your agent when prompted. To install directly for Codex:

```bash
npx skills add optimelv/contextual-writing-skill --skill '*' --agent codex --yes
```

Requires Node.js and npm. Keep `'*'` quoted and install all ten skills, which share supporting files. Use either the [Skills CLI](https://github.com/vercel-labs/skills) or a native plugin installation to avoid duplicates.

<details>
<summary><strong>Already using the Codex plugin?</strong></summary>

Keep that installation and invoke `$contextual-writing`. There is no need to install the skills again through npx.

</details>

## See the difference

A fictional applicant mapped an onboarding workflow and helped implement it for three customers.

| Before | After |
| :--- | :--- |
| “I spearheaded a transformative onboarding initiative, driving significant customer success and operational excellence.” | “I mapped the onboarding workflow and supported implementation for three customers.” |

### Try it on your own material

```text
Application writing
Write a cover letter using my CV and this job description.
Ask if you need more detail about my experience. Write in German.

Academic writing
Edit this discussion paragraph for clarity. Keep the citations and
qualifiers, and do not add conclusions the findings do not support.

Outreach
Draft a short email using this company update and our pilot result.
Do not assume the company has the problem we solve. End with one clear ask.
```

## How it handles your writing

- Uses the brief and source material before asking questions.
- Preserves facts, citations, uncertainty, and deliberate cuts.
- Follows your explicit instructions rather than guessing from a style sample.
- Leaves good passages unchanged.
- Checks word limits, required fields, and other submission requirements.

## Components

The main skill selects the relevant workflow. You can also invoke a focused skill directly.

| Skill | Primary scope |
| --- | --- |
| `contextual-writing` | Selects the workflow, language, and relevant writing rules |
| `write-career-documents` | CVs, cover letters, applications, career outreach, and profiles |
| `write-professional-communication` | Emails, memos, follow-ups, reports, and administrative messages |
| `write-commercial-content` | Sales outreach, marketing, customer, and partner communication |
| `write-academic-content` | Academic drafting and revision from supplied sources |
| `write-research-content` | Source research and fact-checking |
| `write-slides-and-strategy` | Slide narratives, pitches, and strategy presentations |
| `write-general-content` | Articles, essays, newsletters, posts, and website copy |
| `edit-and-humanize` | Editing, style matching, and translation review |
| `teach-and-explain` | Explanations, tutoring, and study material |

In Codex, only the main skill is configured for automatic selection. Other agents use their own discovery rules.

## Template gallery

Three fictional English examples, each on one A4 page. Open a preview to read the PDF or download the editable Word file.

| Dense CV | Early-career CV | Cover letter |
| :---: | :---: | :---: |
| [![Dense CV preview](docs/previews/generic-cv-template-1.png)](docs/previews/generic-cv-template.pdf) | [![Early-career CV preview](docs/previews/generic-cv-template-early-career-1.png)](docs/previews/generic-cv-template-early-career.pdf) | [![Cover letter preview](docs/previews/generic-cover-letter-template-1.png)](docs/previews/generic-cover-letter-template.pdf) |
| [PDF](docs/previews/generic-cv-template.pdf) · [Word](skills/write-career-documents/assets/generic-cv-template.docx) | [PDF](docs/previews/generic-cv-template-early-career.pdf) · [Word](skills/write-career-documents/assets/generic-cv-template-early-career.docx) | [PDF](docs/previews/generic-cover-letter-template.pdf) · [Word](skills/write-career-documents/assets/generic-cover-letter-template.docx) |

Replace the example content with your own experience. Layout and length should follow the application requirements.

## Tools you need

The plugin adds writing instructions and templates to your agent. Research needs web access. Creating Word, PDF, or slide files needs document tools, which are not included.

The research skill covers focused questions and fact-checking, not a full literature review or legal advice.

## Validation

Run the package and helper-script tests:

```bash
python3 scripts/run_tests.py
```

The tests check package structure and helper scripts. To review the writing itself, use the [example tasks](tests/forward_cases.json) and [review guide](tests/FORWARD_TESTING.md).

To [report a problem](https://github.com/optimelv/contextual-writing-skill/issues), include the prompt, expected result, actual output, and model/plugin version. Remove private information first.

---

[MIT license](LICENSE) · [Sources and acknowledgments](NOTICE.md)
