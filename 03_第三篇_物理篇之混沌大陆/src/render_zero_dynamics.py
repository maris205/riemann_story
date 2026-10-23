"""Chapter 14: source-data redraw and independently calculated explanatory figures.

NMR data and flattening convention: Wei et al. Riemann-data, MIT license,
commit a8b0b38202d6f330297212f8755c8df04242f9d6, original Fig4.py.
Original license retained in 资料/14_在动力学系统中寻找零点/原始代码/Wei_2026/LICENSE.
Other panels implement equations, not unpublished author code or experimental data.
"""
from pathlib import Path
import json
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.colors import LinearSegmentedColormap

HERE=Path(__file__).resolve().parent
PART=HERE.parent
ROOT=PART.parent
DATA=ROOT/'资料/14_在动力学系统中寻找零点/原始代码/Wei_2026/data'
font_manager.fontManager.addfont('C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':['Microsoft YaHei','DejaVu Sans'],'font.size':11,
                     'axes.unicode_minus':False,'svg.fonttype':'path'})
BG,INK,TEAL,GOLD,RED='#faf7ef','#253448','#137d89','#be8b38','#be584c'
mp.mp.dps=35
zeros=np.array([float(mp.im(mp.zetazero(i))) for i in range(1,6)])
stats={'zeros':zeros.tolist(),'author_commit':'a8b0b38202d6f330297212f8755c8df04242f9d6'}

def style(ax):
    ax.set_facecolor(BG);ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.14);ax.tick_params(colors=INK)

def canvas(title,sub,cols=2,ratios=None):
    fig,axs=plt.subplots(1,cols,figsize=(14,6),facecolor=BG,
                         gridspec_kw={'width_ratios':ratios or [1]*cols})
    fig.subplots_adjust(left=.075,right=.965,top=.75,bottom=.21,wspace=.25)
    fig.text(.055,.92,title,fontsize=25,color=INK)
    fig.text(.055,.83,sub,fontsize=12,color=INK)
    for ax in np.atleast_1d(axs):style(ax)
    return fig,np.atleast_1d(axs)

def save(fig,name,footer):
    fig.text(.055,.065,footer,fontsize=9.8,color=INK)
    for ext in ['png','svg']:fig.savefig(PART/'img'/f'{name}.{ext}',dpi=180,facecolor=fig.get_facecolor())
    plt.close(fig)

def eta_sum(ts,n,beta=.5):
    ns=np.arange(1,n+1,dtype=float)
    return np.exp(-np.outer(beta+1j*np.asarray(ts),np.log(ns)))@((-1.)**(ns+1))

# 1. Effective, idealized trapped-ion response. No fake experimental markers.
ts=np.linspace(12,23,1101)
g=np.array([-mp.fp.zeta(.5+1j*t)/(.5+1j*t) for t in ts])
false=[]
for i in range(len(ts)-1):
    if g[i].real*g[i+1].real<0:
        r=float(mp.findroot(lambda x:mp.re(-mp.zeta(.5+1j*x)/(.5+1j*x)),(ts[i],ts[i+1])))
        if min(abs(zeros-r))>.02:false.append(r)
false0=false[0]
fig,axs=canvas('不动，也是一种回答','离子内态的有效耦合随参数改变；投影归零，还须辨认是否为真正的 ζ 零点')
ax=axs[0]
ax.plot(ts,g.real,color=TEAL,lw=2,label='有效耦合所对应的实部')
ax.plot(ts,g.imag,color=GOLD,lw=1.6,ls='--',label='同一复函数的虚部')
ax.axhline(0,color=INK,lw=.7)
for z in zeros[:2]:ax.axvline(z,color=TEAL,lw=1,ls=':')
ax.axvline(false0,color=RED,lw=1,ls=':')
ax.annotate('只过了实部这一关',xy=(false0,0),xytext=(false0-1.7,-.085),
            arrowprops={'arrowstyle':'->','color':RED},color=RED,fontsize=10)
ax.set(xlabel='扫描参数 E',ylabel='g(E) = −ζ(½+iE) / (½+iE)',xlim=(12,23))
ax.legend(loc='upper left',fontsize=9,frameon=True,facecolor=BG,edgecolor='none')
ax=axs[1];tau=np.linspace(0,80,801)
for E,color,label in [(13.,GOLD,'偏离零点：E = 13'),(zeros[0],TEAL,'第一颗零点：E ≈ 14.1347')]:
    coupling=float(mp.re(-mp.zeta(.5+1j*E)/(.5+1j*E)))
    ax.plot(tau,np.sin(coupling*tau)**2,color=color,lw=2,label=label)
ax.set(xlabel='有效演化时间（任意单位）',ylabel='从初态转移到另一内态的概率',ylim=(-.045,1.08))
ax.legend(loc='upper right',fontsize=9,frameon=False)
save(fig,'14_ion_silence','按 He 等（2021）的有效模型独立计算。右图作统一比例缩放，仅解释冻结机制；不是原实验时间序列或测量数据。')
stats['extra_real_zero']=false0

# 2. 2024 first-Born reflection equation, independent implementation.
fig,axs=canvas('让光自己做一次加法','散射位置按 log n 安排，强弱按 n⁻½ 递减，正负号交替；反射波在某些频率处相消',ratios=[.9,1.35])
ax=axs[0];ns=np.arange(1,25);xs=np.log(ns);weights=(-1.)**(ns+1)/np.sqrt(ns)
for x,w in zip(xs,weights):
    col=TEAL if w>0 else RED
    ax.vlines(x,0,w,color=col,lw=2);ax.scatter(x,w,s=22,color=col)
ax.axhline(0,color=INK,lw=.8)
ax.set(xlabel='散射体位置 x / x₀',ylabel='相对散射强度（正负表示相位差）',ylim=(-.85,1.15))
ax.text(.8,.8,'只展示前 24 项',color=INK)
ax=axs[1];opt_t=np.linspace(12,35,1500);d0=.02
for n,color in [(32,GOLD),(512,TEAL)]:
    reflect=d0*d0/opt_t**2*abs(eta_sum(opt_t,n))**2
    ax.semilogy(opt_t,reflect,color=color,lw=1.8,label=f'{n} 个散射体')
eta=np.array([(1-2**(.5-1j*t))*mp.fp.zeta(.5+1j*t) for t in opt_t])
ax.semilogy(opt_t,d0*d0/opt_t**2*abs(eta)**2,color=RED,lw=1.2,ls='--',label='无穷求和参照')
for z in zeros:ax.axvline(z,color=INK,lw=.6,ls=':',alpha=.4)
ax.set(xlabel='无量纲扫描参数 2k₀x₀',ylabel='反射强度 R（第一阶 Born 近似）',xlim=(12,35),ylim=(1e-11,2e-5))
ax.legend(loc='upper right',fontsize=9,frameon=True,facecolor=BG,edgecolor='none')
save(fig,'14_light_scattering','依据 Yu、Piao、Park（2024）公式独立重算；x₀ = 1，d₀ = 0.02。竖向点线为 ζ 零点位置；未模拟多次散射，未冒充器件实测。')

# 3. Real processed experimental data with original uncertainty, no fitting.
fig,axs=canvas('五个自旋，听见五处低谷','2026 年核磁共振实验的公开源数据：实线为 16 态理论，空心点与误差条来自实验',ratios=[1.7,1])
e=np.load(DATA/'exp/tscan_beta05_exp.npz',allow_pickle=False)
theory=np.load(DATA/'theory/tscan_beta05_theory.npz',allow_pickle=False)
tx=theory['t_flat'];complex_theory=theory['curve_x_full'].ravel()+1j*theory['curve_y_full'].ravel()
ours=eta_sum(tx,16)/np.sum(np.arange(1,17,dtype=float)**-.5)
err=float(np.max(abs(ours-complex_theory)));assert err<2e-12
assert np.allclose(e['t_grid'].T.ravel(),e['t_flat'])
ax=axs[0]
ax.plot(tx,abs(complex_theory),color=TEAL,lw=2,label='16 态理论')
ax.errorbar(e['t_flat'],e['abs_mean'].T.ravel(),yerr=e['abs_std'].T.ravel(),fmt='o',ms=4,
            mfc=BG,mec=RED,ecolor=RED,capsize=2,elinewidth=.85,label='实验均值 ± 1 标准差')
for i,z in enumerate(zeros):
    ax.axvline(z,color=GOLD,lw=.8,ls=':');ax.text(z,.54 if i==0 else .61,str(i+1),color=GOLD,ha='center',fontsize=10)
ax.set(xlim=(11,35),ylim=(0,.66),xlabel='无量纲演化时间 t',ylabel='探针复相干信号的模 |L|')
ax.legend(loc='upper left',fontsize=9,frameon=True,facecolor=BG,edgecolor='none')
ax.text(30,.58,'β = 0.5',color=INK)
ax=axs[1]
eb=np.load(DATA/'exp/beta_scan_exp.npz',allow_pickle=False)
tb=np.load(DATA/'theory/beta_scan_theory.npz',allow_pickle=False)
# Preserve the repository's beta scan coordinates.
bx=tb['beta'] if 'beta' in tb.files else eb['beta']
assert len(bx)==len(tb['curve_x'])
ax.plot(bx,np.hypot(tb['curve_x'],tb['curve_y']),color=TEAL,lw=2)
ax.errorbar(eb['beta'],eb['abs_mean'],yerr=eb['abs_std'],fmt='o',ms=4,mfc=BG,mec=RED,ecolor=RED,capsize=2,elinewidth=.85)
ax.axvline(.5,color=GOLD,lw=1,ls=':')
ax.set(xlabel='模拟的无量纲逆温度 β',ylabel='探针信号的模 |L|',ylim=(0,.17))
ax.text(.1,.155,'固定 t ≈ 14.1347',color=INK,fontsize=11)
save(fig,'14_nmr_source_data','数据：Wei 等（2026）公开仓库，原 Fig4.py 的数组对应关系；全部 55 + 18 个测量点及其误差保留。谷底未人为置零。')
stats['nmr_theory_max_difference']=err
stats['nmr_measurement_points']=int(len(e['t_flat'])+len(eb['beta']))
stats['nmr_beta05_min_measured_modulus']=float(e['abs_mean'].min())

# 4. Newton field, following the 2014 paper's differential equation.
x=np.linspace(11.5,27,220);y=np.linspace(-.75,1.75,100)
XX,YY=np.meshgrid(x,y);zgrid=YY+1j*XX
zfun=np.vectorize(mp.fp.zeta,otypes=[complex])
vals=zfun(zgrid);h=1e-5
deriv=(zfun(zgrid+h)-zfun(zgrid-h))/(2*h)
flow=-vals/deriv
speed=np.abs(flow)
# Positive scalar rescaling preserves trajectories but not their time parameter.
flow=flow/np.maximum(speed,.025)
flow[np.abs(deriv)<1e-5]=np.nan
fig=plt.figure(figsize=(14,6),facecolor='#101f32');ax=fig.add_axes([.075,.21,.85,.54])
cmap=LinearSegmentedColormap.from_list('river',['#12253b','#175169','#2a8992','#b8d8cb'])
heat=np.log10(np.maximum(abs(vals),1e-4))
im=ax.pcolormesh(x,y,heat,cmap=cmap,shading='auto',vmin=-1.3,vmax=.8,rasterized=True)
ax.streamplot(x,y,flow.imag,flow.real,color='#e2e3ce',density=1.8,linewidth=.58,arrowsize=.7)
ax.axhline(.5,color=GOLD,ls='--',lw=1.2)
ax.scatter(zeros[:3],np.full(3,.5),s=50,c=GOLD,edgecolors='#fff7df',zorder=5)
for i,z in enumerate(zeros[:3]):ax.text(z,.66,f'{z:.4f}',color='#ffe1a0',ha='center',fontsize=10)
ax.set(xlabel='虚部 t',ylabel='实部 σ',xlim=(11.5,27),ylim=(-.75,1.75))
ax.tick_params(colors='#e3e5dd');ax.xaxis.label.set_color('#e3e5dd');ax.yaxis.label.set_color('#e3e5dd')
for spine in ax.spines.values():spine.set_visible(False)
fig.text(.055,.92,'零点，成了河流的归处',fontsize=25,color='#f2ecdc')
fig.text(.055,.83,'Newton 流：沿 −ζ/ζ′ 指定的方向前进，函数值沿路径衰减；金点为前三颗非平凡零点',fontsize=12,color='#c1d4db')
fig.text(.055,.065,'依据 Neuberger 等（2014）独立计算。流线仅表示方向，背景为 log₁₀|ζ|；这是一幅数值地形图，并非实际电磁场或全部零点的证明。',fontsize=9.8,color='#c1d4db')
cb=fig.colorbar(im,ax=ax,pad=.02,fraction=.022);cb.set_label('log₁₀|ζ|',color='#e3e5dd');cb.ax.tick_params(colors='#e3e5dd')
for ext in ['png','svg']:fig.savefig(PART/'img'/f'14_newton_flow.{ext}',dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
checks=[]
for z in [.3+14j,.7+21j,1.2+25j]:
    calc=(mp.fp.zeta(z+h)-mp.fp.zeta(z-h))/(2*h)
    exact=complex(mp.diff(mp.zeta,z));checks.append(abs(calc-exact))
assert max(checks)<1e-7,checks
stats['derivative_sample_max_error']=max(checks)
stats['ion_model']='ideal effective model only; rescaled time; not measured populations'
stats['optical_model']='first Born only; x0=1 d0=.02; N=32,512'
np.savez_compressed(HERE/'14_dynamics_data.npz',ion_t=ts,ion_g=g,optical_t=opt_t,eta=eta,
                    newton_x=x,newton_y=y,newton_zeta=vals,newton_derivative=deriv)
(HERE/'14_dynamics_metadata.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False))
