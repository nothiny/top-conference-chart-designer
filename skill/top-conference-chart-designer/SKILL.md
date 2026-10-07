---
name: top-conference-chart-designer
description: Create, revise, and quality-check publication-ready data figures from user-provided data, using restrained top-conference visual conventions and reproducible source code.
---

# Top Conference Chart Designer

Use this skill when the user wants a data chart for a paper, poster, technical report, or benchmark and asks for a polished, top-conference-style result. Use native plotting code for scientific figures; do not use image generation or hand-drawn raster editing because every mark must remain faithful to the data.

**Default plotting library:** use Python `matplotlib` for static scientific figures unless the user explicitly requests another library or an interactive chart. Use Seaborn only as a helper on top of Matplotlib, and use Plotly or another interactive library only when interactivity is part of the requested output.

## Workflow

1. **Inspect the input.** Locate the supplied CSV, TSV, JSON, XLSX, Parquet, or in-memory table. For a file, run `scripts/inspect_data.py` when practical to record column names, inferred types, units, missing values, ranges, row count, and an input SHA-256. Read duplicate rows and experimental semantics as well. Preserve the original file and never invent missing values. If the intended comparison, grouping, metric, or uncertainty is genuinely ambiguous, ask one focused question; otherwise make the smallest defensible assumption and state it in the figure manifest.
2. **Choose the visual encoding from the question.** Use the mapping in [references/chart_selection.md](references/chart_selection.md). Prefer a direct, information-dense chart over decorative alternatives. Do not use 3D, pie/donut charts, rainbow palettes, faux perspective, or dual axes unless the user explicitly needs them and the tradeoff is explained.
3. **Apply the visual system.** Read [references/style_guide.md](references/style_guide.md) for the publication-size, typography, palette, line, grid, uncertainty, and annotation rules. If the user names a venue, use the local corpus only as a style reference and keep the data and claims entirely from the user's input.
4. **Generate reproducible output.** Write a Python plotting script or notebook cell that loads the data, performs only documented aggregation, and uses `scripts/figure_style.py` when its Matplotlib helpers fit the figure. Save at least:
   - a vector PDF or SVG when the chosen backend supports it;
   - a 300-600 DPI PNG for previews and web use;
   - a small JSON manifest containing input path and SHA-256, columns used, transformations, chart type, assumptions, reference IDs, random seed, environment versions, output paths, and validation results.
5. **Compose at final size.** Pick a one-column or two-column canvas before tuning labels. Keep labels readable at that size, use direct labels when they remove a legend, and reserve whitespace for annotations. Avoid clipped ticks, legends, error bars, captions, or panel labels.
6. **Validate before delivery.** Run `scripts/plot_quality_check.py` on the exported PNG and vector file where applicable. Check that values, ordering, units, baselines, uncertainty, category colors, and sample counts match the input. Inspect the rendered image once; if any text overlaps or becomes unreadable, revise the source and rerun the check.

## Benchmark tables

When the input is an experiment table, prefer long-form semantics:
`method, dataset, metric, seed, value`, with optional `split`, `runtime`, or `error` columns. If the file is wide, explicitly record the pivot or melt operation. Before plotting:

- Check that `(method, dataset, metric, seed)` is unique, `value` is numeric, and missing or non-finite values are reported rather than silently dropped.
- Confirm or infer from an explicit user statement the metric unit, whether higher or lower is better, the baseline method, and the desired method/dataset order. Ask one question when any missing choice could change the conclusion.
- Aggregate repeated seeds only after retaining the raw points. The default is mean with a 95% confidence interval for `n >= 2`; for `n < 2`, show the observed point and do not fabricate an interval. Record the aggregation, interval definition, and seed count in the manifest.
- Use small multiples for multiple datasets. Share a y-axis only when units and meaningful ranges match. Keep method colors stable across panels and use a compact shared legend or direct labels for long method names.
- Use a grouped dot/bar chart for a few methods, a line chart for an ordered budget or scale, and a CDF/ECDF for latency or throughput distributions. Keep raw seed points visible when they clarify variance.

Hard-fail or stop for clarification when the metric is non-numeric, the grouping key is duplicated in a way that changes aggregation, the direction/unit is unknown and affects interpretation, or the resulting figure is empty/clipped/unreadable. A warning is appropriate for small sample size, an unusually long label, or a low-resolution preview when the final vector export is valid.

## Defaults

- Use Matplotlib as the primary renderer; use Seaborn only for a narrow statistical convenience and keep the final style under explicit control.
- Use a white or transparent background only when the destination requires it. Prefer a light neutral plotting area, subtle axes, and no heavy outer box.
- Use a color-blind-safe categorical palette and redundant line style or marker encodings when color alone is insufficient.
- Use confidence intervals, standard error, or quantiles only when the input contains them or the aggregation method can calculate them honestly. Label the uncertainty definition.
- For bars, use a zero baseline unless a nonzero baseline is essential and clearly marked. For lines and scatter plots, use continuous axes and show units.
- For panels, share axes only when scales are comparable; label panels `(a)`, `(b)`, etc. and keep the same semantic series mapped to the same color everywhere.
- Keep chart text concise: descriptive title or caption outside the plot, informative axis labels, units in parentheses, and a legend only when direct labeling is worse.

## Deliverable naming

Use a user-specified output directory. Otherwise create `figure_output/` beside the input data and use stable names such as `figure_01.png`, `figure_01.pdf`, `figure_01.svg`, `plot_figure_01.py`, and `figure_01.manifest.json`. Never overwrite the user’s input data. For a multi-panel figure, keep one source script and one manifest for the complete figure.

## Corpus reference

The default visual reference corpus is the remote GitHub Pages site `https://nothiny.github.io/top-conference-chart-designer/`. Fetch its lightweight `catalog.json` metadata over HTTPS and select 3-6 visual references by `chart_types`, `conference_category`, `paper_topics`, caption, or plot text. Use the remote `image_path` URLs for visual inspection when needed; do not clone the image directory or download the corpus into the local Skill installation. If the user explicitly provides an already-local corpus, it may be used instead. The corpus is a reference set, not a source of numbers or a reason to imitate a specific paper. The index contains `conference`, `conference_category`, `paper_topics`, `figures`, `caption`, `chart_types`, and `needs_review` fields; treat automatically inferred labels as hints and preserve uncertainty in the manifest.

When returning the result, lead with the generated file paths and the chart's intended message, then briefly state the data transformation, visual choices, validation result, and any assumption that could change the interpretation.
