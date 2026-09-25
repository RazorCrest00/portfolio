# About Page Personalization Progress

## 2026-09-25 — 3.08 Iterations homework

- Goal: complete and publish the Python Iterations Popcorn, MCQ, and homework tasks with original data, explanations, browser execution, and evidence supporting a 1.00/1.00 self-assessment.
- Plan: (1) inspect the live assignment and existing portfolio conventions; (2) implement the notebook and reproducible tests; (3) execute, build, and inspect desktop/mobile runners; (4) publish and verify the public page and download.
- Step 1: **Done**. The current lesson requires a notebook, one CODE_RUNNER task per cell, original values, a four-question MCQ result, and a checker using at least eight values, two thresholds, continue, break, and labeled counters/totals.
- Steps 2–3: **Done**. Created the executed notebook and a standard-library verification script. Four independent browser runners, all required exercises, traces, AP translation, design notes, and full-score rubric evidence are complete. Eleven homework datasets, ten extension cases, four mutation checks, and four AP examples pass. The live lesson's MCQ returned 4/4. Local conversion, Jekyll build, and desktop/mobile review pass.
- Step 4: **Done**. Commit `a4a1849` was published to `RazorCrest00/portfolio/main`. GitHub Actions run `36178305305` completed build and deployment successfully. The public page and notebook return HTTP 200; downloaded notebook bytes match the tested source. All four runners and the changed-input/reset/mobile checks also pass on the public site.
- All four plan steps are **Done**. Submit https://razorcrest00.github.io/portfolio/python/iterations-hw through the live Iterations lesson's Submit Homework form, with the page's prepared notes. No assignment form was submitted automatically. Full marks are a requested self-assessment, not an independently awarded grade; monitoring inputs are labeled classroom simulations.

## 2026-08-25 — Section 1: JavaScript flag grid

- Task: Replace the template flag content with Adhvay Iyer's three meaningful locations.
- Files changed: `navigation/about.md`.
- Implementation: JavaScript data objects, DOM-created grid container and cards, responsive CSS Grid, accessible image text, and reduced-motion support.
- Tests run: repository `make` workflow, local Jekyll response parse, inline JavaScript syntax validation, and source assertions for the required DOM methods.
- Result: passed after installing the repository's documented dependencies and placing its virtual environment first on the build path.
- Assumptions: “Carrie, NC” refers to Cary, North Carolina; Bengaluru is represented by the flag of India and Cary by the North Carolina state flag.
- Next verified task: Replace the template biography with Adhvay's journey, interests, and assignment evidence.

## 2026-08-25 — Section 2: Personalized Markdown

- Task: Replace the template biography with Adhvay's identity, life journey, interests, culture, activities, and goals.
- Files changed: `navigation/about.md` and the SDLC reports.
- Implementation: editorial introduction, eight-point chronological journey, eight personal-interest entries, and an evidence-based Exemplar checklist.
- Tests run: repository `make` workflow, built HTML parsing, Markdown structure counts, JavaScript syntax validation, and whitespace validation.
- Result: passed; the built page contains the expected hero, 8 journey entries, 8 interest entries, and 8 rubric items.
- Known intermediate state: the two unchecked rubric items and template gallery files are intentionally reserved for Section 3.
- Next verified task: prepare and install Adhvay's four original photos, then complete the gallery and final checklist.

## 2026-08-25 — Section 3: Personalized photo gallery

- Task: Replace all template gallery references with Adhvay's four original photos and complete the assignment evidence.
- Files changed: `navigation/about.md`, four new files in `images/about/`, and the SDLC reports.
- Implementation: responsive figure gallery, personalized captions, descriptive alternative text, intrinsic dimensions, lazy decoding, and four optimized progressive JPEGs.
- Privacy and compatibility: converted the HEIC source for browser support and removed all EXIF metadata from the published copies; the originals remain unchanged.
- Tests run: third repository `make` workflow, built HTML gallery audit, image decode/dimension/luminance checks, metadata check, template-reference search, JavaScript syntax validation, whitespace validation, and the Impeccable detector.
- Result: passed; all 4 images decode correctly, all 4 captions render, every image has alt text and dimensions, all 8 rubric items are checked, and the detector returned no findings.
- Next verified task: inspect the final diff and three-commit history.

## 2026-08-31 — Upstream merge repair

- Task: Repair the already-committed unrelated-histories merge with `upstream/main` without losing portfolio work.
- Portfolio work preserved: personalized About page and four photos, PC Assembly CPT lesson and language variants, browser-local Python execution, editable runner starters, analytics hooks, and local game content.
- Framework integration: adopted upstream signup/setup/conversion/game-executor behavior; combined upstream runner hooks, robot execution, and autostart with the local multi-language and Pyodide features.
- Merge repairs: removed all embedded conflict markers, disambiguated duplicate Sass partial names, fixed alert-button token interpolation, corrected the `verifyTools.sh` shebang, and made notebook conversion imports work in spawned macOS workers.
- Tests run: JavaScript/Python/shell syntax checks, PC Assembly regression suite, all 19 notebook conversions, generated-output inspection, and a final Jekyll build.
- Result: passed. The working tree contains only the staged merge-repair changes and is ready for a follow-up commit.
- Known limitation: some source notebooks lack modern cell IDs; `nbformat` currently normalizes them with a warning.

## 2026-09-21 — 3.04 Strings homework

- Goal: publish all three Popcorn solutions, the final transmission homework, and evidence-based self-assessment in Adhvay's own portfolio.
- Plan: (1) verify the current assignment and repository; (2) create and execute the notebook with useful additional checks; (3) build and inspect the page; (4) publish and verify the live submission links.
- Completed implementation and local verification: one notebook, five independently executable cells, saved outputs, eight changed-input cases, a successful Jekyll build, and desktop/mobile inspection.
- All four plan steps are **Done**. Commit `d188541` was published to `RazorCrest00/portfolio/main`; GitHub Actions run `35644755294` completed build and deployment successfully. The public page and notebook download both return HTTP 200, and all five runners also pass on the live site.
- Submit the notebook `_notebooks/homework/2026-09-21-strings-intercepters-hw.ipynb` for 3.04 Strings. Public page: https://razorcrest00.github.io/portfolio/python/strings-intercepters-hw .
