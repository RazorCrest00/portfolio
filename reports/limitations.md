# Known Limitations

## 2026-08-31

- Some source notebooks do not contain cell IDs required by newer notebook-format conventions. The installed `nbformat` version still normalizes these cells automatically, so conversion and the site build pass, but the notebooks should eventually be resaved or normalized before that warning becomes an error in a future release.
