# 配图源程序

运行：

```sh
python "render_classical_figures.py"
```

可从任意工作目录运行；源程序按自身位置定位本篇的img目录。放回书稿后目录层级保持不变即可。输出PNG与SVG覆盖同名文件；第二篇同时输出2000行原始CSV。

依赖：Python 3、NumPy、Matplotlib。此次渲染版本：NumPy 2.3.5、Matplotlib 3.10.8。中文字体使用Noto Sans CJK，默认路径 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc；其他系统可修改程序顶部FONT路径。无网络下载，无随机数种子需求。SVG将字形转为路径，接收方无需安装字体。

布局16×8英寸、180dpi，输出2880×1440像素。颜色与简化边界在脚本中直接定义，可编辑；数学依据、图注及插入位置见[图片说明](../img/README.md)。全部PNG已经逐张人工打开检查中文、公式、边界及留白。


## 新增原创配图与复现说明（2026-10-19）

# 第二批原创图源程序

运行 `python render_quantifiers_heat.py`。可从任意目录运行，按源文件的位置写入本篇img目录，覆盖同名PNG、SVG。第三篇脚本还输出logistic_20_steps.csv，并在每次运行时独立检验全部轨迹点。

依赖Python 3、NumPy、Matplotlib。中文使用Noto Sans CJK，默认字体路径在脚本顶部FONT常量；若系统不同，可修改该路径。SVG字形转路径，阅读端无需安装字体。画布16×8英寸，180dpi，PNG为2880×1440。无网络依赖，无随机种子。

图注、数学来源、精确范围与简化说明见[图片目录](../img/README.md)。所有PNG均已逐张打开检查中文、公式、图例、边界与留白。
