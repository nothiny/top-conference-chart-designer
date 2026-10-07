# Top Conference Chart Designer

This repository contains two deliberately separate parts:

- `skill/top-conference-chart-designer/` is the installable Codex Skill. It contains instructions, style references, and lightweight plotting helpers, but no chart corpus images.
- `docs/` is the GitHub Pages site. It contains the searchable index and the lossless WebP chart corpus.

The public gallery is available at:

<https://nothiny.github.io/top-conference-chart-designer/>

## Install the Skill without downloading the corpus

Install or copy only `skill/top-conference-chart-designer/` into the local Skills directory. The Skill uses the remote Pages metadata and image URLs as visual references:

```text
https://nothiny.github.io/top-conference-chart-designer/catalog.json
```

It does not clone or download `docs/compressed/` during installation. The image corpus stays in GitHub Pages.

## Local preview

```powershell
python -m http.server 8765 --directory docs
# open http://127.0.0.1:8765/
```

## Corpus

The index contains 500 papers and 2,737 chart-page records from CVPR, ICCV, NeurIPS, ICML, ACL, OSDI, NSDI, FAST, and ATC. The published images are lossless WebP files; the original PNG files and source PDFs remain outside this repository.

The site is deployed by `.github/workflows/pages.yml` whenever `main` changes.
