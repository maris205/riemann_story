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
def cantor():
 f=base('剪下来的空隙，怎样唱出整数倍？','康托尔弦 · 左侧长度按比例绘制；右侧共用频率刻度，单位选为 f = k / ℓ')
 f.text(.075,.76,'几何：每深入一层，长度 ÷3，数量 ×2',fontsize=17,color=NAVY)
 f.text(.55,.76,'声音：每根弦都有整套泛音',fontsize=17,color=NAVY)
 remain=[(0.,1.)]
 for j in range(3):
  cuts=[];new=[]
  for l,r in remain:
   third=(r-l)/3;cuts.append((l+third,r-third));new.extend([(l,l+third),(r-third,r)])
  remain=new
  a=ax(f,[.075,.53-j*.15,.37,.12]);a.set_xlim(0,1);a.set_ylim(-.5,1);clean(a)
  a.plot([0,1],[.4,.4],color=PALE,lw=2)
  for l,r in cuts:a.plot([l,r],[.4,.4],color=TEAL,lw=7,solid_capstyle='butt')
  tx(a,.5,-.12,f'长度 1/{3**(j+1)}  ×  {2**j} 根',13)
  b=ax(f,[.55,.53-j*.15,.38,.12]);b.set_xlim(0,31);b.set_ylim(0,1);b.set_yticks([])
  for s in ['top','left','right']:b.spines[s].set_visible(False)
  b.spines['bottom'].set_color(PALE);b.tick_params(colors=MUTED,labelsize=10);b.set_xticks([0,3,9,18,27,30])
  freq=np.arange(3**(j+1),31,3**(j+1));b.vlines(freq,0,.6,color=TEAL,lw=2);b.scatter(freq,np.full(len(freq),.62),s=30,color=TEAL)
  for ff in freq:
   if j>0:tx(b,ff,.85,f'×{2**j}',11,GOLD)
 f.text(.075,.12,r'$\zeta_{\mathrm{spec}}(s)=\sum_{j,k}(k/\ell_j)^{-s}=\zeta(s)\sum_j\ell_j^s$',fontsize=23,color=NAVY)
 f.text(.075,.057,'先在绝对收敛区 Re(s)>1 相乘。图只画前三层、频率至30；重数计入声音清单，不是振幅。',fontsize=13,color=MUTED)
 save(f,P3,'cantor_string_harmonics')
def logistic():
 f=base('同一条规则，百万分之一的起点差','实际迭代 · x(n+1) = 4x(n)(1−x(n))，参数固定为 4；没有随机抽样')
 from decimal import Decimal,localcontext
 with localcontext() as ctx:
  ctx.prec=80
  values=[]
  for initial in ['0.2','0.200001']:
   x=Decimal(initial);seq=[x]
   for _ in range(20):x=4*x*(1-x);seq.append(x)
   values.append(seq)
  # Independent closed-form identity x_n = sin²(2^n arcsin sqrt(x_0)).
  import mpmath as mp
  mp.mp.dps=90
  for initial,seq in zip(['0.2','0.200001'],values):
   for n,x in enumerate(seq):assert abs(mp.mpf(str(x))-mp.sin(2**n*mp.asin(mp.sqrt(mp.mpf(initial))))**2)<mp.mpf('1e-65')
 y=np.array([[float(x) for x in seq] for seq in values]);n=np.arange(21)
 np.savetxt(P3/'src'/'logistic_20_steps.csv',np.column_stack([n,y.T,abs(y[0]-y[1])]),delimiter=',',header='n,x_initial_0.2,x_initial_0.200001,absolute_difference',comments='',fmt=['%d','%.17g','%.17g','%.17g'])
 a=ax(f,[.075,.31,.60,.45]);a.plot(n,y[0],'-o',color=TEAL,lw=2,ms=4,label='$x_0=0.2$');a.plot(n,y[1],'--o',color=GOLD,lw=2,ms=4,label='$x_0=0.200001$');a.set_xlim(0,20);a.set_ylim(0,1.06);a.set_xticks([0,5,10,15,20]);a.set_yticks([0,.5,1]);a.legend(loc='lower left',frameon=True,facecolor=BG,edgecolor=PALE,fontsize=12);a.set_xlabel('迭代步数 n',color=NAVY);a.set_ylabel('位置 x(n)',color=NAVY)
 for s in ['top','right']:a.spines[s].set_visible(False)
 for s in ['left','bottom']:a.spines[s].set_color(PALE)
 a.tick_params(colors=MUTED)
 b=ax(f,[.74,.31,.21,.45]);clean(b);b.set_xlim(0,1);b.set_ylim(0,1)
 tx(b,.5,.93,'第 20 步',19);tx(b,.5,.7,f'{y[0,-1]:.6f}',26,TEAL);tx(b,.5,.49,f'{y[1,-1]:.6f}',26,GOLD);tx(b,.5,.2,'相同规则\n不同初始值',15)
 f.text(.075,.15,'确定性混沌：微小初值差可被放大。随机模型：随机性来自另行指定的抽样规则。',fontsize=14,color=NAVY)
 f.text(.075,.08,'GMC 是随机测度理论；它与这里的迭代不是同一个对象。这张图没有证明素数服从混沌。',fontsize=13,color=MUTED)
 save(f,P3,'logistic_initial_sensitivity')

if __name__=='__main__':cantor();logistic()
