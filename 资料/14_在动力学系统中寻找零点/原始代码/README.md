# 原始代码与数据：取得了什么，运行了什么

来源：[lqf2025/Riemann-data](https://github.com/lqf2025/Riemann-data)，对应Wei等2026年Nature Communications论文。下载日期2026-10-23，固定提交：

`a8b0b38202d6f330297212f8755c8df04242f9d6`

[固定版本](https://github.com/lqf2025/Riemann-data/tree/a8b0b38202d6f330297212f8755c8df04242f9d6)。提交号取自下载的GitHub归档版本标记，另存[记录](Wei_2026_commit.txt)。

## 本地保存范围

[Wei_2026](Wei_2026/README.md)是仓库子集：原README、MIT LICENSE、Fig2/4/5.py、GLA.py、Supplementary_Figure_1.py、data目录的生成程序、处理后的实验数据和理论NPZ。未将约百MB一份的GLA1/2/3数组纳入项目，也未复制作者已有PDF输出。因此不能据这个子集直接宣称全部图均可立即复现。

[原许可](Wei_2026/LICENSE)原样保留。[文件哈希清单](manifest.json)记录本地子集及生成的PDF。原始程序未改写。这里只读取公开数据，未向作者发信索取任何文件。

## 实际运行

在Wei_2026目录中运行：

```powershell
$env:MPLBACKEND = 'Agg'
python Fig4.py
```

运行成功，生成[Fig4.pdf](Wei_2026/Fig4.pdf)。该PDF是本地运行结果，不是从出版社下载的原图。其他作者脚本仅归档，没有全部运行。

本书四图另由[render_zero_dynamics.py](../../../03_第三篇_物理篇之混沌大陆/src/render_zero_dynamics.py)生成，依赖numpy、matplotlib、mpmath及本机微软雅黑字体；原实验数据布局沿用Fig4.py。独立求和与作者理论数据作复数级比较，误差约10⁻¹⁵。原仓库的处理后数据不等于原始采集时域信号，本轮没有重做实验数据处理或硬件实验。

He2021、Yu2024的数据声明均为可向作者合理请求，本轮未找到可下载的对应原代码。本文的离子、光散射、Newton流三图是依据论文公式的独立实现，图注已标明。

Wang两篇论文提供的[prime_logistic](https://github.com/maris205/prime_logistic)与[riemann_logistic](https://github.com/maris205/riemann_logistic)链接已记录，上一轮未运行。本轮按用户指定下载两个notebook并固定版本：间隔统计完整复算，谱仅重绘已保存的85项残差，未重跑完整求谱，详见[新增核对记录](../05_映射图与算力转场.md)。
