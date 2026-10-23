# 配图源程序

运行：

```sh
python "render_spectral_figures.py"
```

可从任意工作目录运行；源程序按自身位置定位本篇的img目录。放回书稿后目录层级保持不变即可。输出PNG与SVG覆盖同名文件。

依赖：Python 3、NumPy、Matplotlib。此次渲染版本：NumPy 2.3.5、Matplotlib 3.10.8。中文字体使用Noto Sans CJK，默认路径 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc；其他系统可修改程序顶部FONT路径。无网络下载，无随机数种子需求。SVG将字形转为路径，接收方无需安装字体。

布局16×8英寸、180dpi，输出2880×1440像素。颜色与简化边界在脚本中直接定义，可编辑；数学依据、图注及插入位置见[图片说明](../img/README.md)。全部PNG已经逐张人工打开检查中文、公式、边界及留白。


## 新增原创配图与复现说明（2026-10-19）

# 第二批原创图源程序

运行 `python render_cantor_logistic.py`。可从任意目录运行，按源文件的位置写入本篇img目录，覆盖同名PNG、SVG。第三篇脚本还输出logistic_20_steps.csv，并在每次运行时独立检验全部轨迹点。

依赖Python 3、NumPy、Matplotlib、mpmath；高精度迭代使用Python标准库decimal。中文使用Noto Sans CJK，默认字体路径在脚本顶部FONT常量；若系统不同，可修改该路径。SVG字形转路径，阅读端无需安装字体。画布16×8英寸，180dpi，PNG为2880×1440。无网络依赖，无随机种子。

图注、数学来源、精确范围与简化说明见[图片目录](../img/README.md)。所有PNG均已逐张打开检查中文、公式、图例、边界与留白。

---

# 补充图源与复算

运行 `python src/render_finishing_figures.py`（从任意目录均可）。依赖 Python、NumPy、Matplotlib 和 Noto Sans CJK 字体。输出本篇 img 中 PNG（2560×1280）与 SVG（文字转路径）。本目录脚本自包含，仅运行属于本篇的函数。

全部为本项目原创解释图；没有第三方扫描、照片或论文图版。参数、公式、警告和绘图数据在源码中。窗口图另保存 CSV。脚本对莫比乌斯前十项及模型围道绕数作断言检查。


## 七幅原创物理解释图

在本篇目录运行 `python src/render_physics_depth.py`，生成第09章两图、第10章两图及第13章xp相空间图；运行 `python src/render_physics_extra.py`，生成第11章逆谱抵消图与第14章16态相位编码图。也可用脚本绝对路径从任意工作目录运行。两份程序需保持同目录，后者导入前者的绘图函数；按源文件位置定位本篇img目录。已有render_finishing_figures.py等程序保持原样，文件名没有冲突。

依赖Python 3、NumPy、Matplotlib及Noto Sans CJK字体，默认字体路径在render_physics_depth.py顶部FONT常量。无需网络。PNG为2560×1440，SVG字形转路径，运行覆盖各自同名图片。独立抽样使用固定种子20261019。额外脚本会在本篇目录生成quantum_validation.json数值核验文件；该运行产物不属于书稿资产，不纳入仓库。

第14章图按β=0.5、t=14.134725141734693、N=16实际计算，权重归一化，有限响应模约0.020280；并未人为设成精确零点。第13章图展示无量纲教学截断的面积积分，不声称完整实现Berry–Keating边界条件。详细图注、依据及适用范围见[图片说明](../img/README.md)。
## 第10节：洛伦兹蝴蝶图（2026-10-22）

[render_lorenz.py](render_lorenz.py)按经典三方程积分，输出[PNG](../img/10_lorenz_butterfly.png)、[NPZ轨迹](10_lorenz_trajectory.npz)及[JSON参数与核验](10_lorenz_metadata.json)。依赖NumPy、Matplotlib，Windows微软雅黑。初值(1,1,1)、RK4步长0.002、总时长100，绘图丢弃前5单位时间。

图展示x–z等比例投影，颜色按x编码，叠加描边只改变显示效果。步长减半仅在短时间t＝1交叉检查，长时混沌轨迹不以逐点重合作为要求。它是数值科普图，不是素数实验或混沌性质的严格证明。详见[图像底稿](../../资料/10_素数分布是混沌的吗/04_图片与视频素材.md)。

## 第10节：真实素数散射图

[render_prime_diffraction.py](render_prime_diffraction.py)以分段筛取一百亿附近5221颗素数，再按Torquato等论文定义计算散射强度。输出[配图](../img/10_prime_diffraction.png)、[数据](10_prime_diffraction_data.npz)与[核验记录](10_prime_diffraction_metadata.json)。依赖NumPy、Matplotlib；中文字体为微软雅黑。

## 第11节：素数与分形（2026-10-22）

[render_prime_fractals.py](render_prime_fractals.py)计算乌拉姆螺旋及欧拉40素数对角线、素数连分数柱区间、由v₂(n)编码的龙形折线，生成四幅PNG及[NPZ数据](11_prime_fractals_data.npz)、[核验记录](11_prime_fractals_metadata.json)。依赖NumPy、Matplotlib与微软雅黑，无网络和随机输入。按脚本位置定位输出，从任意目录可运行。具体解释和截断范围见[图片底稿](../../资料/11_素数与分形/04_图片与视频素材.md)。

## 第12节：孔涅路线的三幅解释图（2026-10-22）

[render_connes.py](render_connes.py)生成吸收谱示意、三阶托普利茨矩阵与单位圆、标准时间频率浓缩图。依赖NumPy、Matplotlib、mpmath与Windows微软雅黑；从任意目录运行。输出三张2520×1440 PNG、[NPZ数据](12_connes_data.npz)及[JSON核验](12_connes_metadata.json)。检查矩阵结构、根、归一化、120/200点求积及独立频带积分。它们是教学计算，不是孔涅55位零点实验的复现。详见[素材底稿](../../资料/12_Connes和他的学徒们/04_图片与视频素材.md)。

## 第13节：真实零点统计与闭合轨道（2026-10-23）

[render_prime_music.py](render_prime_music.py)读取已落地的Odlyzko一万颗高位零点，计算9999个展开间距，并绘制两能级避交和2011年紧化模型等值线。输出两幅PNG/SVG、[间距CSV](13_zero_spacings.csv)与[核验JSON](13_prime_music_metadata.json)。依赖NumPy、Matplotlib及Windows微软雅黑，从任意目录离线运行。原表偏移量直接差分，避免巨大高度浮点消减；GUE/GOE为Wigner近似，不称精确分布。

## 第14节：在动力学系统中寻找零点

[render_zero_dynamics.py](render_zero_dynamics.py)生成4组PNG/SVG、[中间数据](14_dynamics_data.npz)及[核验记录](14_dynamics_metadata.json)。依赖numpy、mpmath、matplotlib与Windows微软雅黑字体。运行：`python 03_第三篇_物理篇之混沌大陆/src/render_zero_dynamics.py`，可从项目根目录执行。

输入为[归档的Wei2026实验与理论数据](../../资料/14_在动力学系统中寻找零点/原始代码/README.md)。核磁共振数组对应遵循原Fig4.py，其余图按论文公式独立计算。代码内含理论复数求和值、数组坐标与导数样点校验；完整光学多次散射、原实验硬件与全部论文结论不在复现范围。

### 第14节：作者notebook增补图

[compute_wang_gap.py](compute_wang_gap.py)按原参数复算五亿素数范围与五亿步固定参数映射，使用numpy、numba；输出[计数数据](14_wang_gap_data.npz)及[参数记录](14_wang_gap_metadata.json)。流式计算省去4GB轨道数组，并与100000步字面Python递推核对。

[render_wang_examples.py](render_wang_examples.py)使用上述计数、原notebook保存的85项残差，以及核对原论文后的USTC表格，生成3组PNG/SVG、[谱绘图CSV](14_wang_spectral_plot.csv)与[核验记录](14_wang_examples_metadata.json)。依赖numpy、mpmath、matplotlib。完整非自治矩阵演化及20次求谱未重跑；图中标注保存结果身份与筛选条件。[详细记录](../../资料/14_在动力学系统中寻找零点/05_映射图与算力转场.md)。
