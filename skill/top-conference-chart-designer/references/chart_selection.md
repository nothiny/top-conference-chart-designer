# Chart selection

Choose the simplest encoding that answers the user’s question. The following choices are defaults, not rigid rules.

| Question | Preferred chart | Important details |
| --- | --- | --- |
| Compare a small set of methods or categories | Dot plot or bar chart | Sort by the comparison metric; include uncertainty when available; keep a zero baseline for bars. |
| Show performance as a function of a continuous variable | Line chart | Use markers when there are few observations; show repeated runs or confidence bands without hiding the raw trend. |
| Compare distributions or latency | ECDF/CDF, box plot, or violin plot | State whether lower or higher is better; annotate sample counts and percentile values when useful. |
| Show association between two measurements | Scatter plot | Use transparent points for overplotting; add a fitted line only when it supports the question and label the fit. |
| Show counts over bins or time | Histogram or step line | Make bin width explicit or defensible; avoid smoothing that changes the observed pattern. |
| Show a matrix of values | Heatmap | Use a sequential or diverging map that matches the data range; annotate only when the matrix is small enough to read. |
| Report exact values for a few conditions | Table or annotated dot plot | Prefer exact labels to a bar chart when small differences are the message. |

For benchmark figures, put methods on one semantic axis, use one consistent color per method across panels, and make the primary metric visually dominant. For ablations, keep the baseline visibly distinct and order variants by the ablated component or the result. For multiple datasets, use small multiples rather than forcing unrelated scales onto one axis.
