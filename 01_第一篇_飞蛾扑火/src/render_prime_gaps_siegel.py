import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/riemann-mpl-cache')
os.environ.setdefault('XDG_CACHE_HOME','/tmp/riemann-cache')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties,fontManager
from matplotlib.patches import FancyArrowPatch
FONT='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc';fontManager.addfont(FONT)
plt.rcParams.update({'font.family':FontProperties(fname=FONT).get_name(),'font.size':14,'axes.unicode_minus':False,'mathtext.fontset':'dejavusans','svg.fonttype':'path'})
BG='#F7F3E9'; NAVY='#173346'; TEAL='#178A86'; GOLD='#B78734'; MUTED='#637782'; PALE='#D5DED6'
PART=Path(__file__).resolve().parents[1]
def base(title,sub):
 f=plt.figure(figsize=(16,8),facecolor=BG);f.text(.055,.90,title,fontsize=28,color=NAVY,weight='bold');f.text(.057,.846,sub,fontsize=13,color=MUTED);return f
def ax(f,r):return f.add_axes(r,facecolor=BG)
def clean(a):a.axis('off')
def tx(a,x,y,s,size=16,c=NAVY,ha='center'):a.text(x,y,s,fontsize=size,color=c,ha=ha,va='center')
def save(f,p,name):
 for e in ['png','svg']:f.savefig(p/'img'/f'{name}.{e}',dpi=180,facecolor=BG)
 plt.close(f)
def gaps():
 f=base('七千万跨过的，是“有界”这道门','2013—2014 年的三个历史节点 · 不是现时纪录表；省略了其间其他改进')
 a=ax(f,[.07,.46,.86,.31]);clean(a);a.set_xlim(0,1);a.set_ylim(0,1)
 a.plot([.07,.93],[.54,.54],color=PALE,lw=2)
 for x,num,who,year in [(.13,r'$<70\,000\,000$','张益唐','2013'),(.5,r'$\leq600$','Maynard','2013'),(.87,r'$\leq246$','Polymath8b','2014')]:
  a.scatter([x],[.54],s=75,color=TEAL);tx(a,x,.83,num,28,TEAL);tx(a,x,.31,who,16);tx(a,x,.1,year,13,MUTED)
 f.text(.075,.39,r'$H_1=\liminf_{n\to\infty}(p_{n+1}-p_n)<\infty$',fontsize=23,color=NAVY)
 f.text(.65,.40,'孪生素数要求更强的 $H_1=2$',fontsize=17,color=GOLD)
 b=ax(f,[.075,.19,.85,.14]);clean(b);b.set_xlim(99,133);b.set_ylim(-.6,1.4)
 primes=[101,103,107,109,113,127,131]
 # Trial division and exhaustive interval check: independent of any prime table.
 actual=[n for n in range(101,132) if all(n%d for d in range(2,int(n**.5)+1))]
 assert actual==primes
 b.plot([100,132],[0,0],color=PALE,lw=1.4)
 for p in primes:b.scatter([p],[0],s=58,color=TEAL);tx(b,p,-.43,str(p),12)
 for p,q in zip(primes[:-1],primes[1:]):
  b.plot([p,p,q,q],[.25,.55,.55,.25],color=GOLD,lw=1.4);tx(b,(p+q)/2,.92,str(q-p),13,GOLD)
 f.text(.075,.105,'下方是真实的有限素数片段。出现几次间距 2，不等于证明它出现无穷多次。',fontsize=14,color=NAVY)
 f.text(.075,.055,'有界间距也不是“所有相邻素数都不超过这个界”；保证的是无穷多次遇到短间距。',fontsize=13,color=MUTED)
 save(f,PART,'bounded_gaps_not_twins')
def siegel():
 f=base('先分清：哪一个函数，哪一种零点？','左侧是 RH 的全称目标；右侧是历史上被研究的假设性例外 · 图形不按零点数据绘制')
 a=ax(f,[.08,.29,.36,.46]);a.set_xlim(-.1,1.1);a.set_ylim(-.3,1);clean(a)
 tx(a,.5,.94,r'$\zeta(s)$',26);tx(a,.5,.77,'全部非平凡零点',16)
 a.fill_between([0,1],.05,.61,color='#E6EAE0')
 for x in [0,1]:a.plot([x,x],[.05,.61],color=MUTED,lw=1)
 a.plot([.5,.5],[.05,.61],color=TEAL,lw=2.7)
 for x,s in [(0,'0'),(.5,'1/2'),(1,'1')]:tx(a,x,-.02,s,13,MUTED)
 tx(a,.5,-.19,'RH：每个实部都等于 1/2',16,TEAL)
 b=ax(f,[.55,.29,.4,.46]);clean(b);b.set_xlim(-.05,1.08);b.set_ylim(-.3,1)
 tx(b,.5,.94,r'$L(s,\chi)$',26);tx(b,.5,.77,'χ 为本原、非主、实特征',15)
 b.plot([0,1],[.28,.28],color=MUTED,lw=1.5);b.plot([1,1],[.19,.37],color=NAVY,lw=1.5)
 b.plot([.69,1],[.28,.28],color=GOLD,lw=7,alpha=.45)
 b.scatter([.87],[.28],s=135,facecolors=BG,edgecolors=GOLD,lw=2,zorder=5);tx(b,.87,.48,r'$\beta$',22,GOLD)
 tx(b,0,.13,'0',13,MUTED);tx(b,.5,.13,'1/2',13,MUTED);tx(b,1,.13,'1',13,MUTED)
 tx(b,.5,-.07,r'$1-\frac{c}{\log q}<\beta<1,\quad\operatorname{Im}\beta=0$',19)
 tx(b,.5,-.23,'只盯着靠近 1 的实轴区间',15,GOLD)
 f.text(.075,.15,'○ 空心点表示“假如存在”的例外位置，不是发现过的西格尔零点。',fontsize=15,color=GOLD)
 f.text(.075,.075,'排除这段例外实零点，不能直接替代 ζ 的 RH，也不能替代关于整族 L 函数的 GRH。',fontsize=14,color=NAVY)
 save(f,PART,'siegel_zero_scope')
def scales():
 f=base('都贴近 1，却不是同一把尺子','令 δ = 1−β：把候选零点与 1 的距离，乘上 log q 再看')
 a=ax(f,[.075,.30,.39,.47]);clean(a);a.set_xlim(0,1);a.set_ylim(0,1)
 tx(a,.5,.92,'两种候选下界',20)
 tx(a,.5,.70,r'$\delta\geq\frac{c_1}{(\log q)^A}\quad(A>1)$',24,TEAL)
 tx(a,.5,.51,r'$\delta\log q\geq\frac{c_1}{(\log q)^{A-1}}$',20,TEAL)
 tx(a,.5,.30,r'$\delta\geq\frac{c_2}{\log q}$',24,GOLD)
 tx(a,.5,.10,r'$\delta\log q\geq c_2>0$',22,GOLD)
 b=ax(f,[.57,.33,.36,.41]);u=np.linspace(1,8,250);b.plot(u,u**-2,color=TEAL,lw=2.5);b.plot(u,np.ones_like(u),color=GOLD,lw=2.3)
 b.set_xlim(1,8);b.set_ylim(0,1.15);b.set_xticks([1,2,4,6,8]);b.set_yticks([0,.5,1]);b.set_xlabel(r'$u=\log q$',color=NAVY);b.set_ylabel('归一化后的下界',color=NAVY);b.tick_params(colors=MUTED)
 for side in ['top','right']:b.spines[side].set_visible(False)
 for side in ['left','bottom']:b.spines[side].set_color(PALE)
 tx(b,5.2,1.06,'统一的正常数门槛',13,GOLD);tx(b,5,.30,'这个下界随导子增大趋于 0',13,TEAL)
 f.text(.57,.24,'曲线仅演示 $A=3$、$c_1=c_2=1$ 的尺度差别',fontsize=12,color=MUTED)
 f.text(.075,.15,'2022 年张益唐预印本主张的实轴无零宽度使用 A=2024；这里不把该主张写成已证定理。',fontsize=13,color=NAVY)
 f.text(.075,.075,'高次对数幂对应更窄的缝。常数是否统一、能否有效计算，以及论证是否成立，都须另行核验。',fontsize=14,color=NAVY)
 save(f,PART,'siegel_logarithmic_scales')
if __name__=='__main__':gaps();siegel();scales()
