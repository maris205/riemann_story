import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/riemann-mpl-cache')
os.environ.setdefault('XDG_CACHE_HOME','/tmp/riemann-cache')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties,fontManager
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch
FONT='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc';fontManager.addfont(FONT)
plt.rcParams.update({'font.family':FontProperties(fname=FONT).get_name(),'font.size':15,'axes.unicode_minus':False,'mathtext.fontset':'dejavusans','svg.fonttype':'path'})
ROOT=Path(__file__).resolve().parents[1];BG='#F7F3E9';NAVY='#173346';TEAL='#178A86';GOLD='#B78734';MUTED='#637782';LIGHT='#D9E6DF';RED='#AE5B4A'
def base(title,sub):
 f=plt.figure(figsize=(16,9),facecolor=BG);f.text(.055,.925,title,fontsize=28,color=NAVY,weight='bold');f.text(.057,.875,sub,fontsize=14,color=MUTED);return f
def axis(f,rect,hide=False):
 a=f.add_axes(rect,facecolor=BG)
 if hide:a.axis('off');a.set_xlim(0,1);a.set_ylim(0,1)
 else:
  a.spines[['top','right']].set_visible(False)
  for spine in a.spines.values():spine.set_color(MUTED)
  a.tick_params(colors=MUTED);a.xaxis.label.set_color(NAVY);a.yaxis.label.set_color(NAVY)
 return a
def txt(a,x,y,s,size=16,c=NAVY,ha='center',**kw):a.text(x,y,s,fontsize=size,color=c,ha=ha,va='center',**kw)
def arrow(a,p,q,c=GOLD,dashed=False):a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=18,lw=2,color=c,linestyle='--' if dashed else '-'))
def save(f,name):
 f.savefig(ROOT/'img'/f'{name}.png',dpi=160,facecolor=BG);f.savefig(ROOT/'img'/f'{name}.svg',facecolor=BG);plt.close(f)
def roadmap():
 f=base('给黎曼的回信：问题没有变，工具变多了','从1859年的原始论文，到2026年的综述与书信：三种提问方式共同指向零点位置')
 a=axis(f,[.055,.2,.89,.63],True)
 a.plot([.04,.96],[.88,.88],color=MUTED,lw=2);a.scatter([.08,.92],[.88,.88],s=100,color=[TEAL,GOLD])
 txt(a,.08,.96,'1859',21,TEAL);txt(a,.92,.96,'2026',21,GOLD)
 txt(a,.08,.79,'黎曼发表论文',14);txt(a,.92,.79,'孔涅回望研究版图',14)
 txt(a,.5,.95,'一个尚未解决的问题',16)
 cards=[(.02,'分析：哪里不能有零点？','估计与零点分布','缩小可能区域\n研究临界线上的比例',TEAL),(.35,'谱：谁能产生全部零点？','自伴算子与完整对应','实谱提供约束\n对应关系仍须建立',GOLD),(.68,'几何：正性从哪里来？','空间、迹公式与二次型','寻找结构性理由\n让无穷输入一起受约束',TEAL)]
 for x,t,s,b,c in cards:
  a.add_patch(FancyBboxPatch((x,.08),.30,.53,boxstyle='round,pad=0.012,rounding_size=.02',edgecolor=c,facecolor=BG,lw=2))
  txt(a,x+.15,.53,t,17,c);txt(a,x+.15,.40,s,15);txt(a,x+.15,.22,b,15,linespacing=1.7)
  arrow(a,(x+.15,.73),(x+.15,.64),c)
 f.text(.07,.13,'共同目标：解释所有非平凡零点的位置。三栏是研究视角，并非三条已经走通的证明。',fontsize=15,color=NAVY)
 f.text(.07,.065,'路线会交叉：分析工具进入谱构造，几何结构帮助理解迹与正性。历史节点不表示问题已经解决。',fontsize=13,color=MUTED)
 save(f,'09_three_routes_letter')
def dictionary():
 f=base('素数与零点之间，需要一本“加权词典”','显式公式联结两侧；周期轨道的语言提供类比，但长度相似还不够')
 a=axis(f,[.05,.24,.9,.58],True)
 txt(a,.21,.95,'算术一侧：素数幂',22,TEAL);txt(a,.78,.95,'谱一侧：非平凡零点',22,GOLD)
 for yy,p in zip([.73,.53,.33],[2,3,5]):
  txt(a,.035,yy,str(p),16,TEAL)
  for k in range(1,4):
   x=.08+.085*k*np.log(p)
   a.scatter([x],[yy],s=60,color=TEAL)
   txt(a,x,yy+.085,rf'${p}^{k}$' if k>1 else str(p),13)
  a.plot([.08,.50],[yy,yy],lw=.8,color=LIGHT)
 txt(a,.25,.11,r'$\log(p^k)=k\log p$',21,TEAL)
 for yy,t in zip([.27,.4,.5,.65,.74],[14.1347,21.0220,25.0109,30.4249,32.9351]):
  a.plot([.70,.79],[yy,yy],lw=2,color=GOLD);txt(a,.81,yy,f'{t:.4f}',14,ha='left')
 txt(a,.80,.11,'前五个正虚部：已知零点示例',13)
 arrow(a,(.48,.53),(.66,.53),GOLD,True);txt(a,.57,.66,'测试函数',15);txt(a,.57,.40,'带权求和',15)
 f.text(.07,.17,r'$\Lambda(p^k)=\log p$',fontsize=21,color=TEAL)
 f.text(.31,.17,'素数幂的权重有规则；零点也需按测试函数与重数计入。',fontsize=15,color=NAVY)
 f.text(.07,.10,'还要加入极点、Γ因子等背景项。这里是对应结构示意，不是两串数直接相等。',fontsize=14,color=NAVY)
 f.text(.07,.045,'周期轨道类比：素数对应原始轨道，幂对应重复；振幅、符号和重复贡献仍须逐项匹配。',fontsize=13,color=MUTED)
 save(f,'09_weighted_prime_zero_dictionary')
def spacing():
 f=base('相邻间距：挤在一起，还是彼此避让？','平均间距统一为1后，比较两个概率密度模型；不是对实际零点的新计算')
 a=axis(f,[.08,.29,.56,.51]);s=np.linspace(0,3.5,1200);p=np.exp(-s);g=32/np.pi**2*s*s*np.exp(-4*s*s/np.pi)
 a.plot(s,p,color=GOLD,lw=3,label=r'Poisson：$e^{-s}$');a.plot(s,g,color=TEAL,lw=3,label='GUE：Wigner surmise（近似）')
 a.set_xlim(0,3.5);a.set_ylim(0,1.08);a.set_xlabel('归一化相邻间距 s');a.set_ylabel('概率密度');a.legend(frameon=False,fontsize=13,loc='upper right')
 a.annotate('小间距被压低',xy=(.18,float(32/np.pi**2*.18**2*np.exp(-4*.18**2/np.pi))),xytext=(.65,.24),arrowprops=dict(arrowstyle='->',color=TEAL),color=TEAL,fontsize=15)
 b=axis(f,[.69,.30,.26,.49],True)
 txt(b,.5,.90,'独立点过程',20,GOLD);txt(b,.5,.73,'小间距并不受排斥\n密度在 s＝0 为1',15,linespacing=1.6)
 txt(b,.5,.48,'GUE型能级排斥',20,TEAL);txt(b,.5,.28,'近零处按 s² 增长\n很近的邻居较少',15,linespacing=1.6)
 f.text(.08,.17,r'$P_{\mathrm{W}}(s)=\frac{32}{\pi^2}s^2\exp(-4s^2/\pi)$',fontsize=22,color=TEAL)
 f.text(.08,.095,'这条GUE曲线是2×2模型给出的Wigner近似，不是大矩阵极限的精确间距公式。',fontsize=14,color=NAVY)
 f.text(.08,.045,'零点统计中的相似性提供线索；既不能单独证明RH，也不能说明素数是独立随机抽样的。',fontsize=13,color=MUTED)
 save(f,'10_spacing_repulsion_models')
def primes():
 f=base('素数不像一把互不商量的硬币','同一排整数，比较真正的素数、独立抽样与最初两层整除限制')
 ns=np.arange(2,62);prime=np.array([all(n%d for d in range(2,int(n**.5)+1)) for n in ns]);rng=np.random.default_rng(20261019);selected=rng.random(len(ns))<np.minimum(1,1/np.log(ns))
 a=axis(f,[.045,.26,.91,.55],True)
 for block in range(3):
  chunk=ns[20*block:20*(block+1)];y=.91-block*.32
  for j,n in enumerate(chunk):
   x=.16+j*.042
   txt(a,x,y,str(n),11,MUTED)
   idx=n-2
   a.scatter(x,y-.085,s=85,facecolor=TEAL if prime[idx] else BG,edgecolor=TEAL if prime[idx] else LIGHT,lw=1)
   a.scatter(x,y-.17,s=85,facecolor=GOLD if selected[idx] else BG,edgecolor=GOLD if selected[idx] else LIGHT,lw=1)
   if n>3 and (n%2==0 or n%3==0):txt(a,x,y-.245,'×',14,RED)
  txt(a,.105,y-.085,'实际素数',13,TEAL,ha='right');txt(a,.105,y-.17,'独立抽样',13,GOLD,ha='right');txt(a,.105,y-.245,'被2或3筛掉',11,RED,ha='right')
 f.text(.07,.17,'独立抽样规则：每个 n 以 min(1, 1/log n) 的概率入选；固定种子的一次样本。',fontsize=14,color=NAVY)
 f.text(.07,.105,'真实素数受共同的整除约束：除2外不取偶数，除3外不取3的倍数。',fontsize=15,color=NAVY)
 f.text(.07,.045,'小数区间仅用于说明差别，1/log n 是渐近密度启发；通过2、3筛选的数也未必是素数，如25、49。',fontsize=12,color=MUTED)
 save(f,'10_primes_vs_independent_draws')
 return ns,prime,selected

def xp():
 f=base('xp：一条双曲线，怎样长出 E log E？','经典轨道与半经典面积计数的教学模型；边界条件与完整量子谱仍是另一道题')
 a=axis(f,[.08,.29,.47,.51]);x=np.linspace(.45,9.2,1200)
 for e,c in [(3,LIGHT),(5,GOLD),(8,TEAL)]:
  a.plot(x,e/x,color=c,lw=2.3,label=f'E = {e}')
 xx=np.linspace(1,8,500);a.fill_between(xx,1,8/xx,color=TEAL,alpha=.15)
 a.axvline(1,color=MUTED,ls='--');a.axhline(1,color=MUTED,ls='--');a.set_xlim(0,9);a.set_ylim(0,9);a.set_xlabel('位置 x');a.set_ylabel('动量 p');a.legend(frameon=False,fontsize=12)
 a.annotate('运动方向',xy=(4,2),xytext=(2,5.6),arrowprops=dict(arrowstyle='->',color=TEAL,connectionstyle='arc3,rad=-.2'),color=TEAL,fontsize=14)
 a.text(3.6,1.35,'截断后的面积',fontsize=13,color=TEAL)
 b=axis(f,[.60,.29,.35,.51],True)
 txt(b,.48,.94,r'$H=xp,\quad \dot{x}=x,\quad\dot{p}=-p$',20)
 txt(b,.48,.77,r'$x(t)=x_0e^t,\quad p(t)=p_0e^{-t}$',19)
 txt(b,.48,.58,'教学截断：x ≥ 1，p ≥ 1，xp ≤ E',14)
 txt(b,.48,.40,r'$A(E)=\int_1^E(E/x-1)\,dx$',22,TEAL)
 txt(b,.48,.22,r'$=E\log E-E+1$',23,TEAL)
 txt(b,.48,.04,r'$\overline{N}(E)\approx A(E)/(2\pi\hbar)$',21,GOLD)
 f.text(.07,.17,'E log E 的来源，是对双曲线下面的 1/x 积分。能量与截断均取教学性无量纲单位。',fontsize=14,color=NAVY)
 f.text(.07,.105,'原始轨道不会自行闭合；画出截断线不等于指定了自伴量子算子的边界条件。',fontsize=15,color=NAVY)
 f.text(.07,.045,'与黎曼零点平均计数的比较还需正确的尺度和边界处理；此图没有给出逐个零点或完整谱。',fontsize=13,color=MUTED)
 save(f,'13_xp_hyperbola_phase_area')
if __name__=='__main__':
 roadmap();dictionary();spacing();ns,ps,ss=primes();xp()
 import json
 s=np.linspace(0,12,100000);g=32/np.pi**2*s*s*np.exp(-4*s*s/np.pi)
 info={'spacing_normalization':float(np.trapezoid(g,s)),'spacing_mean':float(np.trapezoid(s*g,s)),'seed':20261019,'actual_primes':ns[ps].tolist(),'independent_draws':ns[ss].tolist(),'xp_area_E8':float(8*np.log(8)-8+1),'xp_area_integral_E8':float(np.trapezoid(8/np.linspace(1,8,100000)-1,np.linspace(1,8,100000)))}
 (ROOT/'validation.json').write_text(json.dumps(info,indent=2));print(info)
