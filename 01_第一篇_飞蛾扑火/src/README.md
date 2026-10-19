# 原创示意图源程序

运行 `python render_atiyah_constant.py`，从任意工作目录均可；脚本按自身目录定位本篇img目录，输出同名PNG与SVG。

依赖Python 3、NumPy、Matplotlib及Noto Sans CJK字体。字体默认位置在脚本顶部FONT常量，可按本机环境修改。PNG尺寸2880×1440；SVG字形转为路径，显示端无需安装字体。无随机数据，无网络依赖。

图中只有137.036近似值与原手稿复合函数是数学标记；其余是原创概念图形，并不模拟物理装置或重建论文数据。图注、原始资料及使用范围见[图片说明](../img/README.md)。

# 原创图复现

运行 `python render_prime_gaps_siegel.py`。可从任意目录执行，源程序按自身位置定位本篇img目录，覆盖三个PNG及三个SVG。

依赖Python 3、NumPy、Matplotlib、Noto Sans CJK中文字体。FONT常量可改为本机字体路径。16×8英寸画布，180dpi，2880×1440像素。没有随机数据或网络依赖。

有限素数片段通过穷举试除即时验证；其余图为按公式绘制的概念/尺度示意。使用限制、史料及图注见[图片说明](../img/README.md)。
