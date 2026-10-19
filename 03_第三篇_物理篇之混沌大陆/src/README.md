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
