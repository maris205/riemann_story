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
def detector():
 f=base('零点检测器，先让一长段系数消失','实际算术示例 X=6 · 展开恒等式先在 Re(s)>1 的绝对收敛区成立')
 f.text(.075,.74,r'$M_X(s)=\sum_{d\leq X}\mu(d)d^{-s},\qquad \zeta(s)M_X(s)=\sum_{m\geq1}a_X(m)m^{-s}$',fontsize=23,color=NAVY)
 from sympy import mobius,divisors
 n=np.arange(1,25);c=np.array([sum(int(mobius(d)) for d in divisors(int(m)) if d<=6) for m in n])
 assert c[0]==1 and np.all(c[1:6]==0)
 a=ax(f,[.075,.32,.85,.31]);a.axvspan(1.5,6.5,color='#E6EAE0');a.axhline(0,color=MUTED,lw=.9);a.bar(n,c,color=[GOLD if m==1 else TEAL for m in n],width=.5);a.scatter(n[c==0],c[c==0],s=22,color=TEAL);a.set_xticks([1,2,3,4,5,6,8,12,16,20,24]);a.set_yticks([-1,0,1]);a.set_ylim(-1.4,1.7);a.set_xlim(.3,24.7);a.set_xlabel('系数下标 m',color=NAVY);a.set_ylabel(r'$a_X(m)$',color=NAVY)
 for side in ['top','right']:a.spines[side].set_visible(False)
 tx(a,4,1.35,'2 至 6：全部抵消',14);tx(a,16,1.35,'尾部仍留下信息',14)
 f.text(.075,.22,r'$a_X(m)=\sum_{d\mid m,\ d\leq X}\mu(d)$',fontsize=22,color=NAVY)
 f.text(.075,.13,r'若 $\zeta(\rho)=0$，有限乘积 $\zeta(\rho)M_X(\rho)=0$；但不能把上方无穷级数直接代入临界带。',fontsize=14,color=NAVY)
 f.text(.075,.065,'从“尾项抵消开头的 1”走向零点检测，还需要平滑、积分表示、截断和误差控制。',fontsize=13,color=MUTED)
 np.savetxt(PART/'src'/'detector_X6.csv',np.column_stack([n,c]),fmt='%d',delimiter=',',header='m,a_X6',comments='');save(f,PART,'mobius_zero_detector')
def positivity():
 f=base('一条不会跌破零的曲线，怎样限制零点？','经典非负三角多项式 · 曲线是精确函数；右侧只展示在实部 1 排除零点的机制')
 a=ax(f,[.075,.36,.38,.36]);theta=np.linspace(0,2*np.pi,500);P=2*(1+np.cos(theta))**2;a.plot(theta,P,color=TEAL,lw=2.4);a.fill_between(theta,0,P,color=TEAL,alpha=.10);a.axhline(0,color=MUTED,lw=.8);a.set_xticks([0,np.pi,2*np.pi],['0',r'$\pi$',r'$2\pi$']);a.set_yticks([0,4,8]);a.set_xlabel(r'$\theta$',color=NAVY);a.set_ylim(-.4,8.6)
 for side in ['top','right']:a.spines[side].set_visible(False)
 f.text(.075,.26,r'$3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2$',fontsize=20,color=TEAL)
 b=ax(f,[.54,.33,.4,.43]);clean(b);b.set_xlim(0,1);b.set_ylim(0,1)
 tx(b,.5,.88,r'$D(s)=-\zeta^\prime(s)/\zeta(s)$',21)
 tx(b,.5,.65,r'$3D(\sigma)+4\operatorname{Re}D(\sigma+it)$',20)
 tx(b,.5,.51,r'$+\operatorname{Re}D(\sigma+2it)\geq0$',20)
 tx(b,.5,.28,'若 1+it 是 m 重零点（t≠0）',15,GOLD)
 tx(b,.5,.08,r'$\frac{3-4m-m_2}{\sigma-1}+O(1)<0$',23,GOLD)
 f.text(.075,.15,r'$\sigma>1$ 时代入 $\theta=t\log n$，乘以非负权重 $\Lambda(n)n^{-\sigma}$ 后求和；再令 $\sigma\downarrow1$。',fontsize=13,color=NAVY)
 f.text(.075,.075,r'极点贡献 3，假设零点至少贡献 −4；$m_2\geq0$ 是 $1+2it$ 处的零点重数。区域宽度还需更多估计。',fontsize=13,color=MUTED)
 save(f,PART,'positive_trigonometric_barrier')
def boundary():
 f=base('常数越小，无零走廊反而越宽','纯参数演示：R=5 与 R=6 · 不将这两个示例当作已经证明的常数或适用高度')
 a=ax(f,[.09,.24,.48,.52]);u=np.linspace(1,10,400);s5=1-1/(5*u);s6=1-1/(6*u);a.plot(s5,u,color=TEAL,lw=2.3,label='R=5');a.plot(s6,u,color=GOLD,lw=2.3,label='R=6');a.fill_betweenx(u,s5,s6,color=TEAL,alpha=.18);a.plot(np.ones_like(u),u,color=MUTED,lw=1);a.set_xlim(.78,1.012);a.set_ylim(1,10);a.set_xticks([.8,.9,1]);a.set_xlabel(r'$\sigma=\operatorname{Re}s$',color=NAVY);a.set_ylabel(r'$\log|t|$',color=NAVY);a.legend(frameon=False,loc='upper left');a.spines[['top','right']].set_visible(False)
 b=ax(f,[.65,.3,.28,.43]);clean(b);b.set_xlim(0,1);b.set_ylim(0,1)
 tx(b,.5,.85,r'$\sigma=1-\frac{1}{R\log|t|}$',24)
 tx(b,.5,.55,'较小的 R',19,TEAL);tx(b,.5,.4,'↓',25,TEAL);tx(b,.5,.25,'同一高度向左伸得更远',15)
 f.text(.075,.12,'两条曲线都在高处贴近实部 1。只优化一个固定常数 R，不会把整条边界推到 1/2。',fontsize=14,color=NAVY)
 f.text(.075,.06,'应用论文结果时，常数、边界不等号和起始高度必须一起使用；本图仅说明公式的方向。',fontsize=13,color=MUTED)
 save(f,PART,'classical_boundary_parameter')
def contour():
 f=base('把积分路径左移，主项与误差开始分开','复平面示意 · 不绘制真实零点位置；边界和路径不代表某条显式常数的数值结果')
 a=ax(f,[.075,.27,.49,.48]);a.set_xlim(.3,1.3);a.set_ylim(-1.7,1.7);clean(a)
 yy=np.linspace(-1.4,1.4,250);xx=.77+.10*abs(yy)/1.4
 a.fill_betweenx(yy,xx,1.23,color='#E6EAE0');a.plot(xx,yy,color=TEAL,lw=2.4);a.plot([1.19,1.19],[-1.4,1.4],color=NAVY,lw=2);a.plot([xx[0],1.19],[-1.4,-1.4],color=MUTED,ls='--');a.plot([xx[-1],1.19],[1.4,1.4],color=MUTED,ls='--')
 a.axhline(0,color=MUTED,lw=.6);a.plot([1,1],[-1.5,1.5],color=MUTED,lw=.7,ls=':');a.scatter([1],[0],s=90,color=GOLD,zorder=5);tx(a,1,-.25,'s=1 极点',13,GOLD)
 for x,y in [(.48,.75),(.60,-.85)]:a.scatter([x],[y],s=90,facecolors=BG,edgecolors=GOLD,lw=1.5)
 tx(a,.49,1.35,'假设零点符号',12,GOLD);tx(a,1.19,1.6,'原路径',13);tx(a,.77,1.6,'新路径',13,TEAL)
 a.add_patch(FancyArrowPatch((1.15,.48),(.92,.48),arrowstyle='-|>',mutation_scale=17,color=TEAL,lw=2))
 b=ax(f,[.62,.28,.32,.47]);clean(b);b.set_xlim(0,1);b.set_ylim(0,1)
 tx(b,.5,.87,r'$-\frac{\zeta^\prime}{\zeta}(s)\frac{x^s}{s}$',28)
 tx(b,.5,.59,'跨过 s=1，留数给出主项 x',15,GOLD)
 tx(b,.5,.36,r'$|x^{\sigma+it}|=x^\sigma$',23,TEAL)
 tx(b,.5,.12,'x>1 时，向左使幂次变小\n还须控制其余因子',15)
 f.text(.075,.15,'新路径须留在已证无零区域内，不能跨过未计入的零点；零点会成为对数导数的极点。',fontsize=14,color=NAVY)
 f.text(.075,.075,'截断高度、横边积分、端点与 Perron 误差均需处理。图只解释移动路径为何能带来误差节省。',fontsize=13,color=MUTED)
 save(f,PART,'zero_free_contour_shift')
def mollifier():
 f=base('找一个有限的搭档，让乘积少些起伏','可精确验算的玩具：f(t)=1−a exp(it)，a=0.65；不是 ζ 临界线的模拟数据')
 tt=np.linspace(0,2*np.pi,500);aa=.65;ff=1-aa*np.exp(1j*tt);mm=sum(aa**k*np.exp(1j*k*tt) for k in range(4));prod=ff*mm;assert np.max(abs(prod-(1-aa**4*np.exp(4j*tt))))<1e-14
 a=ax(f,[.075,.35,.55,.37]);a.plot(tt,abs(ff),color=GOLD,lw=2.2,label=r'$|f|$');a.plot(tt,abs(prod),color=TEAL,lw=2.2,label=r'$|fM_3|$');a.axhline(1,color=MUTED,lw=.8,ls='--');a.set_xticks([0,np.pi,2*np.pi],['0',r'$\pi$',r'$2\pi$']);a.set_ylim(.2,1.8);a.legend(frameon=False);a.set_xlabel('t',color=NAVY);a.spines[['top','right']].set_visible(False)
 b=ax(f,[.69,.36,.25,.37]);clean(b);b.set_xlim(0,1);b.set_ylim(0,1)
 tx(b,.5,.88,'整周期二阶均值',17);tx(b,.5,.60,r'$1+a^2=1.4225$',20,GOLD);tx(b,.5,.30,r'$1+a^8\approx1.0319$',20,TEAL)
 f.text(.075,.24,r'$M_3(t)=\sum_{k=0}^3a^ke^{ikt},\qquad f(t)M_3(t)=1-a^4e^{4it}$',fontsize=22,color=NAVY)
 f.text(.075,.14,'真正的磨光因子是截断、加权的狄利克雷和；目标是改善平均估计，不是处处变成 1。',fontsize=14,color=NAVY)
 f.text(.075,.065,'若 ζ(ρ)=0，任何有限且良好的 M 都仍有 ζ(ρ)M(ρ)=0。有限搭档不会把零点补成倒数。',fontsize=13,color=MUTED)
 save(f,PART,'finite_mollifier_toy')
def jensen():
 f=base('实根性：先看一个能完全算清的例子','二次多项式 q(x)=x²−2ax+b，固定 a=1 · 不是 ξ 系数生成的 Jensen 多项式')
 for j,bval in enumerate([0,1,2]):
  a=ax(f,[.075+.315*j,.34,.24,.37]);x=np.linspace(-.5,2.5,300);a.plot(x,x*x-2*x+bval,color=TEAL,lw=2.2);a.axhline(0,color=MUTED,lw=.8);a.axvline(1,color=PALE,ls='--');a.set_ylim(-1.3,3.8);a.set_xticks([0,1,2]);a.set_yticks([-1,0,1,3]);a.spines[['top','right']].set_visible(False);a.set_title(['b=0：两个实根','b=1：一个二重实根','b=2：无实根'][j],fontsize=16,color=NAVY,pad=14)
  if j==0:a.scatter([0,2],[0,0],s=60,color=GOLD,zorder=5)
  elif j==1:a.scatter([1],[0],s=90,facecolors=BG,edgecolors=GOLD,lw=2,zorder=5)
  tx(a,1,-1.9,[r'$0,\ 2$',r'$1,\ 1$',r'$1+i,\ 1-i$'][j],18,GOLD)
 f.text(.075,.21,r'$q(x)=(x-a)^2+(b-a^2),\qquad \Delta=4(a^2-b)$',fontsize=23,color=NAVY)
 f.text(.075,.12,'判别式 Δ≥0 才能保证这个二次多项式的全部根为实数；仅有实系数还不够。',fontsize=14,color=NAVY)
 f.text(.075,.065,'真正的 Jensen 判据要求完整的次数与平移参数范围；验证少数多项式，不能替代全部量词。',fontsize=13,color=MUTED)
 save(f,PART,'real_roots_quadratic_toy')
def mobius_tree():
 f=base('先查平方因子，再数不同的素数','莫比乌斯函数 μ(n) · 有平方因子就停步；无平方因子才看素因子个数的奇偶')
 for j,kind in enumerate([12,30,210]):
  a=ax(f,[.075+.315*j,.27,.25,.48]);clean(a);a.set_xlim(0,1);a.set_ylim(0,1)
  def node(x,y,s,color=TEAL):tx(a,x,y,str(s),21,color)
  def edge(x,y,u,v):a.plot([x,u],[y-.035,v+.04],color=PALE,lw=1.8)
  node(.5,.91,kind,NAVY)
  if kind==12:
   for x,s in [(.3,4),(.75,3)]:edge(.5,.87,x,.66);node(x,.66,s)
   for x in [.15,.45]:edge(.3,.62,x,.40);node(x,.40,2,GOLD)
   tx(a,.5,.19,r'$12=2^2\cdot3$',22);tx(a,.5,.04,r'$\mu(12)=0$',24,GOLD)
  elif kind==30:
   for x,s in [(.25,2),(.65,15)]:edge(.5,.87,x,.66);node(x,.66,s)
   for x,s in [(.48,3),(.82,5)]:edge(.65,.62,x,.40);node(x,.40,s)
   tx(a,.5,.19,'3 个不同素因子',16);tx(a,.5,.04,r'$\mu(30)=-1$',24,TEAL)
  else:
   for x,s in [(.25,6),(.75,35)]:edge(.5,.87,x,.66);node(x,.66,s)
   for x,s,parent in [(.1,2,.25),(.4,3,.25),(.6,5,.75),(.9,7,.75)]:edge(parent,.62,x,.40);node(x,.40,s)
   tx(a,.5,.19,'4 个不同素因子',16);tx(a,.5,.04,r'$\mu(210)=+1$',24,TEAL)
 f.text(.075,.15,'12 含重复的素因子 2，先归零；30 与 210 都没有平方因子，再按奇数 / 偶数决定正负。',fontsize=14,color=NAVY)
 f.text(.075,.075,'另定 μ(1)=1。这是整数分解决定的规则，没有掷硬币；也不同于总计重数的 Liouville 函数。',fontsize=13,color=MUTED)
 save(f,PART,'mobius_factor_trees')
if __name__=='__main__':detector();positivity();boundary();contour();mollifier();jensen();mobius_tree()
