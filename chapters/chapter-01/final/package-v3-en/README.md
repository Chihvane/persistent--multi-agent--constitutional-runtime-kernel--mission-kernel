# Chapter 1 Publishing Package — English (v3-EN)

**Date:** 2026-05-14
**Series:** *From Single-Agent OS to Constitutional Runtime*
**Chapter:** 1 — Structural Instability in Agent OS

This is the natively-translated English edition of `chapter1_publishing_package_v3` (Chinese). All layout, diagrams, definition boxes, and example boxes are preserved; prose is rewritten in idiomatic English rather than translated word-for-word.

---

## Package contents

```
chapter1.md           Full chapter in Markdown (with pandoc div boxes + PNG diagram refs)
chapter1.docx         Word version, embedded images
chapter1.pdf          PDF version, 17 pages, with red-bordered definitions and
                      green-bordered example boxes
diagrams/             10 rendered PNGs + their .mmd Mermaid sources
chapter_style.css     Reference stylesheet (lift the .definition / .example rules into
                      your site CSS if you want the same box styling on GH Pages)
README.md / .pdf      This file
```

---

## Translation notes

- The Chinese voice was rebuilt rather than literally translated. Idioms, transitions, and tone are calibrated for native English readers.
- Technical terms originally in English (mission, owner, support, evidence, runtime, etc.) are kept in English.
- All ten diagrams have been re-rendered with English labels.
- The definition / example box conventions are unchanged: red border = `Rule X · …` (Stewart-textbook style); green block = `Scenario X · …` or `Analogy X · …` (Discovery-Project style).
- References are unchanged from the Chinese edition — the citation chain is the same.

## Structural changes vs the Chinese v3

None. Section numbering (1.0, 1.1 – 1.8, 1.9 – 1.12), figures, definitions, examples, and references all map one-to-one. The English edition is a parallel artifact, not a different argument.

## Section titles

| # | English title |
|---|---|
| 1.0 | Opening: from Agent-OS expectations to runtime-structure failure |
| 1.1 | Task ownership drifts in long-running conversations |
| 1.2 | Support quietly turns into ownership |
| 1.3 | Memory is not evidence |
| 1.4 | Persona gets smuggled in as a law source |
| 1.5 | The delegation chain quietly becomes an authority chain |
| 1.6 | Global chat degrades collaboration into context pollution |
| 1.7 | Tool calling is not capability governance |
| 1.8 | The system knows how to continue, but not how to lawfully stop |
| 1.9 | Eight symptoms, one structure |
| 1.10 | Constitutional Runtime as a problem frame |
| 1.11 | What this is not |
| 1.12 | Where this leaves us |

## Channel guidance

- **GitHub Pages / Jekyll:** use `chapter1.md` directly; Jekyll renders Mermaid natively in most modern themes, and the `.definition` / `.example` div classes will pick up custom CSS in your site stylesheet.
- **Substack:** Substack does not honor custom CSS or Mermaid. Either translate the box content to Substack's native blockquote styling by hand, or upload `chapter1.pdf` as a downloadable companion to a flat-prose Substack post.
- **Hugging Face Spaces / model cards:** `chapter1.md` works directly if the space supports Mermaid (most modern spaces do).
- **Archival / print:** `chapter1.pdf` (17 pages) is the canonical archival artifact.

## Diagrams

| Figure | Section | Subject | Source file |
|---|---|---|---|
| 1.1 | §1.1 | Task ownership drifts through support input + compaction | `diagrams/fig_1_1.png` |
| 1.2 | §1.2 | Recon request silently promoted to mainline | `diagrams/fig_1_2.png` |
| 1.3 | §1.3 | Memory must pass an evidence gate | `diagrams/fig_1_3.png` |
| 1.4 | §1.4 | Persona shell cannot become the law source | `diagrams/fig_1_4.png` |
| 1.5 | §1.5 | Authority as typed objects on the mission record | `diagrams/fig_1_5.png` |
| 1.6 | §1.6 | Group chat (left) vs orchestrator-workers (right) | `diagrams/fig_1_6.png` |
| 1.6b | §1.6 | Council lifecycle for a single mission | `diagrams/fig_1_6b.png` |
| 1.7 | §1.7 | Tool list vs capability registry | `diagrams/fig_1_7.png` |
| 1.8 | §1.8 | Six lawful runtime actions | `diagrams/fig_1_8.png` |
| 1.9 | §1.9 | Eight defects converging on one structure | `diagrams/fig_1_9.png` |

Every `.png` has a matching `.mmd` source in the same folder, so the diagrams are re-editable.

---

*If anything in the English edition reads off — phrasing, term choice, a paragraph that lost its bite in translation — flag the section and I'll do a targeted rewrite rather than re-translate the whole chapter.*
