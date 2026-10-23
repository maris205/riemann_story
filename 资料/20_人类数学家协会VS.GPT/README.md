# 20 人类数学家协会 VS. GPT：研究底稿

核对日期：2026-10-23。对应[正文](../../04_第四篇_AI新纪元/20_人类数学家协会VS.GPT.md)。本章把原先以核验流程为主的文章，重组为人物处境、共同体分歧和可理解的数学例子。

## 叙事主线

AHM会员名单的小方框 → 研究生与教师的来信 → Gowers未签联名信的不同判断 → 量词与形式化依赖 → 自动翻译把错误论证改成正确证明 → 理解怎样使方法可迁移 → 接第21章《未来之路》，再由第22章书信收尾。

第17章已详述NS风波、25人联名信、批量发布与协会抗议，本章只简短回扣，不重新复述其全部事件。Gowers谈的是9月联名信，不是退出AHM；没有核实并声称他或Tao的AHM会员身份。协会并不代表全部数学家。

## 已保存原始材料

| 文件 | 版本／实际页数 | 本次阅读范围 |
|---|---|---|
| [Tao_2026_ICM_2608.16753v1.pdf](原始文献/Tao_2026_ICM_2608.16753v1.pdf) | arXiv v1，2026-08-17；下载PDF实际13页，摘要页Comments写12页 | 第1—3、7—10、12页；重点数学目标、Bourgain阅读回忆、理解链条、AI披露。不是数学定理证明论文 |
| [Tao_Math_2_0.pdf](原始文献/Tao_Math_2_0.pdf) | 10月9日Caltech讲义，30页；复用第17章已下载原件 | 读第1—19页及讲座博客；第20—22页思想实验只查阅，正文未采用；具体后续方向结合博客与既有章节核对 |
| [BCH_translation_audit.pdf](原始文献/BCH_translation_audit.pdf) | arXiv:2610.08144v1，25页；复用第17章原件 | 本次重点重读第1—4页的两类自动形式化与Example 2.1；NS部分沿用第17章第4—7页核对记录。未独立验证SCI层级理论与全部附录实验 |

文本提取保留PDF页码。哈希与来源记录见[manifest.json](原始文献/manifest.json)。没有在本章执行Lean或重新运行论文中的模型实验。

## 可复用笔记

- [人物与原始声明](人物与原始声明.md)：各人立场、证据层级和不可混淆的地方。
- [数学机制与视频脚本](数学机制与视频脚本.md)：差分降次、量词次序、分解错误和正确证明的区别。
- [图片与复现](图片与复现.md)：人物原图、两幅原创图、运行方式和授权状态。

网页资料以自写摘要和链接落地，没有复制整篇文章。Nature页面正文访问受限，只使用搜索可见的题名、日期、署名和导语来定位10月22日的公开立场。

## 原始来源索引

1. AHM：[宗旨](https://www.ahmath.org/)、[会员承诺与当日人数](https://www.ahmath.org/members)、[FAQ](https://www.ahmath.org/faq)、[10月7日声明](https://www.ahmath.org/statements)。人数是网站当日显示值，非永久统计。读取FAQ区别基础承诺与可选AI-free组别。
2. AHM：[成员提交AGMAI的意见选编](https://www.ahmath.org/agmai-comments)。正文只使用Evan Scott对个人求学时间与担忧的表述，不把选编里的数据挪用、犯罪等指控当作已证实事实。
3. AGMAI：[9月29日建议原文](https://agmai.org/general-sep29/)。反对专有模型测试与对既有成果负责发布两层都保留。
4. Álvaro Lozano-Robledo：[10月8日客座文章](https://terrytao.wordpress.com/2026/10/08/what-should-we-tell-our-students/)。阅读开篇、学生来信、个人处境与研究项目增加段落；未把文中关于模型能力“凸包”的猜测作为技术结论。
5. Sarah Al-Arshani，UConn Today，[2024-06-10本人采访与照片](https://today.uconn.edu/2024/06/math-professor-uses-tiktok-to-tackle-math-phobia/)。MathandCobb账号、沙拉、2021年开始发视频、观众决定学数学的来信。
6. Timothy Gowers：[2026-09-17本人文章](https://gowers.wordpress.com/2026/09/17/why-i-didnt-sign-the-fields-medallists-letter/)。阅读正文；童年故事带有本人明确的记忆重构限定。不同气质、不同判断，不归为“反人类”或“替公司站台”。
7. Lean官方：[Validating a Lean Proof](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)、[Axioms](https://lean-lang.org/doc/reference/latest/Axioms)。正文只讲命题、依赖和信任范围，不依赖某个UI颜色或某版本native公理的固定名字。
8. Bastounis、Circelli、Hansen：[arXiv版本页](https://arxiv.org/abs/2610.08144)。截至核对为v1；论文报告模型修改了错误推理，不能据此说正确形式化证明也错误。
9. Tao：[ICM文章](https://arxiv.org/abs/2608.16753)、[Math 2.0博客](https://terrytao.wordpress.com/2026/10/10/math-2-0/)、[30页讲义](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf)、[AIM正式活动记录](https://aimath.org/videos/terry-tao-pl/)。报告日期10月9日，博客发布10日。
10. Tao，Nature，[Can maths survive AI?](https://www.nature.com/articles/d41586-026-03389-1)，2026-10-22。仅核对公开题名与导语；不声称读到受限全文。

## 未采用材料

Gowers 10月16日的AI风险文章、网络上关于Math 2.0讲座的激烈二手评论，以及AHM意见页涉及其他事件的指控，会把本章引向不同问题，未纳入正文。人物图检索后采用可核实的UConn黑板照，不以未知场景图凑数。
