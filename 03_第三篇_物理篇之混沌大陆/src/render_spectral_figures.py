import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/riemann-mpl-cache')
os.environ.setdefault('XDG_CACHE_HOME','/tmp/riemann-cache')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.patches import FancyArrowPatch, Ellipse
FONT='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fontManager.addfont(FONT)
plt.rcParams.update({'font.family':FontProperties(fname=FONT).get_name(),'font.size':15,'axes.unicode_minus':False,'mathtext.fontset':'dejavusans','svg.fonttype':'path'})
BG='#F7F3E9'; NAVY='#173346'; TEAL='#178A86'; GOLD='#B78734'; MUTED='#637782'; LIGHT='#D9E6DF'
ROOT=Path(__file__).resolve().parents[2]
P2=ROOT/'02_第二篇_经典方法的新长征'; P3=ROOT/'03_第三篇_物理篇之混沌大陆'
def base(title,kicker):
 f=plt.figure(figsize=(16,8),facecolor=BG); f.text(.055,.90,title,fontsize=28,color=NAVY,weight='bold'); f.text(.057,.85,kicker,fontsize=13,color=MUTED); return f
def ax(f,rect):
 a=f.add_axes(rect,facecolor=BG); return a
def clean(a):
 for s in a.spines.values():s.set_visible(False)
 a.set_xticks([]);a.set_yticks([])
def txt(a,x,y,s,size=16,c=NAVY,ha='center',**kw):a.text(x,y,s,fontsize=size,color=c,ha=ha,va='center',**kw)
def arrow(a,p,q,c=GOLD,dashed=False):a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=17,lw=2,color=c,linestyle=(0,(4,4)) if dashed else '-'))
def save(f,part,name):
 f.savefig(part/'img'/f'{name}.png',dpi=180,facecolor=BG); f.savefig(part/'img'/f'{name}.svg',facecolor=BG); plt.close(f)
def bridge():
 f=base('从一条闭路，到全部零点','Hilbert–Pólya 谱设想 · 图中的虚线连接仍须证明，不能由统计吻合替代')
 a=ax(f,[.045,.28,.91,.51]);clean(a);a.set_xlim(0,1);a.set_ylim(0,1)
 xs=[.15,.5,.85]
 for x,t in zip(xs,['经典周期轨道','自伴量子算子','完整的零点对应']):txt(a,x,.91,t,20)
 t=np.linspace(0,2*np.pi,300);a.plot(.15+.09*np.cos(t),.54+.22*np.sin(t),color=TEAL,lw=2.2)
 arrow(a,(.235,.49),(.24,.57),TEAL);txt(a,.15,.54,r'$p,\ p^2,\ p^3$',17);txt(a,.15,.19,r'$\log p,\ 2\log p,\ 3\log p$',16)
 for yy in [.34,.44,.59,.68]:a.plot([.45,.55],[yy,yy],color=TEAL,lw=2)
 txt(a,.5,.79,r'$H=H^*$',21);txt(a,.5,.19,'定义域与边界也须确定',14)
 a.plot([.76,.94],[.54,.54],color=TEAL,lw=1.8);a.scatter([.78,.815,.87,.91],[.54]*4,s=44,color=TEAL)
 txt(a,.85,.73,r'$\rho=\frac{1}{2}+it$',23);txt(a,.85,.33,'无遗漏 · 无多余 · 重数对应',13);txt(a,.85,.19,'目标：所有 t 都是实数',14)
 arrow(a,(.28,.53),(.39,.53),GOLD,True);arrow(a,(.61,.53),(.72,.53),GOLD,True)
 txt(a,.335,.72,'自然构造',12,GOLD);txt(a,.665,.72,'精确全谱',12,GOLD)
 f.text(.075,.175,r'$\rho=\sigma+i\gamma\quad\longmapsto\quad t=-i(\rho-\frac{1}{2})=\gamma-i(\sigma-\frac{1}{2})$',fontsize=23,color=NAVY)
 f.text(.075,.095,'完整位置必须保留。只把虚部 γ 排成实数表，会丢掉是否偏离临界线的信息。',fontsize=14,color=NAVY)
 f.text(.075,.048,'周期长度的类比，还必须接上正确的振幅、符号与重复贡献。图中能级不代表实际零点数据。',fontsize=12,color=MUTED)
 save(f,P3,'hilbert_polya_bridge')
def bc():
 f=base('两个 β，两个不同的问题','Bost–Connes 的平衡系统与临界线量子模拟：共享符号，不共享同一个相变')
 a=ax(f,[.06,.29,.42,.48]);clean(a);a.set_xlim(0,1);a.set_ylim(0,1)
 txt(a,.5,.98,'对数能级 → 热权重',20)
 for n in range(1,9):
  y=.12+.53*np.log(n)/np.log(8);a.plot([.07,.3],[y,y],color=TEAL,lw=2);txt(a,.035,y,str(n),10,MUTED,ha='right')
 txt(a,.19,.76,r'$E_n=\log n$',18);arrow(a,(.34,.43),(.49,.43));txt(a,.74,.47,r'$e^{-\beta E_n}=n^{-\beta}$',21)
 txt(a,.52,-.045,r'$Z(\beta)=\sum_{n=1}^{\infty}n^{-\beta}=\zeta(\beta),\quad\beta>1$',22)
 b=ax(f,[.55,.29,.4,.48]);clean(b);b.set_xlim(0,1);b.set_ylim(0,1)
 txt(b,.5,.98,'先辨认模型，再读取参数',20)
 txt(b,.03,.8,'Bost–Connes：平衡态',15,ha='left');b.plot([.06,.94],[.63,.63],color=MUTED,lw=1.3);b.scatter([.47],[.63],s=90,color=GOLD)
 txt(b,.47,.54,r'$\beta=1$',17,GOLD);txt(b,.21,.7,'唯一 KMS 态',12);txt(b,.74,.7,'多个极端 KMS 态',12);txt(b,.18,.54,r'$0<\beta\leq1$',12,MUTED);txt(b,.79,.54,r'$\beta>1$',12,MUTED);txt(b,.5,.42,'关口对应 ζ 的极点',14,GOLD)
 txt(b,.03,.25,'零点模拟：复响应',15,ha='left');txt(b,.5,.08,r'$s=\beta+it,\qquad\beta=\frac{1}{2}$',23,TEAL);txt(b,.5,-.06,'临界线参数；并非样品的实际温度',13)
 f.text(.075,.135,'β ≤ 1 时，左侧普通热权重总和发散；KMS 平衡态不能靠这个发散的和来归一化。',fontsize=14,color=NAVY)
 f.text(.075,.075,'右下是另一模型的编码关系示意。有限项、读出误差与极限条件，均需单独处理。',fontsize=13,color=MUTED)
 save(f,P3,'bost_connes_two_betas')

if __name__=='__main__': bridge(); bc()
