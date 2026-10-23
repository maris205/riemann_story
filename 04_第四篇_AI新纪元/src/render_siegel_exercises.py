"""Chapter 19: original teaching diagrams, not numerical evidence for the theorem."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'img'
FONT = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family': FONT.get_name(), 'axes.unicode_minus': False,
                     'figure.facecolor': '#f7f3eb', 'axes.facecolor': '#f7f3eb',
                     'text.color': '#23323d', 'axes.labelcolor': '#23323d',
                     'svg.fonttype': 'path'})

def save(fig, name):
    fig.savefig(OUT / (name + '.png'), dpi=180, facecolor=fig.get_facecolor())
    p = OUT / (name + '.svg')
    fig.savefig(p, facecolor=fig.get_facecolor())
    p.write_text('\n'.join(line.rstrip() for line in p.read_text(encoding='utf-8').splitlines())+'\n', encoding='utf-8')
    plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 4.6))
fig.subplots_adjust(left=.08, right=.96, top=.74, bottom=.20)
fig.text(.08,.90,'一个整数，两种不相容的要求',fontsize=22,weight='bold')
fig.text(.08,.81,'M ≠ 0；8、9、5 两两互质，因此 360 必须整除 M',fontsize=13)
ax.axvspan(0,300,color='#237d8c',alpha=.14)
ax.axvspan(360,440,color='#b95f45',alpha=.15)
ax.axvline(300,color='#237d8c',lw=2,ls='--')
ax.axvline(360,color='#b95f45',lw=2)
ax.text(130,.62,'大小要求\n0 < |M| < 300',ha='center',va='center',fontsize=16,color='#196575',linespacing=1.7)
ax.text(400,.62,'整除要求\n|M| ≥ 360',ha='center',va='center',fontsize=14,color='#9e4936',linespacing=1.7)
ax.annotate('',xy=(359,.22),xytext=(301,.22),arrowprops={'arrowstyle':'<->','color':'#23323d','lw':1.5})
ax.text(330,.34,'无交集',ha='center',fontsize=11)
ax.set(xlim=(0,440),ylim=(0,1),yticks=[],xticks=[0,100,200,300,360],xlabel='非零整数的绝对值 |M|')
for sp in ['left','right','top']: ax.spines[sp].set_visible(False)
fig.text(.08,.055,'教学重构 · 数字 300 与 360 用于解释骨架，不是原论文常数。',fontsize=10,color='#64727a')
save(fig,'19_integer_budget')

fig, axes = plt.subplots(1,3,figsize=(10,4.4),sharex=True,sharey=True)
fig.subplots_adjust(left=.06,right=.97,top=.68,bottom=.24,wspace=.25)
fig.text(.06,.91,'同样是零，留下的信息不同',fontsize=22,weight='bold')
fig.text(.06,.81,'记录取值，再记录导数：有限的次数，容不下无限的消失条件。',fontsize=12)
x=np.linspace(-1.1,1.1,500)
for ax,n,c,label in zip(axes,[1,2,3],['#237d8c','#b78a32','#a25057'],['一重根：一阶导数不为零','二重根：一阶导数为零','三重根：前两阶导数为零']):
    ax.axhline(0,color='#9caaa9',lw=.8); ax.axvline(0,color='#9caaa9',lw=.8)
    ax.plot(x,x**n,color=c,lw=3); ax.scatter([0],[0],s=38,color=c,zorder=3)
    ax.set(xlim=(-1.15,1.15),ylim=(-1.3,1.3),xticks=[-1,0,1],yticks=[])
    ax.set_title(['P(t) = t','P(t) = t²','P(t) = t³'][n-1],fontsize=16,color=c,pad=12)
    ax.text(.5,-.28,label,transform=ax.transAxes,ha='center',fontsize=10)
    for s in ax.spines.values():s.set_visible(False)
fig.text(.06,.045,'辅助多项式的示意，非 L 函数零点图。多变量证明还需要结式与独立性论证。',fontsize=10,color='#64727a')
save(fig,'19_multiplicity')

checks = {'coprime_factors':[8,9,5],'product':8*9*5,'size_upper_bound':300,
          'sqrt3_mod7_coefficient':pow(3,3,7),'nonzero_square_residues_mod7':sorted({i*i%7 for i in range(1,7)}),
          'meaning':'pedagogical arithmetic only; not a verification of the research proof'}
assert checks['product']==360 and checks['sqrt3_mod7_coefficient']==6
(Path(__file__).parent/'19_teaching_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Created two PNG/SVG pairs and arithmetic-check metadata.')
