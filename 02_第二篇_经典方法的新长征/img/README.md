# 第二篇图片来源与使用说明

人物照片分别记录来源页所列许可或权利状态，保留可核实的作者署名与原有水印、标识；本项目未裁剪、去水印、调色或重新编码。照片不因收入本仓库而改变许可。原图下载链接仅供核对出处，正文引用本目录中保留原文件字节的副本。

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



## 新增原创配图与复现说明（2026-10-19）

# 第二批原创数学图：量词与热流

两图均为本书原创，未复制或描摹论文图形。PNG为2880×1440，SVG字体转路径。使用方式与复现见[源程序](../src/README.md)。

## proportion_quantifiers

**建议位置：** 第06节区分无穷多个、正比例、比例趋于1与全部的段落之后。它解释命题强弱，不充当在线比例历史纪录图。

**图注：** 正整数中的平方数无穷多，却占比趋于0；偶数占一半；非平方数占比趋于1，却仍遗漏无穷多个平方数。RH要求“全部”，比任何允许例外的渐近比例都严格。图中圆点展示正整数1—64，而不是ζ零点。

**替代文本：** 四个8×8圆点阵依次选择平方数、偶数、非平方数、全部正整数。青色实心为入选，金色空心为未入选。下方给出对应的极限占比。

**数学性质：** 原创教学例子，图按从左到右、从上到下排列1—64。相应计数分别为8、32、56、64。一般N的计数严格为floor(sqrt(N))、floor(N/2)、N−floor(sqrt(N))、N；公式取N趋于无穷。未借有限网格估算渐近比例，未宣称实际存在离线零点。

**阅读依据：** 本篇第06节及参考文献中的[Bui–Conrey–Young](https://arxiv.org/abs/1002.4127)、[Pratt–Robles–Zaharescu–Zeindler](https://arxiv.org/abs/1802.10521)。论文用于在线比例概念背景，本图整数集合及构图独立设计，不声称图中一半是论文的零点结论或现时纪录。

## toy_heat_zero_collision

**建议位置：** 第07节“名叫热流，却要看清方向”，在二次多项式例子及根运动解释之后。

**图注：** 玩具多项式p_t(z)=z²−2t满足反向热方程∂ₜp_t=−∂²_zp_t。t从−1/2增加到0再到1/2，两根由±i合成二重根，再分开成为±1；倒退时间则反过来。这只是看清时间方向的模型，并非ξ函数的计算。

**替代文本：** 三个复平面依次显示虚轴上的±i、原点二重根、实轴上的±1，时间参数依次为−1/2、0、1/2。

**数学性质：** 图中三个状态为精确代数值。两边导数均为−2，已经用符号计算核对；六个根按重数逐一代入验证。此图采用把碰撞时刻平移到0的简单版本。正文p_t=z²−a²−2t可用τ=t+a²/2变成图中的形式，所以不与正文符号方向冲突。玩具分界0不能用于声称真实de Bruijn–Newman常数为0。

**阅读依据：** [Rodgers–Tao，The de Bruijn–Newman constant is non-negative](https://arxiv.org/abs/1801.05914)，尤其反向热方程与根运动背景；正文第07节的二次多项式说明。图不是论文数值结果的重绘。

---

# 第二篇：七幅方法深描图

全部原创程序绘制，不复制论文图片。各图PNG为2880×1440，附字体转路径SVG。精确计算、教学玩具、机制示意分别标明。复现及独立检查见[src](../src/README.md)。

## 04｜mobius_zero_detector

**位置：** 第04节“零点为何会逼出大值”，系数a_X的定义及前段抵消解释之后。

**图注：** 取X=6，截断莫比乌斯和与ζ相乘后，a_X(1)=1，2至6的系数全部抵消，信息留在尾部。柱高来自实际除数求和；级数恒等式先在Re(s)>1成立。要在临界带检测零点，还须平滑、截断与控制误差，不能直接代入原无穷级数。

**替代文本：** m=1至24的系数柱图，第一项为1，2至6全部为0，后续有正、负和零。

**验证与来源：** 程序以SymPy除数表和μ值生成24项，另用独立试除分解逐项核验，数据保存在detector_X6.csv。概念依据为第04节及[Guth–Maynard原文](https://arxiv.org/abs/2405.20552)的零点密度方法背景。图解释经典检测入口，不代表该论文完整检测器或数值结果。

## 05｜positive_trigonometric_barrier

**位置：** 第05节“一个非负的三角多项式”，第一次写出对数导数非负组合之后。

**图注：** 3+4cosθ+cos2θ=2(1+cosθ)²保证整条曲线非负。代入θ=t log n并按Λ(n)n⁻σ加权，在σ>1得到对数导数的不等式。若1+it是m重零点，σ趋于1时组合的主导系数3−4m−m₂为负，与非负性冲突。由直线排除进一步得到显式区域宽度，还需额外估计。

**替代文本：** 左侧非负曲线在π处接触0，两端为8。右侧对比对数导数的非负组合与假设边界零点导致的负主导项。

**准确范围：** t为固定非零实数，m≥1；m₂是1+2it处的零点重数，无零则取0。σ从右趋于1，O(1)可依赖固定t。D=−ζ'/ζ在s=1的极点留数为+1，在m重零点处留数为−m。三角恒等式经符号检查，不靠采样证明非负。这里是经典直线无零机制，不以一个图冒充精确R常数的证明。

**来源：** 第05节；[Mossinghoff–Trudgian，Nonnegative trigonometric polynomials and a zero-free region](https://arxiv.org/abs/1410.3926)与该篇参考文献中的Kadiri工作。此基础多项式为独立重绘，不是论文优化多项式的图。

## 05｜classical_boundary_parameter

**位置：** 第05节第一次解释“R越小结论越强”之后。

**图注：** 只比较公式σ=1−1/(R log|t|)：同一高度上，R=5的示例比R=6向左伸得更远；随着高度增长，两条曲线都趋近实部1。R=5与6在图中只是演示参数，并非声称某个已证定理或最新纪录。

**替代文本：** 纵轴log|t|从1至10，横轴实部σ。青色R=5边界在金色R=6边界左边，两曲线之间的窄带涂浅青色。

**验证与限制：** 真实函数公式按u=log|t|计算。两边界之差恰为−1/(30u)，u>0时严格为负。纵轴不是|t|的线性尺度。实际应用必须同时查清论文的常数、边界不等号与起始高度。本图不采用历史记录，避免把不同适用范围混为一谈。

**来源：** [Mossinghoff–Trudgian–Yang，Explicit zero-free regions](https://arxiv.org/abs/2212.06867)及第05节中的经典形状。曲线不是该文数值结论的重绘。

## 05｜zero_free_contour_shift

**位置：** 第05节“边界怎样变成素数误差”，在x^β与右侧零点影响的解释之后。

**图注：** 从实部大于1的积分路径向左移动，在无零走廊内绕过s=1。Perron被积函数−(ζ'/ζ)(s)x^s/s在s=1的留数给出主项x；新路径上x^σ较小，有利于节省误差。其他因子、横边、截断和端点仍要控制。

**替代文本：** 深蓝原路径在右，青色新路径在左，上下用虚线连接；金色s=1极点在两路径之间。左外侧空心符号仅指假设的零点，不是实际数据。

**限制：** x>1；示意路径始终位于正实部，新路径不穿过零点。左侧两个符号不是完整或满足对称性的零点集合，也不暗示已观察到离线零点。走廊形状为机制图，没有数值刻度与定理常数。所画留数关系不能代替Perron公式的截断误差或完整素数定理证明。

**来源：** 第05节与[Bombieri，Riemann Hypothesis问题说明](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)中零点、显式公式及素数计数的联系；图形独立设计。

## 06｜finite_mollifier_toy

**位置：** 第06节“给波动找一个搭档”，解释有限磨光因子希望在平均意义下改善乘积之后。

**图注：** 玩具函数f(t)=1−ae^(it)配上有限和M₃=Σₖ₌₀³aᵏe^(ikt)，得到fM₃=1−a⁴e^(4it)。a=0.65时，整周期二阶均值从1.4225降到约1.0319。这是可验算的有限逆近似，帮助理解改善均值的目标，不是ζ临界线数据。

**替代文本：** 金色|f|有较大起伏，青色|fM₃|在1附近小幅振荡；右侧列出两个精确二阶均值的公式。

**验证及限制：** 几何级数乘法恒等式已符号验证，曲线直接计算；均值由傅里叶正交性精确给出，并非拟合。a<1保证这个玩具在所画实t上无零。不能把玩具的均匀近似移植为ζ的处处可逆性；在ζ零点处任何有限M仍使ζM=0。没有把这个几何和称为实际Levinson磨光器。

**来源：** 第06节及[Bui–Conrey–Young原文](https://arxiv.org/abs/1002.4127)中的有限磨光与均值思想；玩具模型为本图原创。

## 07｜real_roots_quadratic_toy

**位置：** 第07节“另一条实根之路”专题，解释Jensen多项式实根性及量词要求时。

**图注：** 二次多项式q(x)=x²−2ax+b是否全部实根，由Δ=4(a²−b)决定。固定a=1，b=0、1、2依次给出两个实根、二重实根、共轭非实根。这只是实根判别的入门模型，不是从ξ系数计算出的Jensen多项式。

**替代文本：** 三条抛物线分别穿过、接触、完全高于实轴；下方列出根0与2、1与1、1±i。

**验证与限制：** 所有根及判别式经符号代入验证。实系数本身不保证实根；单个低次多项式通过检查，也不能代替真正判据中的全部次数和平移量词。

**来源：** [Griffin–Ono–Rolen–Zagier，Jensen polynomials](https://arxiv.org/abs/1902.07321)提供判据与量词背景；所画二次例子为独立教学构造，不复现原文数据。

## 08｜mobius_factor_trees

**位置：** 第08节“整数怎样决定一步”，μ的定义与几个例子之后。

**图注：** 12的分解重复出现素数2，因此μ(12)=0；30有三个不同素因子，μ(30)=−1；210有四个不同素因子，μ(210)=+1。先检查是否含平方因子，再数不同素因子的奇偶，顺序不能颠倒。

**替代文本：** 三棵因数分解树分别把12、30、210分解到素数叶子；12中的两个2以金色强调。

**验证与来源：** 所有分解和μ值由试除法、SymPy交叉核验。另有μ(1)=1。此图只解释μ定义，不宣称其取值独立随机；Liouville函数计算质因子总数且含重数，规则不同。背景见第08节与[Soundararajan，Partial sums of the Möbius function](https://arxiv.org/abs/0705.0723)。

---

# 原创补充图：来源、图注与边界

本批7张均为项目原创，无第三方图像复制。PNG与SVG同名配对。核验日期：2026-10-19。

## 第06章：argument_principle_toy
建议位置：“辐角原理提供一种桥梁”段后。
图注：用 f(z)=z²+1 演示辐角原理。半径1/2的围道不含根，像曲线绕原点0圈；半径3/2包含±i，像曲线绕原点2圈。像的大圆被走过两遍，几何轮廓本身不会显示遍历次数。
核验：f(re^{it})=1+r²e^{2it}，参数t从0至2π；无极点、围道无零点。源码用unwrap辐角复核绕数。不是ζ计算，也不把玩具例子当Levinson方法的完整证明。
数学依据：辐角原理标准定理；模型等式为独立直接计算。相关章节原始方法：N. Levinson, More than one third of zeros of Riemann's zeta-function are on σ=1/2, https://doi.org/10.1073/pnas.71.4.1013 。

## 第07章：jensen_quantifier_grid
建议位置：“每个固定次数、充分大平移”量词段后。
图注：示意表把次数排成行、平移排成列。假想门槛N(d)=d²使每行尾部都被覆盖，却不能清空全部灰格。实际定理的门槛并不是这张表给出的d²；灰格也不代表反例。
范围：只显示d=1…6、n=0…16。文字明确∀d ∃N(d) ∀n≥N(d)，与全部d,n的RH判据区分。
来源：Griffin–Ono–Rolen–Zagier, Jensen polynomials for the Riemann zeta function and other sequences（2019），https://arxiv.org/abs/1902.07321 。

## 第08章：mobius_short_windows
建议位置：“几乎所有”短区间的解释段后。
图注：三个长度30的实际莫比乌斯窗口，起点预先取100、800、1500。和分别为−3、−5、+4；相同长度不意味着每个窗口恰好零和。
数据：src/mobius_windows.csv，共90行。按素因子筛精确计算μ(1…2000)，画出(100,130]、(800,830]、(1500,1530]。青色+1，金色−1，灰点0。
范围：这些不是Matomäki–Radziwiłł定理的证明或统计验证，也没有宣称每个短区间平方根抵消。
来源：Matomäki–Radziwiłł, Multiplicative functions in short intervals, https://arxiv.org/abs/1501.04585 ，正式版 https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p06-p.pdf 。

## 第04章新增现场照片（2026-10-22）

以下三图直接保存哥本哈根大学数学系官方活动页发布的文件，未裁剪、调色、补画、去除标识或重新编码。活动页未列出这些现场照片的摄影者及开放许可，版权归原权利人；本章在介绍相关人物、讲座与数学思路时作有出处的场景引用，不标为项目原创、CC或公有领域。活动主页另有肖像注明摄影者或CC0，该标注不移用于本处的现场照片。

### maynard_copenhagen_conversation_2024.jpg

- 内容：梅纳德在2024年哈拉尔德·玻尔讲座活动中与人交谈，背景包括大厅壁画、茶歇纸杯与参会者。原页未明确该张摄于报告前还是报告后，正文不作具体断言。
- 发布方：哥本哈根大学数学系。[现场相册](https://www.math.ku.dk/english/calendar/events/hbl-maynard/photos-from-the-james-maynard-lecture/)，[讲座主题与介绍](https://www.math.ku.dk/english/calendar/events/hbl-maynard/)。
- [原图](https://www.math.ku.dk/english/calendar/events/hbl-maynard/photos-from-the-james-maynard-lecture/hbl_james_maynard_2024__01_.jpg)，1100×619，103143字节。
- SHA-256：`dd2aef7ae8db021c959e991ae477b2cd8f7e918b2f0ac96b562dde917743ae7f`。

### guth_copenhagen_kakeya_2025.jpg

- 内容：2025年11月21日，古思在王虹获奥斯特洛夫斯基奖的活动中作研究介绍；投影展示挂谷集合及不同方向的线段，画面保留讲台和黑板。本图不是2024年与梅纳德合作的现场，不把画中投影说成零点密度证明。
- 发布方：哥本哈根大学数学系。[活动与相册原页](https://www.math.ku.dk/english/calendar/events/ostrowski/)。
- [原图](https://www.math.ku.dk/english/calendar/events/ostrowski/ostrowski_wang__2_.jpg)，1100×733，54954字节。
- SHA-256：`4a31e2742a6d916c9fd7834acd5a509c4a178f611cd03ea5fbf77548fce65e16`。

### maynard_copenhagen_blackboard_2024.jpg

- 内容：2024年哈拉尔德·玻尔讲座“Prime numbers and zero densities”。梅纳德指向黑板上的黎曼显式公式，前景为听众和阶梯教室。
- 发布方：哥本哈根大学数学系。[现场相册](https://www.math.ku.dk/english/calendar/events/hbl-maynard/photos-from-the-james-maynard-lecture/)。
- [原图](https://www.math.ku.dk/english/calendar/events/hbl-maynard/photos-from-the-james-maynard-lecture/hbl_james_maynard_2024__08_.jpg)，1100×619，71687字节。
- SHA-256：`749fcdce3e1c83a42ae11305b9e05c9dc7b45b1b14b73f57481967ff7a8cfd25`。

第04章本次改写保留three_zero_fronts示意图；原maynard.jpg肖像与mobius_zero_detector示意图不再插入本章，原文件及说明保留供其他章节和后续修订使用。
