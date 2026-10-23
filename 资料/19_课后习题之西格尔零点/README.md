# 19 课后习题之西格尔零点：研究底稿

核对日期：2026-10-23。对应[正文](../../04_第四篇_AI新纪元/19_课后习题之西格尔零点.md)。

本章以“答案如何成为可传授的知识”为主线，回扣第一篇张益唐与西格尔零点，承接第18章的准黎曼假设。没有找到把完整新证明布置为普通本科作业的可靠原始记录；标题是文学引题，整数300/360练习为本书自编。Tao 10月20日的公开项目是研究挑战，正文明确区分。

## 原始材料与阅读范围

| 材料 | 版本与篇幅 | 本次阅读及用途 |
|---|---|---|
| OpenAI，Uniform exclusion of Landau–Siegel zeros | 2026-10-01，9页；10月6日发布批次 | 阅读全文，追踪定理、解析输入、插值行列式、范数、大小与整除条件；未独立验证完整证明 |
| William D. Banks，On the OpenAI proof that Landau–Siegel zeros do not exist | arXiv:2610.15483v1，10月11日，19页 | 重点读第1—3页及第19页，核对直接证明、显式常数及AI使用声明；中间技术推导不声称逐项复核 |
| Bryce Kerr，A simpler proof that there are no Landau–Siegel zeros | arXiv:2610.21099v1，10月15日，6页 | 阅读全文，重点抽屉原理、范数迫使取值为零、Masser次数下界；未独立复核所引1981年定理 |
| Ben Green，On Landau–Siegel zeros | Hexagon:2610.00311v2，初稿10月17日、修订18日，5页，CC BY 4.0 | 阅读全文与结式附录；正文的详细数学路线主要依据此稿 |
| Terence Tao，A sketch of the proof of non-existence of Siegel zeroes | 10月19日博客 | 阅读开头、§1—3及§4开头和Green相关评论；用作讲解与协作记录，不把博客的简化假设代替一般定理 |
| Terence Tao，An experimental AI-math challenge… | 10月20日博客 | 阅读正文；只述项目目标和规则，不报告未经核对的评论区新计算结果 |

四份PDF及带PDF页码标记的文本见[原始文献](原始文献/)。下载链接、页数和SHA-256见[manifest.json](原始文献/manifest.json)。网页资料保存为下列自行整理的Markdown要点，未整篇复制评论或采访。

- [论文与数学机制](论文与数学机制.md)：定理边界、证明路线对照、教学类比的边界。
- [人物与视频线索](人物与视频线索.md)：版本时间线、AI贡献声明、可用故事和镜头。
- [图片与复现](图片与复现.md)：原图来源、两个原创示意图及算术核对。

## 原始链接

1. OpenAI：[九页原稿](https://github.com/openai/math/blob/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf)。独立伴随论证，与同成果族两份准黎曼假设稿区分。
2. Banks：[arXiv摘要及版本](https://arxiv.org/abs/2610.15483)。全范围0.003结论还使用Lu、Zaman、Zhao的有限范围计算，本次未重新运行该计算，也未另行精读其原论文。
3. Kerr：[arXiv摘要及版本](https://arxiv.org/abs/2610.21099)。六页正文依赖Masser旧定理，不是六页初等证明。
4. Green：[Hexagon v2及溯源声明](https://hexagonmath.org/2610.00311v2)。网页主日期为初始提交日，历史页列v2为10月18日；PDF页数包含附录和参考文献。
5. Tao：[10月19日讲解](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/)。Green留言提及收到四页与三页变体；本次未取得这两份原稿，不能当作独立审读成果。
6. Tao：[10月20日研究挑战](https://terrytao.wordpress.com/2026/10/20/an-experimental-ai-math-challenge-using-tenth-discriminant-bounds-to-explore-arguments-ruling-out-siegel-zeroes/)。利用新方法估计假想第十个判别式，禁止直接调用Heegner解法绕过问题；允许AI并要求披露。

没有把预印本写成期刊已经审定或奖项机构已认证；本书做的是原稿阅读、机制解释及小例子的核对，未运行相关Lean工程。
