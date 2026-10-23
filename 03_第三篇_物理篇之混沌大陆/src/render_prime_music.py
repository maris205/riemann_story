"""Chapter 13: actual zero spacings and two classical Hamiltonians; offline."""
from pathlib import Path
import json
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
PART = HERE.parent
ROOT = PART.parent
font_manager.fontManager.addfont('C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family': 'Microsoft YaHei', 'font.size': 12,
                     'axes.unicode_minus': False, 'svg.fonttype': 'path'})
BG, INK, TEAL, GOLD, RED = '#faf7ef', '#233448', '#147d84', '#c08a34', '#ba5b51'

def style(ax):
    ax.set_facecolor(BG)
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(colors=INK)
    ax.grid(alpha=.15)

def save(fig, name, footer):
    fig.text(.05, .035, footer, color=INK, fontsize=10)
    fig.savefig(PART/'img'/f'{name}.png', dpi=180, facecolor=BG)
    fig.savefig(PART/'img'/f'{name}.svg', facecolor=BG)
    plt.close(fig)

raw = (ROOT/'资料/13_弹出素数的乐章/原始文献/Odlyzko_zeros_10e21.txt').read_text()
# Preserve supplied offsets: adding the huge integer base in float64 destroys gaps.
offsets = np.array([float(s) for s in raw.splitlines() if re.fullmatch(r'\s*\d+\.\d+\s*', s)])
assert len(offsets) == 10000 and np.all(np.diff(offsets) > 0)
base = 144176897509546973000
density = np.log(base/(2*np.pi))/(2*np.pi)
gaps = np.diff(offsets)*density
assert .98 < gaps.mean() < 1.02
np.savetxt(HERE/'13_zero_spacings.csv', np.column_stack((np.arange(1,10000), gaps)),
           delimiter=',', header='gap_offset_after_zero_10e21,unfolded_spacing', comments='')

fig, axes = plt.subplots(1, 2, figsize=(14, 6), facecolor=BG,
                         gridspec_kw={'width_ratios':[1,1.45]})
fig.subplots_adjust(left=.07, right=.97, top=.77, bottom=.19, wspace=.26)
fig.suptitle('琴键为何不愿挤在一起', x=.05, ha='left', y=.96, fontsize=25, color=INK)
fig.text(.05,.84,'左：最小的耦合模型    右：第 10²¹ 颗之后，10,000 颗黎曼零点的真实数据',color=INK)
ax=axes[0]; style(ax)
t=np.linspace(-2,2,501); g=.4
for sign in [-1,1]:
    ax.plot(t,sign*t,'--',color=GOLD,lw=1.8,label='无耦合：可以相交' if sign==1 else None)
    ax.plot(t,sign*np.sqrt(t*t+g*g),color=TEAL,lw=2.6,label='有耦合：避开相交' if sign==1 else None)
ax.annotate('',(0,g),(0,-g),arrowprops={'arrowstyle':'<->','color':RED,'lw':2})
ax.text(.12,.02,'最小间距 2g',color=RED,fontsize=10)
ax.set(xlabel='外部调节参数',ylabel='能级（任意单位）')
ax.legend(loc='upper left',fontsize=10,frameon=False)
ax=axes[1]; style(ax)
bins=np.arange(0,3.61,.12)
counts,edges=np.histogram(gaps,bins=bins)
ax.bar((edges[:-1]+edges[1:])/2,counts/(len(gaps)*.12),width=.112,
       color=TEAL,alpha=.35,label='零点间距 · 9,999 个')
s=np.linspace(0,3.6,600)
ax.plot(s,32/np.pi**2*s*s*np.exp(-4*s*s/np.pi),color=TEAL,lw=2.7,label='GUE · Wigner 近似')
ax.plot(s,np.pi/2*s*np.exp(-np.pi*s*s/4),color=GOLD,lw=2,ls='--',label='GOE · Wigner 近似')
ax.plot(s,np.exp(-s),color=RED,lw=1.8,ls=':',label='独立随机 · Poisson')
ax.set(xlim=(0,3.6),ylim=(0,1.08),xlabel='相邻间距 ÷ 当地平均间距',ylabel='概率密度')
ax.legend(frameon=False,fontsize=10)
save(fig,'13_zero_spacing','数据：A. Odlyzko，zeros4。曲线为参照，非拟合；有限数据支持统计线索，不能代替全部零点的证明。')

fig,axes=plt.subplots(1,2,figsize=(14,6),facecolor=BG)
fig.subplots_adjust(left=.07,right=.97,top=.77,bottom=.19,wspace=.25)
fig.suptitle('给逃走的轨道，一个归处',x=.05,ha='left',y=.96,fontsize=25,color=INK)
fig.text(.05,.84,'左：位置乘动量，沿双曲线远去    右：2011 年紧化模型，轨道自行闭合',color=INK)
ax=axes[0];style(ax)
x=np.linspace(1,10,1000); E=10
ax.plot(x,E/x,color=TEAL,lw=2.5)
ax.fill_between(x,1,E/x,color=GOLD,alpha=.30)
ax.axhline(1,color=GOLD,lw=1);ax.axvline(1,color=GOLD,lw=1)
ax.annotate('',(6,10/6),(5,2),arrowprops={'arrowstyle':'->','color':TEAL,'lw':2})
ax.text(3,4.4,r'$xp=E$',fontsize=21,color=TEAL)
ax.text(2.8,1.25,'量子小格装在这片面积里',fontsize=10,color=INK)
ax.set(xlim=(0,10.7),ylim=(0,10.7),xlabel='位置 x',ylabel='动量 p')
ax=axes[1];style(ax)
u=np.linspace(-2.2,2.2,600);U,V=np.meshgrid(u,u)
H=4*np.cosh(U)*np.cosh(V)
cs=ax.contour(U,V,H,levels=[5,8,14],colors=[TEAL,GOLD,RED],linewidths=2.5)
ax.clabel(cs,fmt=lambda v:f'E = {v:g}',fontsize=11)
ax.set(xlabel='log x',ylabel='log p',xlim=(-2.1,2.1),ylim=(-2.1,2.1))
ax.text(0,0,'最低能量 4',ha='center',va='center',color=INK)
ax.text(0,1.95,r'$H=(x+1/x)(p+1/p)$',ha='center',fontsize=15,color=INK)
save(fig,'13_xp_closed','无量纲教学图。左面积为 E log E − E + 1；右曲线由方程直接计算。轨道闭合与平均谱密度吻合，均不等于得到全部零点。')

# Numerical checks concern the explanatory calculations, not the cited proofs.
area=np.trapezoid(E/x-1,x)
exact=E*np.log(E)-E+1
assert abs(area-exact)<1e-4
for t0 in [-1.,0.,1.]:
    assert np.allclose(np.linalg.eigvalsh([[t0,g],[g,-t0]]),[-np.sqrt(t0*t0+g*g),np.sqrt(t0*t0+g*g)])
metadata={'zero_count':len(offsets),'gap_count':len(gaps),'mean_spacing':float(gaps.mean()),
          'local_density':float(density),'source':'https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros4',
          'offset_base':str(base),'source_accuracy':'probably within 1e-6; source does not guarantee',
          'area_numeric':float(area),'area_exact':float(exact),
          'curves':'GUE and GOE Wigner surmises, not exact infinite-dimensional spacing laws',
          'bounded_model':'Berry–Keating 2011; positive x,p; contour axes log x, log p'}
(HERE/'13_prime_music_metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(metadata,ensure_ascii=False))
