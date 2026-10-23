from style_reference import *
from matplotlib.patches import Circle,FancyBboxPatch
ROOT=Path(__file__).resolve().parents[2]
def card(a,x,y,w,h,color=LIGHT):a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012,rounding_size=0.015',facecolor=color,edgecolor='none',alpha=.65))
def footer(f,line,small):
 f.text(.07,.10,line,fontsize=14,color=NAVY);f.text(.07,.045,small,fontsize=12,color=MUTED)
def release():
 f=base('722 → 719：把修改留在记录里','第19章 · 2026年10月6日发布与10月7日更改记录；手稿数量，不是已认证定理总数')
 a=panel(f,[.06,.25,.88,.53]);
 for x,date,n,label in [(.15,'10月6日','722','首次发布的手稿'),(.85,'10月7日','719','撤回后的目录')]:
  txt(a,x,.91,date,18,MUTED);txt(a,x,.61,n,62,TEAL);txt(a,x,.31,label,18)
 arr(a,(.3,.61),(.7,.61));txt(a,.5,.77,'− 3 份撤回',22,GOLD)
 txt(a,.5,.45,'1 份出现符号错误\n牵连 2 份依赖手稿',16)
 a.plot([.15,.85],[.09,.09],color=MUTED,lw=1);a.scatter([.15,.85],[.09,.09],color=TEAL,s=55)
 footer(f,'撤回影响什么，要追踪依赖关系；不能从“三份”推出其余全部有效或全部无效。','官方记录还列出其他修订与引用更新。此图是日期快照，不将719当作永久不变的数量。')
 save(f,'release_722_to_719')
def families():
 f=base('372 个结果族，不是另一份手稿总数','第19章 · 同一目录有两个计数单位：一组相关成果，可以拆成多份文本')
 a=panel(f,[.065,.24,.87,.55]);txt(a,.15,.86,'372',51,TEAL);txt(a,.15,.65,'结果族',21);txt(a,.15,.47,'2026-10-19 查阅目录\n共 719 份手稿',17)
 a.plot([.32,.32],[.06,.94],color=MUTED,lw=1,alpha=.4)
 card(a,.43,.4,.2,.23);txt(a,.53,.515,'一个结果族',20)
 for y,label in [(.86,'主论证'),(.64,'伴随论证'),(.42,'推论'),(.20,'另一种证明')]:
  arr(a,(.64,.515),(.77,y),c=MUTED);card(a,.79,y-.065,.17,.13);txt(a,.875,y,label,15)
 txt(a,.65,.025,'示意分支；不表示每族恰有四篇',14,GOLD)
 footer(f,'家族数、手稿数、独立难题数是不同口径，不能相互替换。','分支类别依据官方目录说明；这里没有绘制真实各族大小，也不推算“平均解决了几道猜想”。')
 save(f,'families_and_manuscripts')
def coverage():
 f=base('约42%，说明的是哪一层覆盖？','第19章 · 官方2026-10-07记录：300 / 719 项顶层结果有形式化；不是首发722份的比例')
 a=panel(f,[.06,.25,.88,.53]);x0=.02; width=.94
 a.add_patch(Rectangle((x0,.76),width,.14,facecolor=LIGHT,edgecolor='none'));a.add_patch(Rectangle((x0,.76),width*300/719,.14,facecolor=TEAL,edgecolor='none'))
 txt(a,x0+width*300/719/2,.83,'300 项',21,BG);txt(a,.7,.83,'其余未在此统计中列为形式化',16)
 txt(a,.5,.63,'这是顶层结果的覆盖统计，不是整篇每条推论的逐项保证',14,MUTED)
 for x,title,body in [(.17,'形式化检查','陈述、证明项、依赖\n与检查配置是否对应？'),(.5,'同行审阅','论证与解释是否经\n领域专家审查？'),(.83,'原创与意义','新颖性、独立问题数\n和数学价值如何判断？')]:
  a.add_patch(Rectangle((x-.13,.14),.26,.32,facecolor='none',edgecolor=GOLD,lw=1.5));txt(a,x,.38,title,18);txt(a,x,.23,body,13)
 footer(f,'三项问题彼此相关，但一个覆盖数字不能替另外两项回答。','没有同行评审率或独立难题总数的可靠统计，此图不画这些比例。未在此统计中形式化也不等于错误。')
 save(f,'formalization_coverage_scope')
def constraints():
 f=base('搜索一件乐器，先约束它能“偷看”什么','第21章 · 面向未来的谱搜索设想；算术输入可以有，目标零点不能被悄悄塞进边界条件')
 a=panel(f,[.06,.22,.88,.57]);
 card(a,.015,.37,.23,.40);txt(a,.13,.68,'独立结构输入',19);txt(a,.13,.52,'素数与轨道规则\n空间、作用与边界',15);txt(a,.13,.20,'不是“禁止输入素数”',13,MUTED)
 arr(a,(.26,.56),(.39,.56));a.add_patch(Circle((.5,.56),.105,facecolor=LIGHT,edgecolor=TEAL,lw=2));txt(a,.5,.56,'候选 H',22)
 for x,y,label in [(.47,.88,'定义域与自伴性'),(.82,.80,'周期与重复权重'),(.83,.34,'完整零点与重数'),(.48,.08,'正规化与极限')]:
  dx,dy=x-.5,y-.56;norm=(dx*dx+dy*dy)**.5
  arr(a,(.5+.11*dx/norm,.56+.11*dy/norm),(x-.04*dx/norm,y-.06*dy/norm),dashed=True);txt(a,x,y,label,16)
 txt(a,.84,.06,'均为必须证明的约束',12,GOLD)
 a.plot([.04,.22],[.29,.29],color=GOLD,lw=2);txt(a,.13,.31,'预存目标零点表',14,GOLD)
 footer(f,'低位谱相似只是候选线索；还须得到无遗漏、无多余的完整解析对应。','虚线表示研究任务，不是已经接通的证明。此图不预测哪条路线成功，也不宣称存在RH自动证明系统。')
 save(f,'spectral_search_constraints')
def certificates():
 f=base('一次失败，什么时候能成为证书？','第21章 · 将“值得降级的线索”与“严格排除一个模型”分开')
 a=panel(f,[.06,.25,.42,.54]);b=panel(f,[.55,.25,.39,.54]);txt(a,.5,.91,'数值失配：调整优先级',21);txt(b,.5,.91,'严格冲突：排除指定对象',21)
 xs=np.linspace(.1,.9,7);a.plot(xs,.3+.15*np.sin(xs*4),color=TEAL,lw=2,marker='o');a.plot(xs,.3+.15*np.sin(xs*4)+np.linspace(0,.25,7),color=GOLD,lw=2,marker='s')
 a.axvline(.49,ymin=.15,ymax=.66,color=MUTED,ls='--');txt(a,.28,.12,'拟合区',14,MUTED);txt(a,.71,.12,'留出区',14,MUTED)
 txt(a,.5,.72,'目标样本与候选预测',13,MUTED);txt(a,.5,.02,'有限误差或统计不符，本身未必严格否证',12,GOLD)
 b.plot([.1,.92],[.47,.47],color=MUTED,lw=1.5)
 for x,label in [(.16,'−1'),(.38,'0'),(.6,'1'),(.82,'2')]:b.plot([x,x],[.45,.49],color=MUTED);txt(b,x,.37,label,13)
 b.plot([.16,.27],[.47,.47],color=TEAL,lw=9,solid_capstyle='butt');b.plot([.6,.82],[.47,.47],color=GOLD,lw=9,solid_capstyle='butt')
 txt(b,.21,.65,'已证必要范围',13,TEAL);txt(b,.73,.65,'候选的认证范围',13,GOLD)
 txt(b,.5,.20,'两个区间不相交 → 不能同时成立',15);txt(b,.5,.02,'仅排除该候选／认证参数盒',13,GOLD)
 footer(f,'先证明被比较的量与必要条件确实对应，再给出严格误差包络。','左右均为教学示意，不是实测数据。右图人为选取区间[−1,−1/2]与[1,2]，没有宣称排除了某条现有谱路线。')
 save(f,'candidate_failure_certificate')
def epsilon():
 f=base('到达临界线，需要“每一个 ε”','第21章 · 有限次改善边界，不保证能逼近目标；全称量词才完成最后一步')
 a=f.add_axes([.09,.28,.82,.48],facecolor=BG);a.set_xlim(.45,.9);a.set_ylim(0,1);a.spines[['top','right','left']].set_visible(False);a.set_yticks([]);a.set_xticks([.5,.59,.68,.875],['1/2','1/2 + ε','1/2 + δ','7/8']);a.tick_params(axis='x',labelsize=16,colors=NAVY)
 a.axvspan(.59,.9,color=LIGHT);a.axvline(.5,color=TEAL,lw=2);a.axvline(.59,color=GOLD,lw=2,ls='--');a.axvline(.875,color=MUTED,lw=1,ls=':')
 a.scatter([.68],[.55],s=180,facecolor=BG,edgecolor=GOLD,lw=2.5);a.text(.68,.72,'假设的离线零点',ha='center',fontsize=20,color=NAVY)
 a.annotate('',xy=(.5,.23),xytext=(.68,.23),arrowprops=dict(arrowstyle='<->',color=TEAL,lw=2));a.text(.59,.12,'δ > 0',ha='center',fontsize=19,color=TEAL)
 a.text(.75,.08,'若每个 ε > 0 都成立，\n取 ε = δ/2 即将此点排除',ha='center',fontsize=17,color=NAVY)
 a.text(.52,.91,'RH目标',color=TEAL,fontsize=15);a.text(.86,.91,'一个固定界',ha='center',color=MUTED,fontsize=13)
 footer(f,'所需结论：每个 ε > 0，右侧 Re(s) > 1/2 + ε 都无零，而且覆盖全部高度。','s=1极点另处理；再由对称性排除左侧。空心点纯属反证示意，ε、δ显示值为任意选例，非已发现零点。')
 save(f,'every_epsilon_to_line')
if __name__=='__main__':
 release();families();coverage();constraints();certificates();epsilon()
 assert 722-3==719 and round(100*300/719)==42
 assert .59 == .5+(.68-.5)/2 or abs(.59-(.5+(.68-.5)/2))<1e-12
 print('six figures rendered; count and epsilon checks passed')
