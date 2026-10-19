"""Original conceptual diagram, not a reconstruction of Atiyah's slides."""
import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/riemann-mpl-cache')
os.environ.setdefault('XDG_CACHE_HOME','/tmp/riemann-cache')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager
from matplotlib.patches import Circle,FancyArrowPatch
FONT='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fontManager.addfont(FONT)
plt.rcParams.update({'font.family':FontProperties(fname=FONT).get_name(),'font.size':15,'axes.unicode_minus':False,'mathtext.fontset':'dejavusans','svg.fonttype':'path'})
BG='#F7F3E9'; NAVY='#173346'; TEAL='#178A86'; GOLD='#B78734'; MUTED='#637782'
PART=Path(__file__).resolve().parents[1]
f=plt.figure(figsize=(16,8),facecolor=BG)
f.text(.055,.90,'从一个常数，到一个猜想',fontsize=28,color=NAVY,weight='bold')
f.text(.057,.848,'阿蒂亚 2018 年的尝试 · 虚线表示宣称中的联系，并非已建立的数学桥梁',fontsize=13,color=MUTED)
a=f.add_axes([.055,.31,.89,.46]);a.set_xlim(0,1);a.set_ylim(0,1);a.axis('off')
def tx(x,y,s,size=16,c=NAVY):a.text(x,y,s,fontsize=size,color=c,ha='center',va='center')
def arrow(p,q):a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=19,lw=2,color=GOLD,linestyle=(0,(4,4))))
for x,s in [(.14,'物理常数'),(.5,'提出的新工具'),(.87,'想抵达的结论')]:tx(x,.91,s,20)
# Charges and a stylized oscillating field: visual symbols, not particle trajectories.
for x,sign in [(.055,'+'),(.225,'−')]:
 a.add_patch(Circle((x,.58),.021,transform=a.transData,facecolor=BG,edgecolor=TEAL,lw=2));tx(x,.58,sign,19,TEAL)
x=np.linspace(.08,.20,150);a.plot(x,.58+.045*np.sin(np.linspace(0,5*np.pi,150)),color=TEAL,lw=2)
tx(.14,.34,r'$\alpha^{-1}\approx137.036$',22,TEAL)
tx(.14,.15,'无量纲的电磁耦合强度',13)
tx(.14,.035,'低能实验值，不是精确的 137',13,MUTED)
# Do not plot an invented Todd graph; the mathematical object is intentionally abstract.
a.add_patch(Circle((.5,.57),.081,facecolor='#E6EAE0',edgecolor='none'))
tx(.5,.57,r'$T$',40,TEAL);tx(.574,.69,'?',23,GOLD)
tx(.5,.34,'Todd 函数',19)
tx(.5,.15,'定义域？解析性？极限？',14,GOLD)
tx(.5,.035,'关键性质必须先得到证明',13,MUTED)
# Schematic target only, no actual or hypothetical off-line zero positions.
a.fill_between([.79,.95],.36,.76,color='#E6EAE0');a.plot([.79,.79],[.36,.76],color=MUTED,lw=1);a.plot([.95,.95],[.36,.76],color=MUTED,lw=1)
a.plot([.87,.87],[.36,.76],color=TEAL,lw=2.5)
for x,s in [(.79,'0'),(.87,'1/2'),(.95,'1')]:tx(x,.29,s,12,MUTED)
tx(.87,.15,'全部非平凡零点在线',14)
tx(.87,.035,'这是目标，不是已证结果',13,MUTED)
arrow((.285,.57),(.385,.57));arrow((.615,.57),(.745,.57))
tx(.335,.72,'尝试共用',12,GOLD);tx(.68,.72,'试图导出',12,GOLD)
f.text(.075,.22,r'$F(s)=T\!\left(1+\zeta(s+b)\right)-1$',fontsize=24,color=NAVY)
f.text(.56,.232,'手稿中的复合函数；b 是假设的离线零点',fontsize=13,color=MUTED)
f.text(.075,.12,'数值接近不能代替函数性质的证明。这里没有一条由 α 已知通向 RH 的推论。',fontsize=15,color=NAVY)
f.text(.075,.065,'这项宣称没有成为公认的 RH 证明；图中保留的是尝试的方向，以及尚未接通的环节。',fontsize=13,color=MUTED)
for ext in ['png','svg']:f.savefig(PART/'img'/f'atiyah_constant_to_conjecture.{ext}',dpi=180,facecolor=BG)
