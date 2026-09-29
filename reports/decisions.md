# About Page Personalization Decisions

## 2026-09-29 — Remaining Python homework

- Follow all eight live assignments as checked September 29. The active 3.09 version is Safe Passage Heals; 3.14 uses season statistics and Flask, not the older cached study-session exercise. Store exact assignment URLs and fetched HTML hashes in `python-homework-2026-09-29.json`.
- Use seven notebook pages with saved outputs and one Markdown page for the explicitly requested 3.17 format. Keep code cells independently runnable, add plain Python downloads and one submission checklist, and preserve the existing theme and shared runner.
- Use real Flask and its test client for the required Libraries route exercise. A page-local loader prepares Flask 3.1.3 and pinned pure-Python dependencies in the existing Pyodide 0.23.4 runtime before enabling Run. No repository dependency or lockfile changes. Flask was checked through its official PyPI metadata (Python >=3.9; maintained BSD-3-Clause package); its six dependency packages use compatible permissive licenses. MarkupSafe comes from the existing Pyodide package set. Local validation dependencies stay in a temporary directory.
- Keep JavaScript, AP pseudocode, and Java translations as static examples beside Python-only runners. Standard `pre`/`code` markup prevents the existing converter from treating those translations as Python runner slots; do not change the shared converter. Compile the actual Java translation, since the assignment's block labeled Java uses JavaScript syntax.
- Name the Random Values download `random-values.py`; `random.py` shadows the standard library when launched as a file. Test all eight downloads in fresh Python processes as well as executing their definitions.
- Credit existing OCS/Pyodide infrastructure and AI assistance. Explain full-credit rubric evidence without instructions to manipulate grading. Leave 3.09's classroom participation bonus unclaimed without actual evidence; 3.13 has no published numeric rubric. Seed random demonstrations and fix the Libraries report date so saved outputs remain reproducible.

## 2026-09-28 — 3.12 Calling Procedures homework

- Follow the current live emergency-report assignment, rather than the outdated local café version. Preserve the specified procedure names and exact Medical Emergency comparison.
- Keep three independent code cells: both Popcorn exercises and the dispatch homework. Four homework calls use four fictional practice locations and three incident types. Add explanations and verification without complicating the functions.
- Reuse existing OCS/Pyodide browser execution with `local_python: true`; restrict this page's selectors to Python because all editable examples are Python. No CSS, Sass, shared runner, or dependency changes.
- Base the 1.00/1.00 self-assessment on the current six-row rubric. The five written knowledge answers are B,B,B,B,A, self-checked rather than recorded as a live quiz grade. Credit AI assistance and the existing runtime.

## 2026-09-25 — 3.08 Iterations homework

- Follow the live Python 3.08 notebook submission format and reuse the existing portfolio OCS/Pyodide runner; no shared runner, CSS, Sass, or dependency changes.
- Keep the required solutions as direct, independently executable loops with original simulated datasets. Use SFSRC for Popcorn and UESL match latency for the personal homework theme.
- Include the critical reading in action counts/totals before stopping; label the unread suffix as uninspected. Test exact threshold equality and initial critical values.
- Add while/fixed-count examples, an AP translation, traces, and a reproducible verifier that executes the submitted cells instead of a duplicate solution.
- Show the user's requested 1.00/1.00 as a self-assessment with criterion-level evidence. The live MCQ was completed with A,B,A,B and returned 4/4. Credit AI assistance and existing OCS/Pyodide infrastructure.

## 2026-08-25

- Preserve the site's incumbent dark Minima theme while giving the About page a distinct warm-gold accent.
- Use the San Diego city flag, Indian national flag, and North Carolina state flag so each location has a recognizable and accurate visual.
- Generate the grid container and all location items through JavaScript DOM methods to make the assignment's learning objectives directly inspectable.
- Keep evaluation claims evidence-based: show completed requirements and explain their implementation instead of inserting grader-manipulation instructions.
- Publish descriptive, lowercase image filenames instead of Photos-library identifiers, use progressive JPEG for broad browser support, and strip EXIF metadata to avoid exposing device or location details.
- Preserve each photo's natural subject and orientation in a responsive editorial gallery rather than forcing every image into one uniform crop.

## 2026-08-31 — Upstream merge repair

- Preserve local files and behavior when they represent portfolio authorship or intentional functionality; use upstream as the base for generic framework, setup, and conversion code.
- Combine runner implementations instead of choosing one side: upstream supplies `data-hook` controls, robot execution, autostart, and improved game module resolution; local supplies language variants, Pyodide, case-insensitive pseudocode, and prefilled editable starters.
- Keep the existing merge commit intact and prepare a staged follow-up repair because the merge had already been committed and pushed before conflict markers were removed.
- Resolve the old/new Sass filename collision with explicit upstream partial imports, retaining the local legacy files for compatibility.

## 2026-09-21 — 3.04 Strings homework

- Follow the current Strings assignment's notebook format, retaining CODE_RUNNER markers and avoiding imports and input().
- Keep each required answer separate and independently executable; place additional test cases in a fifth cell.
- Use literal outer JSON braces around f-string fields to avoid conflicting with the site's Liquid template syntax.
- Justify rubric coverage using executable evidence and actual outputs; disclose AI assistance and do not claim independent authorship, peer feedback, or a guaranteed grade.
- Preserve the existing site theme, layout, configuration, and unrelated portfolio work.
- Enable the existing Pyodide executor through a page-level opt-in. The remote OCS runner does not return an allowed-origin header for this GitHub Pages domain, so the homework executes Python locally in the browser. Existing include-level opt-ins keep working.
