# Top Conference Chart Designer

一个面向科研绘图的 Codex Skill 和顶会论文图表参考库，目标是让 AI 根据真实论文中的信息组织方式，生成更准确、更清晰、更适合论文排版的数据图表。

## 在线资源

- 图表索引：[nothiny.github.io/top-conference-chart-designer](https://nothiny.github.io/top-conference-chart-designer/)
- GitHub 仓库：[github.com/nothiny/top-conference-chart-designer](https://github.com/nothiny/top-conference-chart-designer)
- 远程索引：[catalog.json](https://nothiny.github.io/top-conference-chart-designer/catalog.json)

图表索引支持按会议、论文方向、图表类型、年份、论文标题和关键词筛选。

## 项目内容

仓库分成两个互相独立的部分：

```text
skill/
└── top-conference-chart-designer/
    ├── SKILL.md
    ├── references/
    └── scripts/

docs/
├── index.html
├── catalog.json
└── compressed/
    └── 2,637 张无损 WebP 图表图片
```

`skill/` 是可安装的 Skill，不包含图片语料；`docs/` 是 GitHub Pages 网站和图表数据集。

目前语料包含 500 篇论文、2737 个图表页面，覆盖：

- CVPR、ICCV
- NeurIPS、ICML
- ACL
- OSDI、NSDI、FAST、ATC

图片使用无损 WebP 格式保存。原始 PDF 和 PNG 保留在本地采集环境中，没有上传到仓库。

## 安装 Skill

安装时只复制下面这个目录：

```text
skill/top-conference-chart-designer/
```

Skill 默认通过 GitHub Pages 读取远程元数据和参考图片：

```text
https://nothiny.github.io/top-conference-chart-designer/catalog.json
```

安装 Skill 不会自动克隆或下载 `docs/compressed/` 图片语料。图片仍然保存在 GitHub 仓库和 Pages 站点中。

调用示例：

```text
$top-conference-chart-designer

请读取 results.csv，画一张比较不同方法在多个数据集上性能的顶会风格图。
要求保留每个 seed 的原始点，使用 95% CI，并输出 PNG、PDF、SVG 和绘图源代码。
```

对于 benchmark 数据，推荐使用 long-form 表格：

```text
method,dataset,metric,seed,value
```

Skill 会检查缺失值、重复 seed、指标方向、单位、baseline、聚合方式和置信区间，然后选择合适的图表类型并生成：

静态科研图表默认使用 Python `matplotlib`；只有用户明确要求交互式图表或指定其他绘图库时才切换。Seaborn 仅作为 Matplotlib 的辅助工具使用。

- 300–600 DPI PNG
- PDF/SVG 矢量图
- 可复现的 Python 绘图源代码
- 包含输入哈希、数据变换、图表选择和 QA 结果的 manifest

## 顶会论文图表经验

### 一张图只表达一个主要结论

先确定图表要回答的问题，再选择图表类型。不要为了展示所有实验结果，把无关指标全部堆到同一张图里。

### 图表类型服从数据语义

- 方法比较：点图或柱状图
- 参数变化：折线图
- 消融实验：分组点图或多 panel 图
- 延迟和吞吐分布：CDF/ECDF
- 两个指标的关系：散点图
- 多个数据集：small multiples
- 矩阵结果：heatmap

### 多 panel 优于拥挤的大图

不同数据集或任务通常放到不同 panel 中。相同方法在所有 panel 中使用相同颜色，共享坐标轴和图例，并使用 `(a)`、`(b)`、`(c)` 标记子图。

### 颜色、坐标轴和基线要有明确语义

使用克制、色盲友好的配色，让 baseline 和重点方法容易区分。柱状图默认从 0 开始；使用对数轴、截断轴或双 Y 轴时必须有明确理由。性能图应该标出 baseline 或 `1×` 参考线，并注明指标是越高越好还是越低越好。

### 系统论文重视分布和尾部

系统论文中，平均值通常不够。CDF、p50/p95/p99 延迟、throughput-latency trade-off、不同 workload 和尾延迟往往比单一平均值更有信息量。

### 统计信息不能隐藏

有多次运行时，明确均值、中位数、标准差、标准误或置信区间，并保留原始点。只有一次测量时，不要伪造误差条。

### 按最终论文尺寸设计

单栏图通常约 3.25–3.5 英寸，双栏图约 6.5–7 英寸，正文文字通常为 7–9 pt。必须在最终尺寸下检查字体、图例、tick、注释和 panel 间距，同时输出 PNG 和 PDF/SVG。

## 本地预览

```powershell
python -m http.server 8765 --directory docs
# 打开 http://127.0.0.1:8765/
```

## GitHub Pages 部署

`.github/workflows/pages.yml` 会在 `main` 分支更新后自动部署 `docs/`。站点地址为：

```text
https://nothiny.github.io/top-conference-chart-designer/
```

## 说明

这个项目提供的是图表结构、排版和视觉编码方面的参考，不会把论文中的数据直接用于用户的新图。自动分类和风格参考仍然需要人工复核，尤其是复杂的多 panel 图、统计图和系统性能图。
