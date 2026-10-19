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
ROOT=Path(__file__).resolve().parents[2];P2=ROOT/'02_第二篇_经典方法的新长征';P3=ROOT/'03_第三篇_物理篇之混沌大陆'
def base(title,sub):
 f=plt.figure(figsize=(16,8),facecolor=BG);f.text(.055,.90,title,fontsize=28,color=NAVY,weight='bold');f.text(.057,.846,sub,fontsize=13,color=MUTED);return f
def ax(f,r):return f.add_axes(r,facecolor=BG)
def clean(a):a.axis('off')
def tx(a,x,y,s,size=16,c=NAVY,ha='center'):a.text(x,y,s,fontsize=size,color=c,ha=ha,va='center')
def save(f,p,name):
 for e in ['png','svg']:f.savefig(p/'img'/f'{name}.{e}',dpi=180,facecolor=BG)
 plt.close(f)
def quantifiers():
 f=base('“无穷多”离“全部”还有多远？','用正整数集合解释量词 · 下方圆点只展示 1—64，并不是 ζ 零点样本')
 heads=['无穷多，也可占比为 0','占正比例，仍有大量例外','占比趋于 1，仍有例外','全部：不允许任何例外']
 subs=['平方数：1, 4, 9, 16, …','偶数：2, 4, 6, 8, …','所有非平方数','所有正整数']
 forms=[r'$\frac{\lfloor\sqrt{N}\rfloor}{N}\to0$',r'$\frac{\lfloor N/2\rfloor}{N}\to\frac{1}{2}$',r'$1-\frac{\lfloor\sqrt{N}\rfloor}{N}\to1$',r'$A=\mathbb{N}_{>0}$']
 for j in range(4):
  a=ax(f,[.055+.24*j,.24,.21,.52]);clean(a);a.set_xlim(-.7,7.7);a.set_ylim(-2.5,10.7)
  tx(a,3.5,10.1,heads[j],14);tx(a,3.5,8.9,subs[j],12,MUTED)
  for n in range(1,65):
   sq=int(np.sqrt(n))**2==n;inside=[sq,n%2==0,not sq,True][j]
   a.scatter((n-1)%8,7-(n-1)//8,s=65,facecolors=TEAL if inside else BG,edgecolors=TEAL if inside else GOLD,lw=1.3)
  tx(a,3.5,-1.65,forms[j],20)
 f.text(.075,.14,'● 属于集合     ○ 不属于集合',fontsize=14,color=NAVY)
 f.text(.075,.075,'极限占比只描述总体密度。RH 的“每一个”不容许稀疏例外，更不容许漏掉无穷远处。',fontsize=15,color=NAVY)
 save(f,P2,'proportion_quantifiers')
def heat():
 f=base('把时间倒退，两个实根会相撞','二次多项式玩具模型 · 仅演示反向热方程的符号与根的运动，不是 ξ 函数的零点数据')
 for j,t in enumerate([-.5,0,.5]):
  a=ax(f,[.07+j*.315,.31,.25,.39]);a.set_xlim(-1.6,1.6);a.set_ylim(-1.35,1.35);a.set_aspect('equal');a.set_xticks([]);a.set_yticks([])
  for s in a.spines.values():s.set_visible(False)
  a.axhline(0,color=MUTED,lw=1);a.axvline(0,color=MUTED,lw=1);tx(a,1.4,-.2,'Re z',11,MUTED);tx(a,.27,1.18,'Im z',11,MUTED)
  if t<0:a.scatter([0,0],[-1,1],s=100,color=GOLD);tx(a,-.65,1,r'$+i$',17,GOLD);tx(a,-.65,-1,r'$-i$',17,GOLD)
  elif t==0:a.scatter([0],[0],s=155,facecolors=BG,edgecolors=GOLD,lw=2.8);a.scatter([0],[0],s=33,color=TEAL);tx(a,.0,-.55,'二重根',14)
  else:a.scatter([-1,1],[0,0],s=100,color=TEAL);tx(a,-1,-.4,'−1',15);tx(a,1,-.4,'+1',15)
  a.set_title([r'$t=-\frac{1}{2}$',r'$t=0$',r'$t=+\frac{1}{2}$'][j],fontsize=24,color=NAVY,pad=20)
 f.text(.075,.215,r'$p_t(z)=z^2-2t,\qquad \partial_t p_t=-\partial_z^2p_t$',fontsize=24,color=NAVY)
 f.text(.70,.22,'t 增加：非实根 → 碰撞 → 实根分开',fontsize=13,color=TEAL,ha='center')
 f.text(.075,.12,'向左读：倒退 t，实根先靠近，碰撞后离开实轴。向右读：这是反向热方程的时间方向。',fontsize=14,color=NAVY)
 f.text(.075,.065,'这个玩具的分界点是 0，不代表真实 de Bruijn–Newman 常数已经证明等于 0。',fontsize=13,color=MUTED)
 save(f,P2,'toy_heat_zero_collision')

if __name__=='__main__':quantifiers();heat()
