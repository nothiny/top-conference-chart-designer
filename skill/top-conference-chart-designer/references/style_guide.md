# Publication-style visual system

This guide distills recurring conventions from the local top-conference chart corpus. It is meant to make figures easy to compare and read at paper scale, not to reproduce any one paper’s identity.

## Canvas and typography

- Choose the final paper width first: roughly 3.25–3.5 inches for a single column or 6.5–7.0 inches for a two-column figure.
- Render raster previews at 300 DPI or higher. Prefer PDF/SVG for line work, text, and vector marks.
- Use a readable sans-serif or the venue’s requested font. Start around 8–9 pt at final size; never shrink labels until they are unreadable just to fit more data.
- Use a short descriptive caption outside the axes. Titles inside the axes are optional and should not repeat the caption.
- Use consistent panel labels `(a)`, `(b)`, etc. and align panel margins.

## Axes, marks, and grids

- Remove top and right spines when they do not carry information. Keep the baseline and tick marks clear.
- Use thin axis and line strokes, with slightly stronger emphasis for the primary series. Avoid decorative shadows and gradients.
- Use only light horizontal or vertical grid lines when they help estimate values. Do not grid every direction by default.
- Keep tick precision honest: do not show more decimals than the measurement supports. Put units in the axis label rather than repeating them in every tick.
- Use a logarithmic axis only when the data-generating scale or the comparison requires it, and label it clearly.

## Color and redundancy

- Use a restrained, color-blind-safe palette. A good default is blue, orange, green, red, purple, and brown with different markers or line styles for important series.
- Keep the semantic mapping stable: the same method or condition gets the same color in every panel.
- Use redundant encodings (color plus marker, dash, or direct label) when the figure must remain interpretable in grayscale or for color-vision deficiency.
- Reserve saturated accent colors for the key result or an anomaly. Keep baselines and context neutral.

## Uncertainty and annotation

- Show error bars or confidence bands only when they have a defined meaning; state `95% CI`, standard deviation, standard error, or quantiles in the legend/caption.
- Avoid covering the data with annotations. Use short callouts for the one or two comparisons the reader should notice.
- Put values on marks only when the number of marks is small enough to remain legible. Otherwise rely on axes and a compact caption.
- When a result is statistically or practically tied, do not imply a large difference through color or annotation.

## Review checklist

Before delivery, verify: the chart type matches the question; categories are ordered intentionally; no group is silently omitted; baselines and axis limits are defensible; units and uncertainty are visible; labels and legends fit at final size; the exported image has no clipping; and the figure can still be understood when printed in grayscale.
