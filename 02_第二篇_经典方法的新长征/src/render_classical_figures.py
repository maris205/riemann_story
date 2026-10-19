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
def fronts():
 f=base('同一条临界带，三种不同的问题','概念示意 · 横轴为实部；纵向仅表示高度，不按实际零点坐标绘制')
 labels=[('清空一片区域','无零区域'),('约束偏离者的数量','零点密度'),('保证中央的占比','在线比例')]
 for j,(title,sub) in enumerate(labels):
  a=ax(f,[.07+j*.315,.26,.255,.5]);clean(a);a.set_xlim(-.1,1.1);a.set_ylim(0,1.12)
  txt(a,.5,1.075,title,19);txt(a,.5,.98,sub,13,MUTED)
  a.fill_between([0,1],.12,.87,color='#EAECE4'); a.plot([0,0],[.12,.87],color=MUTED,lw=1);a.plot([1,1],[.12,.87],color=MUTED,lw=1);a.plot([.5,.5],[.12,.87],color=TEAL,lw=2)
  for x,t in [(0,'0'),(.5,'1/2'),(1,'1')]:txt(a,x,.065,t,14)
  if j==0:
   y=np.linspace(.12,.87,100);b=.69+.18*(1-np.exp(-3*(y-.12)))
   a.fill_betweenx(y,b,1,color=GOLD,alpha=.3);a.plot(b,y,color=GOLD,lw=2)
   txt(a,.86,.42,'无\n零',17,GOLD);txt(a,.3,.7,'边界随\n高度改变',14,MUTED)
  elif j==1:
   a.axvline(.69,ymin=.108,ymax=.777,color=GOLD,ls='--',lw=1.5)
   a.scatter([.77,.85],[.34,.7],s=100,facecolors='none',edgecolors=GOLD,lw=2)
   txt(a,.67,.01,r'$\sigma$',14,GOLD);txt(a,.28,.48,'统计右侧\n可能的例外',14,MUTED)
  else:
   a.scatter(np.full(7,.5),[.19,.28,.39,.48,.6,.71,.81],s=40,color=TEAL)
   a.scatter([.24,.76],[.55,.55],s=90,facecolors='none',edgecolors=GOLD,lw=2)
  txt(a,.5,-.14,['确定区域内一个也没有','数量上界，不把零点搬走','渐近比例为 1 仍不等于全部'][j],14)
 f.text(.075,.115,'○ 空心点只是假设性例外的符号，并非发现了离线零点。',fontsize=14,color=GOLD)
 f.text(.075,.064,'区域的宽度、例外的数量、中央的比例：不能换算成同一条“RH 进度条”。',fontsize=15,color=NAVY)
 save(f,P2,'three_zero_fronts')
def mobius():
 f=base('整数没有掷骰子','实际计算 · 每一步由 μ(n) 决定；累计得到 M(n)，1 ≤ n ≤ 2000')
 n=np.arange(1,2001);mu=np.ones(2001,dtype=int);prime=np.ones(2001,dtype=bool);prime[:2]=False
 for p in range(2,2001):
  if prime[p]:
   prime[p*p::p]=False;mu[p::p]*=-1;mu[p*p::p*p]=0
 M=np.cumsum(mu[1:]); np.savetxt(P2/'src'/'mobius_1_2000.csv',np.column_stack((n,mu[1:],M)),fmt='%d',delimiter=',',header='n,mu,M',comments=''); assert list(mu[1:11])==[1,-1,-1,0,-1,1,-1,0,0,1]; assert M[-1]==5
 a=ax(f,[.075,.23,.85,.57]);a.plot(n,np.sqrt(n),ls=(0,(5,4)),color=GOLD,lw=1.8);a.plot(n,-np.sqrt(n),ls=(0,(5,4)),color=GOLD,lw=1.8);a.step(n,M,where='post',color=TEAL,lw=1.65)
 a.axhline(0,color=NAVY,lw=.7,alpha=.35);a.set_xlim(0,2060);a.set_ylim(-52,52);a.set_xticks([0,500,1000,1500,2000]);a.set_yticks([-40,-20,0,20,40]);a.tick_params(colors=MUTED);a.spines[['top','right']].set_visible(False)
 for s in ['left','bottom']:a.spines[s].set_color('#BDC6C3')
 a.set_xlabel('整数 n',color=NAVY);a.set_ylabel('累计位置',color=NAVY)
 txt(a,1800,45,r'$+\sqrt{n}$',17,GOLD);txt(a,1800,-46,r'$-\sqrt{n}$',17,GOLD);txt(a,1200,20,r'$M(n)=\sum_{k\leq n}\mu(k)$',20,TEAL)
 f.text(.075,.105,'金色虚线只作尺度参照。把它当作永不越过的围栏，得到的是已被否定的 Mertens 猜想。',fontsize=14,color=NAVY)
 f.text(.075,.06,'这段有限轨迹既不能证明 RH，也不能说明莫比乌斯函数是独立随机序列。',fontsize=13,color=MUTED)
 save(f,P2,'mobius_walk_2000')

if __name__=='__main__': fronts(); mobius()
