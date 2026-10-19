import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/riemann-ai-mpl')
os.environ.setdefault('XDG_CACHE_HOME','/tmp/riemann-ai-cache')
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties,fontManager
from matplotlib.patches import FancyArrowPatch,Rectangle
FONT='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
fontManager.addfont(FONT)
plt.rcParams.update({'font.family':FontProperties(fname=FONT).get_name(),'font.size':15,'axes.unicode_minus':False,'mathtext.fontset':'dejavusans','svg.fonttype':'path'})
BG='#F7F3E9';NAVY='#173346';TEAL='#178A86';GOLD='#B78734';MUTED='#637782';LIGHT='#D9E6DF'
PART=Path(__file__).resolve().parents[1]; IMG=PART/'img'
def base(title,subtitle):
 f=plt.figure(figsize=(16,8),facecolor=BG)
 f.text(.055,.915,title,fontsize=28,color=NAVY,weight='bold')
 f.text(.057,.864,subtitle,fontsize=13,color=MUTED)
 return f
def panel(f,rect):
 a=f.add_axes(rect,facecolor=BG);a.set_xlim(0,1);a.set_ylim(0,1);a.axis('off');return a
def txt(a,x,y,s,size=16,c=NAVY,ha='center',**kw): a.text(x,y,s,fontsize=size,color=c,ha=ha,va='center',**kw)
def arr(a,p,q,c=GOLD,dashed=False): a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=17,lw=2,color=c,linestyle='--' if dashed else '-'))
def save(f,name):
 for ext in ['png','svg']: f.savefig(IMG/f'{name}.{ext}',dpi=180,facecolor=BG)
 plt.close(f)
def budget():
 f=base('两个零点名额，至多一个正方向','第16章 · 有限压缩的记账机制：允许离线配对存在，再用整体信息限制它们的总量')
 a=panel(f,[.065,.36,.39,.43]); b=panel(f,[.55,.36,.39,.43])
 for ax,head in [(a,'一个简单在线零点'),(b,'一对假设的离线零点')]:
  txt(ax,.5,.96,head,21);ax.plot([.5,.5],[.35,.77],color=MUTED,ls='--',lw=1.5)
  txt(ax,.5,.26,r'$\mathrm{Re}\,s=1/2$',14,MUTED)
 a.scatter([.5],[.56],s=180,color=TEAL,zorder=3);txt(a,.5,.09,'1 个零点名额',18)
 b.plot([.29,.71],[.56,.56],color=GOLD,lw=1.2,ls=':')
 b.scatter([.29,.71],[.56,.56],s=180,facecolors=BG,edgecolors=GOLD,lw=2.5,zorder=3)
 txt(b,.5,.09,'至少 2 个名额（按重数）',18)
 arr(a,(.7,.56),(.88,.56));txt(a,.9,.76,'正',16,TEAL);txt(a,.9,.56,'＋',29,TEAL);txt(a,.9,.36,'秩 ≤ 1',13)
 arr(b,(.76,.56),(.88,.56));txt(b,.92,.76,'压缩后',12,MUTED);txt(b,.92,.56,'＋',29,TEAL);txt(b,.92,.36,'至多 1 个',12)
 f.text(.08,.317,'正秩一形式的贡献；测试空间中可能退化。',fontsize=12,color=MUTED)
 f.text(.56,.317,'原始配对一正一负；压缩不会增加正惯性指标。',fontsize=12,color=MUTED)
 c=panel(f,[.065,.13,.87,.14]);c.add_patch(Rectangle((0,0),1,1,facecolor=LIGHT,edgecolor='none',alpha=.65))
 txt(c,.19,.66,'迹：净贡献',16);txt(c,.19,.28,'平方和：限制贡献过度集中',13)
 arr(c,(.38,.5),(.49,.5));txt(c,.73,.64,'结合块结构的计数不等式',16)
 txt(c,.73,.25,r'$N_{\rm simple,on}\ \geq\ (2-R-o(1))\,N$',20,TEAL)
 f.text(.07,.068,'N 按重数计数，R 来自测试窗的二阶矩。优化后渐近至少约67.25%既单又在线。',fontsize=13,color=NAVY)
 f.text(.07,.025,'这是机制示意，非实测零点或矩阵。其余部分未获此定理保证，不等于已发现离线零点。',fontsize=12,color=MUTED)
 save(f,'weil_pair_budget')
def regions():
 f=base('从随高度收窄，到固定宽度','第17章 · ζ 的非平凡零点位置：7/8 是横坐标，不是“已证明的百分比”')
 axs=[]
 for rect,title in [([.075,.25,.39,.52],'经典曲边：随 |t| 增大收窄'),([.565,.25,.36,.52],'2026 QRH：固定带')]:
  ax=f.add_axes(rect,facecolor=BG);axs.append(ax);ax.set_xlim(0,1);ax.set_ylim(-1.1,1.1)
  ax.spines[['top','right']].set_visible(False);ax.spines[['left','bottom']].set_color(MUTED)
  ax.set_yticks([]);ax.set_xticks([0,.125,.5,.875,1],['0','1/8','1/2','7/8','1']);ax.tick_params(axis='x',colors=NAVY,labelsize=13)
  ax.axvline(.5,color=TEAL,lw=2,ls='--');ax.axhline(0,color=MUTED,lw=.6,alpha=.4)
  ax.set_title(title,color=NAVY,fontsize=20,pad=17);ax.set_xlabel('实部 σ',color=NAVY,labelpad=8)
  ax.annotate('',xy=(.5,1.09),xytext=(.5,.91),arrowprops=dict(arrowstyle='->',color=TEAL,lw=2))
  ax.annotate('',xy=(.5,-1.09),xytext=(.5,-.91),arrowprops=dict(arrowstyle='->',color=TEAL,lw=2))
 t=np.linspace(-1.1,1.1,401);gap=.30/(1+4*np.abs(t))
 axs[0].fill_betweenx(t,0,gap,color=LIGHT);axs[0].fill_betweenx(t,1-gap,1,color=LIGHT)
 axs[0].plot(gap,t,color=GOLD,lw=2);axs[0].plot(1-gap,t,color=GOLD,lw=2)
 axs[0].text(.5,.38,'形状示意\n不代表显式常数',ha='center',color=MUTED,fontsize=14)
 axs[0].text(.01,1.15,'虚部 t（无数值刻度）',color=MUTED,fontsize=11)
 ax=axs[1];ax.axvspan(0,.125,color=LIGHT);ax.axvspan(.875,1,color=LIGHT)
 ax.axvline(.125,color=GOLD,lw=2,ls=':');ax.axvline(.875,color=GOLD,lw=2,ls=':')
 ax.text(.5,.47,'全部非平凡零点\n仍可处在这条闭带内',ha='center',color=NAVY,fontsize=15)
 ax.text(.06,.02,'无\n零',ha='center',color=TEAL,fontsize=14);ax.text(.94,.02,'无\n零',ha='center',color=TEAL,fontsize=14)
 ax.scatter([1],[0],s=80,facecolors=BG,edgecolors=GOLD,lw=2,zorder=4,clip_on=False)
 ax.annotate('s = 1 为极点',xy=(1,0),xytext=(.67,-.42),color=GOLD,fontsize=12,arrowprops=dict(arrowstyle='-',color=GOLD))
 ax.text(.5,-.79,'中央虚线：RH 的目标',ha='center',color=TEAL,fontsize=13)
 f.text(.08,.14,'右图：Re(s) > 7/8 无零（s = 1 的极点单独处理）；由对称性得 1/8 ≤ Re(ρ) ≤ 7/8。',fontsize=14,color=NAVY)
 f.text(.08,.084,'点线边界 1/8、7/8 仍属于允许的闭带；排除区不含边界。固定结论覆盖全部高度。',fontsize=13,color=NAVY)
 f.text(.08,.033,'左图仅示意高处收窄的形状，不绘实际最佳区域；不能据此比较低高度的强弱。未绘任何零点数据。',fontsize=12,color=MUTED)
 save(f,'curved_and_fixed_regions')
def audit():
 f=base('检查正确，还要检查是哪一个命题','第18章 · 同一个证明项通过检查，不能自动补上范围或量词上的缺口')
 a=panel(f,[.06,.24,.41,.56]);b=panel(f,[.55,.24,.39,.56])
 txt(a,.5,.96,'范围：有限高度 ≠ 无穷范围',20)
 a.plot([.12,.12],[.14,.77],color=NAVY,lw=1.8);arr(a,(.12,.70),(.12,.83),NAVY)
 a.add_patch(Rectangle((.12,.14),.27,.32,facecolor=LIGHT,edgecolor='none'))
 a.plot([.10,.44],[.46,.46],color=GOLD,ls='--',lw=2);txt(a,.07,.46,'T',15,GOLD)
 for y in [.19,.26,.34,.4]:a.scatter([.25],[y],s=40,color=TEAL)
 txt(a,.67,.30,'0 < Im(ρ) ≤ T\n有限验证的范围',17)
 txt(a,.67,.66,'Im(ρ) > T\n还没有被这次验证覆盖',15,GOLD)
 txt(a,.25,.06,'示意，不代表零点数据',11,MUTED)
 txt(b,.5,.96,'量词：界可以跟着范围长大',20)
 txt(b,.5,.79,r'$\forall H>0\ \exists C>0:\ H\leq C$',21,TEAL)
 txt(b,.5,.68,'成立：对每个 H，取 C = H',14)
 b.plot([.12,.88],[.18,.18],color=MUTED,lw=1);b.plot([.12,.12],[.18,.57],color=MUTED,lw=1)
 b.plot([.18,.34,.5,.66,.82],[.24,.30,.36,.42,.48],color=TEAL,lw=2,marker='o')
 b.plot([.12,.88],[.37,.37],color=GOLD,lw=1.7,ls='--');txt(b,.9,.37,'固定 C',11,GOLD,ha='left')
 txt(b,.5,.10,'再大的固定 C，也会被更大的 H 越过',13,GOLD)
 txt(b,.07,.56,'数值',10,MUTED);txt(b,.91,.18,'H',11,MUTED)
 txt(b,.5,.01,r'$\exists C>0\ \forall H>0:\ H\leq C$',21,GOLD)
 txt(b,.5,-.08,'不成立；顺序交换改变了命题',14)
 f.text(.075,.14,'读回顶层陈述：对象是不是原来的函数？区域是否完整？常数能否依赖高度或模数？',fontsize=14,color=NAVY)
 f.text(.075,.085,'内核检查给定陈述及其证明；数学审查还须确认，它表达的正是我们要证明的命题。',fontsize=13,color=NAVY)
 f.text(.075,.032,'左：有限验证的范围示意。右：H ≤ C 的初等反例，仅说明量词次序；不是对任何公开工程的缺陷指控。',fontsize=11.5,color=MUTED)
 save(f,'proof_scope_and_quantifiers')
if __name__=='__main__':
 budget();regions();audit()
 r=1/2+1/np.sqrt(2)/np.tan(1/np.sqrt(2))
 assert .6725 < (2-r) < .6726
 assert .125==1-.875
 assert all(H<=H for H in [1,2,100,10**9])
 print(json.dumps({'R':r,'2-R':2-r,'checks':'passed'},indent=2))
