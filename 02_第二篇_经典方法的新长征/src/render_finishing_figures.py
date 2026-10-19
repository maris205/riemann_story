import os
os.environ['MPLCONFIGDIR']='/tmp/finish-mpl'
os.environ['XDG_CACHE_HOME']='/tmp/finish-cache'
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties,fontManager
from matplotlib.patches import Rectangle,FancyArrowPatch
F='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc';fontManager.addfont(F)
plt.rcParams.update({'font.family':[FontProperties(fname=F).get_name(),'DejaVu Sans'],'font.size':14,'axes.unicode_minus':False,'mathtext.fontset':'dejavusans','svg.fonttype':'path'})
R=Path(__file__).resolve().parents[2];P=[R/x for x in ['01_第一篇_飞蛾扑火','02_第二篇_经典方法的新长征','03_第三篇_物理篇之混沌大陆']]
BG='#F7F3E9';N='#173346';T='#178A86';G='#B78734';M='#637782';L='#D9E6DF'
def base(title,sub):
 f=plt.figure(figsize=(16,8),facecolor=BG);f.text(.055,.92,title,fontsize=27,weight='bold',color=N);f.text(.057,.865,sub,fontsize=13,color=M);return f
def axis(f,rect):return f.add_axes(rect,facecolor=BG)
def off(a):a.axis('off');a.set_xlim(0,1);a.set_ylim(0,1)
def tx(a,x,y,s,size=16,c=N,ha='center'):a.text(x,y,s,fontsize=size,color=c,ha=ha,va='center')
def foot(f,s):f.text(.06,.065,s,fontsize=13,color=M)
def save(f,p,name):
 f.savefig(P[p]/'img'/f'{name}.png',dpi=160,facecolor=BG);f.savefig(P[p]/'img'/f'{name}.svg',facecolor=BG);plt.close(f)
def tidy(a):
 a.spines[['top','right']].set_visible(False);a.tick_params(colors=M)
 for s in ['left','bottom']:a.spines[s].set_color('#BDC6C3')
def parity():
 f=base('筛法的“奇偶”，数的是质因子','确切整数例子 · Ω(n) 重复计算质因子；λ(n) = (−1)^Ω(n)')
 a=axis(f,[.06,.22,.88,.58]);off(a)
 heads=['整数 n','本身奇偶','素因子分解','Ω(n)','λ(n)','μ(n)'];xs=[.07,.24,.47,.66,.79,.93]
 for x,h in zip(xs,heads):tx(a,x,.95,h,17)
 rows=[('5','奇数','5',1,-1,-1),('9','奇数','3 × 3',2,1,0),('6','偶数','2 × 3',2,1,1),('12','偶数','2 × 2 × 3',3,-1,0),('30','偶数','2 × 3 × 5',3,-1,-1)]
 for j,row in enumerate(rows):
  y=.78-j*.16;a.add_patch(Rectangle((0,y-.065),1,.13,color=L if row[4]==1 else '#EEE3CB',alpha=.7))
  for x,v in zip(xs,row):tx(a,x,y,str(v),18,T if row[4]==1 else N)
 foot(f,'素数与某些合数同取 λ = −1。符号相同不等于都是素数；这张表解释对象，不是奇偶障碍定理的证明。');save(f,0,'sieve_factor_parity')
def chars():
 f=base('给每个整数配上一个周期权重','两个实本原非主 Dirichlet 特征 · 展示系数，不是 ζ 函数的零点图')
 for j,(q,vals) in enumerate([(4,[0,1,0,-1]),(5,[0,1,-1,-1,1])]):
  a=axis(f,[.07,.56-j*.29,.86,.21]);off(a);tx(a,.05,.7,fr'$\chi_{{{q}}}(n)$',22)
  for n in range(1,16):
   x=.14+(n-1)*.057;v=vals[n%q];a.add_patch(Rectangle((x-.023,.38),.046,.47,color=T if v==1 else G if v==-1 else '#D8D8D0',alpha=.75));tx(a,x,.64,str(v),15);tx(a,x,.18,str(n),12,M)
 tx(a,.54,-.15,'整数 n：按模 q 的余数重复',14,M)
 f.text(.08,.17,r'$L(s,\chi_4)=1-3^{-s}+5^{-s}-7^{-s}+\cdots$',fontsize=20,color=N)
 f.text(.57,.17,r'$L(s,\chi_5)=1-2^{-s}-3^{-s}+4^{-s}+\cdots$',fontsize=19,color=N)
 foot(f,'上述级数在 Re(s) > 1 绝对收敛。χ5 是模5的二次特征；模数的倍数权重为0，不能遗漏。');save(f,0,'dirichlet_character_weights')
def winding():
 f=base('不逐个找根，也可以数出根','精确教学模型 f(z) = z² + 1 · 两条围道都逆时针，且不经过零点')
 for j,r in enumerate([.5,1.5]):
  th=np.linspace(0,2*np.pi,2001);z=r*np.exp(1j*th);w=z*z+1
  for k,data in enumerate([z,w]):
   a=axis(f,[.065+k*.46,.51-j*.31,.37,.25]);a.set_aspect('equal');a.plot(data.real,data.imag,color=T if j else G,lw=2)
   a.axhline(0,color=M,lw=.6);a.axvline(0,color=M,lw=.6);tidy(a)
   a.annotate('',xy=(data[70].real,data[70].imag),xytext=(data[30].real,data[30].imag),arrowprops={'arrowstyle':'->','color':N,'lw':2})
   if k==0:a.scatter([0,0],[1,-1],marker='x',s=70,color=N);a.set_xlim(-1.8,1.8);a.set_ylim(-1.8,1.8);a.set_title(f'z平面：半径 {r}，圈内 {0 if j==0 else 2} 个根',fontsize=14)
   else:a.scatter([0],[0],s=28,color=N);a.set_xlim(-1.5,3.5);a.set_ylim(-2.7,2.7);a.set_title(f'f(z)平面：绕原点 {0 if j==0 else 2} 圈',fontsize=14)
  winding=(np.unwrap(np.angle(w))[-1]-np.unwrap(np.angle(w))[0])/(2*np.pi);assert abs(winding-2*j)<1e-10
 f.text(.16,.125,'× 零点位于 ±i；没有极点。右侧大圆被完整走过两遍。',fontsize=15,color=N)
 foot(f,'辐角原理：像曲线绕原点的圈数 = 围道内零点数 − 极点数（计重数）。此图没有计算任何 ζ 零点。');save(f,1,'argument_principle_toy')
def jensen():
 f=base('每一行的尾部，仍不是整张表','Jensen 实根判据的量词示意 · 色块不表示论文给出的实际门槛')
 a=axis(f,[.08,.25,.57,.54]);a.set_xlim(-.5,16.5);a.set_ylim(5.5,-.5)
 for d in range(1,7):
  for n in range(17):a.add_patch(Rectangle((n-.45,d-1-.43),.9,.86,facecolor=T if n>=d*d else '#E5E0D5',edgecolor='none'))
 a.set_xticks([0,4,8,12,16]);a.set_yticks(range(6),range(1,7));a.set_xlabel('平移 n →');a.set_ylabel('次数 d →');tidy(a)
 b=axis(f,[.69,.28,.27,.48]);off(b);tx(b,.5,.85,'固定 d，再让 n 足够大',18);tx(b,.5,.64,r'$\forall d\ \exists N(d)\ \forall n\geq N(d)$',19,T);tx(b,.5,.40,'图中仅假设 N(d) = d²\n用来显示门槛可以随 d 增长',15,M);tx(b,.5,.12,'灰色：这一条渐近结论未覆盖\n不表示存在非实根',15,G)
 f.text(.08,.14,'RH 要求：对全部 d ≥ 1、n ≥ 0，整族 Jensen 多项式均只有实根。',fontsize=17,color=N)
 foot(f,'Griffin–Ono–Rolen–Zagier（2019）的固定次数、大平移定理不能直接交换量词，不能因此宣布 RH 已证。');save(f,1,'jensen_quantifier_grid')
def mobius():
 mu=np.ones(2001,dtype=int);prime=np.ones(2001,dtype=bool);prime[:2]=False
 for p in range(2,2001):
  if prime[p]:prime[p*p::p]=False;mu[p::p]*=-1;mu[p*p::p*p]=0
 assert list(mu[1:11])==[1,-1,-1,0,-1,1,-1,0,0,1]
 starts=[100,800,1500];h=30
 f=base('一样长的窗口，不会每次都打平','真实整数计算 · 三个事先指定的窗口 (x, x+30]；全部位于 n ≤ 2000')
 rows=[]
 for j,x in enumerate(starts):
  a=axis(f,[.075,.61-j*.205,.72,.14]);n=np.arange(x+1,x+h+1);vals=mu[n];a.bar(n,vals,width=.72,color=[T if v>0 else G for v in vals]);a.scatter(n[vals==0],np.zeros(sum(vals==0)),s=13,color=M);a.axhline(0,color=M,lw=.7);a.set_ylim(-1.35,1.35);a.set_yticks([-1,0,1]);a.set_xticks([x+1,x+10,x+20,x+30]);tidy(a)
  s=int(sum(vals));f.text(.825,.66-j*.205,f'Σ μ = {s:+d}',fontsize=22,color=N);f.text(.825,.615-j*.205,f'平均 = {s/30:+.3f}',fontsize=14,color=M)
  rows += [(int(k),int(mu[k]),x) for k in n]
 np.savetxt(P[1]/'src'/'mobius_windows.csv',rows,delimiter=',',fmt='%d',header='n,mu,window_start',comments='')
 foot(f,'有限窗口只是例子。Matomäki–Radziwiłł 的“几乎所有短区间”是渐近结论，并非每个固定短窗都零和。');save(f,1,'mobius_short_windows')
def conformal():
 f=base('换一个空间，也换一种提问','原创背景模型 · 共形映射与能量极小化；不复现 Connes 的算子或黎曼的历史手稿')
 a=axis(f,[.07,.27,.37,.49]);a.set_aspect('equal')
 for x in np.linspace(-3,3,13):
  z=x+1j*np.linspace(.03,5,300);w=(z-1j)/(z+1j);a.plot(w.real,w.imag,color=T,lw=.8)
 for y in [.05,.15,.3,.5,.8,1.2,2,3,5]:
  z=np.linspace(-15,15,800)+1j*y;w=(z-1j)/(z+1j);a.plot(w.real,w.imag,color=G,lw=.8)
 t=np.linspace(0,2*np.pi,400);a.plot(np.cos(t),np.sin(t),color=N,lw=1.4);a.axis('off');a.set_title('上半平面的网格 → 单位圆盘',fontsize=17,color=N);a.text(0,-1.2,r'$w=(z-i)/(z+i)$',ha='center',fontsize=20,color=N)
 a=axis(f,[.56,.31,.35,.41]);v=np.linspace(-1,1,250);a.plot(v,1+.5*np.pi**2*v*v,color=T,lw=2.5);a.scatter([0],[1],color=G,s=70);a.set_xlabel('扰动幅度 a');a.set_ylabel('Dirichlet 能量 E(a)');tidy(a);a.set_title('固定边界，比较能量',fontsize=17,color=N)
 f.text(.51,.21,r'$u_a(x,y)=x+a\sin(\pi x)\sin(\pi y)$',fontsize=19,color=N);f.text(.51,.15,r'$E(a)=\int_{[0,1]^2}|\nabla u_a|^2=1+\frac{\pi^2a^2}{2}$',fontsize=19,color=N)
 foot(f,'右图所有 u_a 的边界值相同；这族函数在 a=0 能量最低。极值思想提供观察方式，本图不导出 RH。');save(f,2,'conformal_extremum_background')
def cantor():
 f=base('缩小三倍，复制两份','康托尔集的维数与康托尔弦的复维数 · 两种 ζ 的角色必须区分')
 a=axis(f,[.07,.35,.46,.42]);off(a);segs=[(0,1)]
 for lev in range(5):
  y=.9-lev*.19
  for lo,hi in segs:a.plot([lo,hi],[y,y],lw=9,color=T,solid_capstyle='butt')
  segs=[s for lo,hi in segs for s in [(lo,lo+(hi-lo)/3),(hi-(hi-lo)/3,hi)]]
 tx(a,.5,-.09,r'$2(1/3)^D=1\quad\Rightarrow\quad D=\frac{\log 2}{\log 3}\approx0.63093$',21)
 a=axis(f,[.66,.33,.24,.45]);D=np.log(2)/np.log(3);ys=np.arange(-2,3)*2*np.pi/np.log(3);a.axvline(D,color=T,lw=2);a.scatter([D]*5,ys,color=G,s=50);a.axhline(0,color=M,lw=.7);a.set_xlim(.2,1);a.set_xticks([D],['D ≈ 0.631']);a.set_yticks(ys,['−4π/log3','−2π/log3','0','2π/log3','4π/log3']);a.set_xlabel('实部');a.set_title('几何 ζ 的极点',fontsize=17,color=N);tidy(a)
 f.text(.08,.17,r'$\zeta_{\mathcal{L}}(s)=\sum_{n\geq1}2^{n-1}3^{-ns}=\frac{1}{3^s-2}$',fontsize=22,color=N)
 foot(f,'级数在 Re(s)>D 收敛，右式给出亚纯延拓。其极点 D+2πik/log3 是几何复维数，绝不是黎曼 ζ 的非平凡零点。');save(f,2,'cantor_dimension_poles')
if __name__=='__main__':
 for fn in [winding,jensen,mobius]:fn();print(fn.__name__)
