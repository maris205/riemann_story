"""Chapter14: author notebook data, faithful gap recomputation, verified USTC table.

The spectral figure redraws the notebook's SAVED, rounded residual array.
It does not rerun the million-step matrix calculation or reinterpret selected
ARPACK results as independent predictions. See the research audit for selection
and matrix-normalization details. USTC values were checked against Table I.
"""
from pathlib import Path
import json
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE=Path(__file__).resolve().parent
PART=HERE.parent
RAW=PART.parent/'资料/14_在动力学系统中寻找零点/原始代码/Wang_notebooks'
font_manager.fontManager.addfont('C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],
                     'font.size':11,'axes.unicode_minus':False,'svg.fonttype':'path'})
BG,INK,TEAL,GOLD,RED='#faf7ef','#253448','#137d89','#be8b38','#be584c'

def canvas(title,subtitle):
    fig,axes=plt.subplots(1,2,figsize=(14,6.6),facecolor=BG)
    fig.subplots_adjust(left=.075,right=.96,top=.73,bottom=.22,wspace=.27)
    fig.text(.055,.92,title,fontsize=25,color=INK)
    fig.text(.055,.83,subtitle,fontsize=11.5,color=INK)
    for ax in axes:
        ax.set_facecolor(BG);ax.spines[['top','right']].set_visible(False)
        ax.grid(alpha=.15)
    return fig,axes

def save(fig,name,footer):
    fig.text(.055,.075,footer,fontsize=9.8,color=INK,linespacing=1.7)
    for ext in ['png','svg']:
        fig.savefig(PART/'img'/f'{name}.{ext}',dpi=180,facecolor=fig.get_facecolor())
    plt.close(fig)

g=np.load(HERE/'14_wang_gap_data.npz')
fig,axes=canvas('隔山相望的两列节拍','同样出现离散的偶数间隔，却有不同的峰形与尺度；保留原 notebook 的五亿规模')
for ax,key,limit,col,title,peaks in zip(axes,['prime','chaos'],[100,60],[TEAL,GOLD],
        ['素数：相邻素数之差','固定参数映射：两次进入 x < 0 的步数间隔'],[[6,12,18],[2,4,6]]):
    c=g[key+'_counts'];prob=c/g[key+'_total'];xs=np.arange(len(c))
    mask=(xs<=limit)&(prob>0)
    ax.vlines(xs[mask],1e-6,prob[mask],color=col,lw=1.4)
    ax.scatter(xs[mask],prob[mask],s=12,color=col,zorder=3)
    ax.set(yscale='log',ylim=(1e-6,.9),xlim=(0,limit+1),xlabel='原始间隔（未缩放）',ylabel='出现概率',title=title)
    for k in peaks:ax.text(k,prob[k]*1.35,str(k),ha='center',fontsize=10,color=INK)
    mean=float(c@np.arange(len(c))/g[key+'_total'])
    ax.text(.97,.93,f'平均间隔 ≈ {mean:.2f}',transform=ax.transAxes,ha='right',color=INK)
save(fig,'14_wang_gap_spectrum','按 fig5-discrete_gap_spectrum.ipynb 的规则重新计算：整数上界 5×10⁸，映射迭代 5×10⁸ 次，u = 1.543689012692076。\n相似性限于本图的离散结构；这幅图没有使用随时间变化的参数，也不表明两种分布相同。')

saved=np.loadtxt(RAW/'saved_spectral_residuals.csv',delimiter=',',skiprows=1)
mp.mp.dps=25
true=np.array([float(mp.im(mp.zetazero(i))) for i in range(1,86)])
diff=saved[:,1];pred=true+diff;rel=100*diff/true
assert len(diff)==85 and abs(sum(abs(diff[1:6]))-1.7469707378)<1e-8
fig,axes=canvas('近处相逢，远处渐行渐远','非自治 Logistic 映射的有限矩阵谱：左看前 25 项的对应，右看全部 85 项的相对偏差')
ax=axes[0]
ax.plot(true[:25],true[:25],color=INK,lw=1,ls='--',label='完全一致的位置')
ax.axvspan(true[0]-2,true[5]+2,color=TEAL,alpha=.08)
ax.scatter(true[:6],pred[:6],s=38,color=TEAL,label='前 6 项：尺度／筛选参照',zorder=4)
ax.scatter(true[6:25],pred[6:25],s=30,color=GOLD,label='其余展示项',zorder=3)
ax.scatter(true[19],pred[19],marker='D',color=RED,s=42,zorder=5)
ax.annotate('第 20 项也参与筛选',xy=(true[19],pred[19]),xytext=(42,115),fontsize=9.5,color=RED,
            arrowprops={'arrowstyle':'->','color':RED})
ax.set(xlabel='真实零点高度',ylabel='换算后的模型谱值',xlim=(10,93),ylim=(10,125))
ax.legend(loc='lower right',fontsize=8.8,frameon=False)
ax=axes[1];ind=np.arange(1,86)
ax.axvspan(.5,6.5,color=TEAL,alpha=.08)
ax.axhline(0,color=INK,lw=.8)
ax.plot(ind,rel,color=GOLD,lw=1.7)
ax.scatter(ind[:6],rel[:6],s=22,color=TEAL,zorder=4)
ax.scatter(20,rel[19],marker='D',s=38,color=RED,zorder=4)
ax.set(xlabel='零点序号 n',ylabel='相对偏差（模型 − 真值）/ 真值，%',xlim=(0,87))
ax.text(.05,.93,'全部 85 项的相对偏差',transform=ax.transAxes,color=INK,fontsize=10)
save(fig,'14_wang_spectral_fit','重绘 notebook 已保存的 85 项残差；首个零点定尺度，前 6 项与第 20 项参与 20 次求谱结果的筛选。\n这组结果包含校准与结果筛选；用于展示有限谱对应及其偏差，不能视为独立预测或量子实验。')
np.savetxt(HERE/'14_wang_spectral_plot.csv',np.c_[ind,true,pred,diff,rel],delimiter=',',
           header='index,true_zero,model_value,signed_residual,relative_error_percent',comments='')

t=np.genfromtxt(RAW/'ustc_first20_verified.csv',delimiter=',',names=True)
fig,axes=canvas('离子交出的答卷','中科大 2021 年论文补充表：前 20 个零点的测量值，以及它们与理论位置之间的距离')
axes[0].plot(t['index'],t['exact_table'],lw=1,color=INK,ls='--',label='理论位置')
for om,col,mark,j in [(8,TEAL,'o',-.14),(12,GOLD,'s',0),(16,RED,'^',.14)]:
    for ax,vals in [(axes[0],t[f'omega{om}']),(axes[1],t[f'omega{om}']-t['exact_table'])]:
        ax.errorbar(t['index']+j,vals,yerr=t[f'err{om}'],fmt=mark,color=col,ms=4,
                    mfc=BG,capsize=2,lw=.85,label=f'Ω = {om}')
axes[0].set(xlabel='零点序号 n',ylabel='零点高度：理论值与实验测量值',xlim=(.3,20.7))
axes[0].legend(loc='upper left',fontsize=9,frameon=False)
axes[1].axhline(0,color=INK,lw=.8)
axes[1].set(xlabel='零点序号 n',ylabel='实验值 − 理论值（含原表误差条）',xlim=(.3,20.7))
axes[1].legend(loc='lower left',fontsize=9,frameon=False)
for ax in axes:ax.set_xticks([1,5,10,15,20])
save(fig,'14_ustc_measured_zeros','来源：He 等（2021）Supplementary Table I，CC BY 4.0；与 notebook 转录的 20 行逐项核对，保留三组共 60 个点。\n误差条按原表括号数字换算；Ω 沿用论文的驱动频率缩放约定。')

info={'spectral_source':'saved notebook output cell7; not rerun ARPACK',
      'spectral_first6_MAE':float(np.mean(abs(diff[:6]))),
      'spectral_7to25_MAE':float(np.mean(abs(diff[6:25]))),
      'spectral_26to85_MAE':float(np.mean(abs(diff[25:]))),
      'selected_n20_error':float(diff[19]),
      'ustc_rows_verified':20,'ustc_values_verified':80,'ustc_points_drawn':60,
      'gap_counts_source':'full-scale recomputation with 100000-step equality check'}
(HERE/'14_wang_examples_metadata.json').write_text(json.dumps(info,indent=2),encoding='utf8')
print(json.dumps(info))
