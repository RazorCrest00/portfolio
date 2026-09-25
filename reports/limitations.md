# Known Limitations

## 2026-09-25 — 3.08 Iterations homework

- Scores in the notebook are a full-credit self-assessment supported by completed work, not an awarded course grade. The MCQ result was checked against the live lesson.
- Monitoring values and thresholds are original classroom simulations, not real UESL/SFSRC measurements or operational guidance. Early-exit reports describe only the inspected prefix.
- The existing browser Python engine needs an initial network download. The submitted notebook retains execution output for review without rerunning.

## 2026-08-31

- Some source notebooks do not contain cell IDs required by newer notebook-format conventions. The installed `nbformat` version still normalizes these cells automatically, so conversion and the site build pass, but the notebooks should eventually be resaved or normalized before that warning becomes an error in a future release.

## 2026-09-21 — 3.04 Strings homework

- This assignment intentionally parses controlled four-field CSV-style strings and formats controlled JSON text without imports. Quoted CSV fields, embedded delimiters, and arbitrary JSON escaping are outside its stated scope and are explained in the notebook.
- Browser execution uses the portfolio's existing Pyodide runtime, requiring a network connection for its initial CDN download. Saved outputs remain readable without executing code again.
- The rubric justification identifies completed evidence; a final score remains the grader's decision. The submission explicitly acknowledges AI assistance.
