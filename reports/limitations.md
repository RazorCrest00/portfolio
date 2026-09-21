# Known Limitations

## 2026-08-31

- Some source notebooks do not contain cell IDs required by newer notebook-format conventions. The installed `nbformat` version still normalizes these cells automatically, so conversion and the site build pass, but the notebooks should eventually be resaved or normalized before that warning becomes an error in a future release.

## 2026-09-21 — 3.04 Strings homework

- This assignment intentionally parses controlled four-field CSV-style strings and formats controlled JSON text without imports. Quoted CSV fields, embedded delimiters, and arbitrary JSON escaping are outside its stated scope and are explained in the notebook.
- Browser execution uses the portfolio's existing Pyodide runtime, requiring a network connection for its initial CDN download. Saved outputs remain readable without executing code again.
- The rubric justification identifies completed evidence; a final score remains the grader's decision. The submission explicitly acknowledges AI assistance.
