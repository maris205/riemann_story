# 第二篇图片来源与使用说明

人物照片按各自来源页所列许可使用，保留作者署名与原有水印、标识；本项目未裁剪、去水印、调色或重新编码。照片不因收入本仓库而改变许可。原图下载链接仅供核对出处，正文引用本目录中保留原文件字节的副本。

## tao.jpg

- 图注：陶哲轩在2006年马德里国际数学家大会。
- 作者／署名：Gert-Martin Greuel / MFO
- 来源文件页：[Terence Tao.jpg](https://commons.wikimedia.org/wiki/File:Terence_Tao.jpg)
- 原文件：[下载链接](https://upload.wikimedia.org/wikipedia/commons/1/12/Terence_Tao.jpg)
- 许可／权利状态：[CC BY-SA 2.0 DE](https://creativecommons.org/licenses/by-sa/2.0/de/)
- 修改：无；原文件字节、原有标识保持不变。
- SHA-256：`a19ba86ff455c84370b75b1c75dc2a5e0c513beeea95685a4c9ee59a975c4e7f`
- 范围说明：此处仅使用 Commons 已公布的低分辨率版本，不延伸至 MFO 档案中的高清原片。

## maynard.jpg

- 图注：詹姆斯·梅纳德，2013年于奥伯沃尔法赫。
- 作者／署名：Petra Lein / MFO
- 来源文件页：[James Maynard MFO 2013.jpg](https://commons.wikimedia.org/wiki/File:James_Maynard_MFO_2013.jpg)
- 原文件：[下载链接](https://upload.wikimedia.org/wikipedia/commons/e/ea/James_Maynard_MFO_2013.jpg)
- 许可／权利状态：[CC BY-SA 2.0 DE](https://creativecommons.org/licenses/by-sa/2.0/de/)
- 修改：无；原文件字节、原有标识保持不变。
- SHA-256：`8566d3a496238e1862fffb9a4e584db98780faedef5f9a7797cfc84385357718`
- 范围说明：此处仅使用 Commons 已公布的低分辨率版本，不延伸至 MFO 档案中的高清原片。

## 本项目原创数学示意图

作者／制作：本项目原创配图；来源：本篇 [src](../src/README.md) 中的复现程序。以下文献是数学依据，不是图片复制来源；未为原创图或源程序另行新增开放许可证。

### 第二篇原创数学图

本目录图片由本书配图程序原创绘制，没有复制、裁切或描摹论文插图。采用统一的象牙底、深蓝正文、青绿对象、金色限制提示。PNG 为 2880×1440；SVG 中字体已转为路径，便于跨设备显示。复现见 [src](../src/README.md)。

## three_zero_fronts.png / .svg

**图注：** 同一条临界带，三种问题。无零区域排除某片空间中的零点，密度估计约束偏离中央的数量，在线比例保证临界线上的渐近占比。空心点仅表示假设性例外，绝不是已经发现的离线零点；渐近占比为1仍允许零密度例外。

**建议位置：** 第04节第一次区分零点密度与RH后，作为第04—06节共用地图；或第二篇目录的导言后。避免在三章中重复嵌入。

**性质及简化：** 完全为概念示意。纵坐标没有数值刻度，所有点的位置、个数、边界曲线均非论文数据。曲线只表现经典无零区域随高度收窄，不代表任何显式常数或2026年固定半平面。右图有限点数不用于计算比例。

**数学来源：** [Guth–Maynard，零点密度](https://arxiv.org/abs/2405.20552)；[Mossinghoff–Trudgian–Yang，无零区域](https://arxiv.org/abs/2212.06867)；[Bui–Conrey–Young，在线比例](https://arxiv.org/abs/1002.4127)。对应本篇参考文献的前三组；这里只借用三类命题的结构，不重绘论文结果曲线。

**替代文本：** 三个并列临界带：左图实部1附近金色区域无零，中图在σ右侧统计假设例外，右图强调中央实部二分之一上的比例。空心点并非实测。

## mobius_walk_2000.png / .svg

**图注：** 按整数素因子算出的莫比乌斯累计和，n从1到2000。青线是真实计算的阶梯曲线，金色虚线是正负平方根尺度。有限图像不能证明RH；将虚线当作永不越过的硬界，得到的是已被否定的Mertens猜想。

**建议位置：** 第08节“平方根从哪里来”末尾，进入“一条折线怎样接到黎曼猜想”之前。也可紧接Mertens和的首次定义。

**计算与核验：** 用整数筛法独立计算全部2000个μ(n)，并逐一与SymPy的mobius函数交叉核验；M(2000)=5。绘制右连续阶梯，不做随机抽样、平滑或拟合。完整数据见 [CSV](../src/mobius_1_2000.csv)。图像不展示Mertens猜想反例，也没有声称这个范围已经出现越界。

**数学来源：** [Odlyzko–te Riele，Disproof of the Mertens conjecture](https://ir.cwi.nl/pub/1823/1823D.pdf)；[Soundararajan，Partial sums of the Möbius function](https://arxiv.org/abs/0705.0723)。分别支持强界已被否定、RH所需增长估计的区别；图片数据由定义计算，不取自论文。

**替代文本：** 2000步确定性的莫比乌斯累计曲线在零附近起伏，正负平方根虚线向两侧张开，仅作尺度参照。

