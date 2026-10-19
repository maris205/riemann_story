# 配图源程序

运行：

```sh
python "render_classical_figures.py"
```

可从任意工作目录运行；源程序按自身位置定位本篇的img目录。放回书稿后目录层级保持不变即可。输出PNG与SVG覆盖同名文件；第二篇同时输出2000行原始CSV。

依赖：Python 3、NumPy、Matplotlib。此次渲染版本：NumPy 2.3.5、Matplotlib 3.10.8。中文字体使用Noto Sans CJK，默认路径 /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc；其他系统可修改程序顶部FONT路径。无网络下载，无随机数种子需求。SVG将字形转为路径，接收方无需安装字体。

布局16×8英寸、180dpi，输出2880×1440像素。颜色与简化边界在脚本中直接定义，可编辑；数学依据、图注及插入位置见[图片说明](../img/README.md)。全部PNG已经逐张人工打开检查中文、公式、边界及留白。
