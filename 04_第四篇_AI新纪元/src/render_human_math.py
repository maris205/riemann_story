"""Chapter 20 teaching figures: finite differences and a repaired factorization."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'img'
FONT=FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':FONT.get_name(),'axes.unicode_minus':False,
 'figure.facecolor':'#f7f3eb','axes.facecolor':'#f7f3eb','text.color':'#23323d',
 'axes.labelcolor':'#23323d','svg.fonttype':'path'})

def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=180,facecolor=fig.get_facecolor())
    p=OUT/(name+'.svg');fig.savefig(p,facecolor=fig.get_facecolor())
    p.write_text('\n'.join(l.rstrip() for l in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

levels=[np.arange(6)**3]
for _ in range(3):levels.append(np.diff(levels[-1]))
assert levels[-1].tolist()==[6,6,6]
fig,ax=plt.subplots(figsize=(10,5.1))
fig.subplots_adjust(left=.03,right=.97,top=.77,bottom=.11)
fig.text(.06,.91,'立方数，一层一层卸去次数',fontsize=22,weight='bold')
fig.text(.06,.82,'把相邻两项相减；重复三次，留下同一个 6。',fontsize=12)
colors=['#23323d','#237d8c','#b78a32','#a25057']
labels=['立方数','一次差分','二次差分','三次差分']
for k,row in enumerate(levels):
    y=3-k
    ax.text(-1.55,y,labels[k],ha='left',va='center',fontsize=12,color=colors[k])
    for j,n in enumerate(row):
        x=j+k*.5
        ax.text(x,y,str(n),ha='center',va='center',fontsize=22,color=colors[k],weight='bold',bbox={'boxstyle':'round,pad=.30','facecolor':'#ede8dc','edgecolor':'none'})
        if k<3 and j<len(row)-1:
            ax.annotate('',xy=(x+.5,y-.72),xytext=(x+.08,y-.20),arrowprops={'arrowstyle':'-','color':'#c4c7bf','lw':1.1})
            ax.annotate('',xy=(x+.5,y-.72),xytext=(x+.92,y-.20),arrowprops={'arrowstyle':'-','color':'#c4c7bf','lw':1.1})
ax.set(xlim=(-1.7,5.6),ylim=(-.55,3.45));ax.axis('off')
fig.text(.06,.04,'教学重构 · 有限列表展示规律，一般结论由作差时最高次项抵消来证明。',fontsize=10,color='#64727a')
save(fig,'20_finite_differences')

x=np.linspace(-1,2,601)
p=x**3-x*x-x+1
correct=(x+1)*(x-1)**2
wrong=(x-1)*(x+1)**2
assert np.allclose(p,correct) and correct[200]==1 and wrong[200]==-1
fig,ax=plt.subplots(figsize=(10,5.5))
fig.subplots_adjust(left=.08,right=.96,top=.69,bottom=.18)
fig.text(.08,.92,'证明换了路，原稿没有自动过关',fontsize=22,weight='bold')
fig.text(.08,.83,'同一个结论可以有正确证明；这不替另一份错误推理作保。',fontsize=12)
ax.plot(x,p,lw=3,color='#237d8c',label='原式 = (x + 1)(x − 1)²')
ax.plot(x,wrong,lw=2.5,ls='--',color='#b95f45',label='误写成 (x − 1)(x + 1)²')
ax.axhline(0,color='#9ca6a4',lw=.8);ax.axvline(0,color='#9ca6a4',lw=.8)
ax.scatter([0,0],[1,-1],s=45,color=['#237d8c','#b95f45'],zorder=4)
ax.annotate('x = 0：原式为 1',xy=(0,1),xytext=(-.85,3.7),fontsize=12,color='#237d8c',arrowprops={'arrowstyle':'->','color':'#237d8c'})
ax.annotate('错误分解却为 −1',xy=(0,-1),xytext=(.35,-1.8),fontsize=12,color='#b95f45',arrowprops={'arrowstyle':'->','color':'#b95f45'})
ax.set(xlim=(-1.05,2.05),ylim=(-2.4,9.6),xlabel='x（考察 x ≥ −1）',xticks=[-1,0,1,2])
ax.legend(loc='upper left',frameon=False,fontsize=11,bbox_to_anchor=(.35,1.16))
for s in ['top','right']:ax.spines[s].set_visible(False)
fig.text(.08,.045,'依据 Bastounis–Circelli–Hansen，Example 2.1；本图验证代数关系，不代表重跑 Lean。',fontsize=10,color='#64727a')
save(fig,'20_proof_translation')
(Path(__file__).parent/'20_teaching_checks.json').write_text(json.dumps({'cubes':levels[0].tolist(),'successive_differences':[r.tolist() for r in levels[1:]],'coefficient_identity':'x^3-x^2-x+1 = (x+1)(x-1)^2','wrong_expansion':'(x-1)(x+1)^2 = x^3+x^2-x-1','values_at_zero':{'original':1,'correct':1,'wrong':-1},'lean_execution':False},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Created two PNG/SVG pairs and teaching checks.')
