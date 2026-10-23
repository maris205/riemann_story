# 图片源文件说明

本篇照片保留原文件字节，不提供裁剪、去水印或改图代码。逐图来源、作者、许可链接与校验值见 [img/README.md](../img/README.md)。

# 第16—18章原创图复现

运行：python render_ai_figures.py

输出至同篇img/：weil_pair_budget、curved_and_fixed_regions、proof_scope_and_quantifiers，各含PNG与SVG。依赖Python 3、numpy、matplotlib及/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc。图形为原创教学示意，不需要下载外部图片。原始数据仅包括显示坐标和定义的基本函数，均在源程序中；没有隐藏零点数据或论文图形。

自检包括窗函数常数2−R约0.6725007036794115、1−7/8=1/8，以及量词例子的有限样例检查。量词命题的完整数学解释见img/README.md，不以有限样例替代证明。

文件未新增开放许可证。数学与版权范围、推荐位置、中文图注和替代文本见../img/README.md。


# 六幅配图源程序

执行：python render_depth.py。需要Python、NumPy、Matplotlib、Noto Sans CJK字体，具体字体路径与色值见style_reference.py。输出本篇img/中的6个PNG和6个SVG。画布16×8英寸，PNG 180dpi得到2880×1440；SVG文本转路径。

release/families/coverage使用已注明日期的官方公开计数。certificate左侧曲线与右侧区间、epsilon显示坐标均是明确标注的教学例子，不是外部数据。程序断言722−3=719、300/719约42%、ε=δ/2。图注、来源、使用边界和alt见../img/README.md。原创内容未新增统一开放许可证。

---

# 第16—18章补图源程序

执行python render_finishing.py。figure_style.py保存统一画布、字体、配色及输出工具。所有数值为源中显式定义的简单教学数据：矩阵diag(4,1,1,0)、重数1/2/3、假设对称点、两条幂函数、五层奇数格子。没有外部零点数据或实际工程运行日志。

输出6个2880×1440 PNG与6个SVG，SVG字体转路径。完整图注、来源、数学边界、使用位置和alt见../img/README.md。未新增开放许可证。


---

# 重现第15章挂谷概念图

环境：Python 3，numpy，matplotlib；中文字体 Noto Sans CJK Regular。

运行：`python src/render_kakeya.py`（从本篇目录）；或以任意工作目录运行脚本的绝对路径。脚本按自身位置定位img/src。

输出PNG和SVG至img；端点数据unit_segments.csv和validation.json至src。固定72个球面半球方向，反向方向对应同一线段，不使用随机数。各中心作小幅确定性偏移；端点为中心±单位方向/2。用欧氏距离检查所有线段长为1。图形是有限示意，不是对全方向、零体积、分形维数的数值模拟。有限非退化线段并集的Hausdorff和盒维数均为1。

建议在原始2880×1440分辨率下检查中文字、图例及边界；SVG将字形转路径便于移植。本次PNG已实际查看并调整立方体与文字间距。

validation.json是运行时生成的数值核验记录，不属于书稿资产，不纳入仓库。

## 第16章史料图与算术检查

运行 `python prepare_chapter16_assets.py`，从本地PDF提取标题局部，并从原照片生成正文缩略图；使用PyMuPDF、Pillow、mpmath。脚本复算主常数、短区间常数与正文四数字例子，输出 `16_arithmetic_checks.json`。不联网，不改原件，不执行Lean工程。

## 第17章史料图

运行 `python prepare_chapter17_assets.py`，由本地NS论文提取Figure 1图形部分，并为双人照片生成展示缩略图。依赖PyMuPDF和Pillow；内置的均值与能量指数检查只是科普例子，不是NS模拟或Lean验证。


## 第18章图内章号更新（2026-10-23）

在本目录调用`python -c "import render_ai_figures as a; import render_finishing as b; a.regions(); b.envelope(); b.symmetry()"`可只重建本章三幅图，避免改写其他章节输出。所用样式支持Noto Sans CJK或Windows微软雅黑回退；数学内容不变，仅将图内旧章号17更正为18。[来源与解释边界](../../资料/18_被拉直的边界/图片与复现.md)。

## 第19章（2026-10-23）

`render_siegel_exercises.py`生成两幅原创教学图的PNG/SVG，并保存`19_teaching_checks.json`。解释大小/整除冲突与多项式重数，不是研究定理的数值验证。

## 第20章（2026-10-23）

`render_human_math.py`生成立方差分与证明翻译两幅教学图的PNG/SVG，保存`20_teaching_checks.json`。它核对差分和代数关系，不代表执行研究论文中的模型或Lean实验。

## 第21章（2026-10-23）

在本目录调用 `python -c "import render_depth as r; r.epsilon(); r.certificates(); r.constraints()"`，仅重绘本章两幅正文图和一幅留存图。将旧章号20改为21，样式增加Windows微软雅黑字体回退；输出PNG/SVG。数学内容与教学示意身份不变。[研究底稿](../../资料/21_未来之路/README.md)。
