"""Chapter 12: original teaching figures, not a computation of Connes's operator.

Run from any directory. Requires numpy, matplotlib, mpmath; Windows YaHei.
Outputs three PNGs, source arrays and a JSON validation record.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mpmath as mp

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'img'
FONT = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family': FONT.get_name(), 'axes.unicode_minus': False,
                     'font.size': 13, 'text.color': '#e6edf6',
                     'axes.labelcolor': '#c9d7e8', 'xtick.color': '#a8bbd1',
                     'ytick.color': '#a8bbd1', 'axes.edgecolor': '#476078',
                     'axes.facecolor': '#101e31', 'figure.facecolor': '#101e31'})
GOLD, TEAL, RED = '#f1c873', '#60d5c5', '#ff8686'

def frame(title, subtitle):
    fig = plt.figure(figsize=(14, 8), dpi=180)
    fig.text(.065, .92, title, fontsize=27, weight='bold')
    fig.text(.065, .86, subtitle, fontsize=13, color='#a8bbd1')
    return fig

def save(fig, name):
    fig.savefig(OUT / name, facecolor=fig.get_facecolor())
    plt.close(fig)

mp.mp.dps = 30
zeros = np.array([float(mp.im(mp.zetazero(n))) for n in range(1, 7)])
fig = frame('零点，藏在光的缺席处', '同一组频率，可以画成亮线，也可以画成连续背景里的暗线。')
for idx, label in enumerate(['发射谱的直观比喻：出现的线', '吸收谱的直观比喻：缺席的线']):
    ax = fig.add_axes([.09, .57 - .29 * idx, .84, .17])
    ax.set_facecolor('#040910')
    if idx:
        grad = np.tile(np.linspace(0, 1, 1600), (40, 1))
        ax.imshow(grad, extent=[10, 40, 0, 1], aspect='auto', cmap='viridis', alpha=.9)
    for z in zeros:
        ax.axvline(z, color='#08101c' if idx else GOLD, lw=3)
    ax.set(xlim=(10, 40), ylim=(0, 1), yticks=[])
    ax.set_title(label, loc='left', fontsize=16, color='#e6edf6', pad=12)
    if idx: ax.set_xlabel('横坐标：前六个ζ零点的高度 γ（非光的波长）', labelpad=12)
fig.text(.065, .08, '示意图采用已知零点位置；线宽与颜色仅供说明，不是实验光谱，也不是独立算出的孔涅能谱。',
         fontsize=12, color='#a8bbd1')
save(fig, '12_absorption_spectrum.png')

T = np.full((3, 3), -1.0)
np.fill_diagonal(T, 2)
eigenvalues = np.linalg.eigvalsh(T)
roots = np.roots([1, 1, 1])
assert np.allclose(eigenvalues, [0, 3, 3])
assert np.allclose(T @ np.ones(3), 0)
assert np.allclose(abs(roots), 1)
v = np.array([1+2j, 3-1j, -.3+.7j])
assert np.allclose(np.vdot(v, T @ v), sum(abs(v[i]-v[j])**2 for i,j in [(0,1),(1,2),(2,0)]))
fig = frame('一张矩阵，把零点留在圆上', '教学例子：正半定 + 托普利茨结构 + 一维核，三项条件共同起作用。')
ax = fig.add_axes([.07, .38, .38, .35]); ax.axis('off')
ax.text(0, .96, 'T =', fontsize=22, color=GOLD, va='top')
for i in range(3):
    for j in range(3):
        ax.text(.26+j*.21, .84-i*.23, f'{T[i,j]:.0f}', fontsize=28, ha='center')
ax.plot([.13,.11,.11,.13],[.99,.99,.28,.28], color=TEAL, lw=2)
ax.plot([.78,.8,.8,.78],[.99,.99,.28,.28], color=TEAL, lw=2)
ax.set(xlim=(0,1),ylim=(0,1.05))
fig.text(.09,.31,'核向量 (1, 1, 1)  →  P(z) = 1 + z + z²',fontsize=17,color=GOLD)
fig.text(.09,.24,'特征值：0、3、3；所有二次型值均 ≥ 0',fontsize=13)
ax = fig.add_axes([.57,.25,.36,.49]); a=np.linspace(0,2*np.pi,500)
ax.plot(np.cos(a), np.sin(a), color=TEAL, lw=2)
ax.axhline(0,color='#476078',lw=1);ax.axvline(0,color='#476078',lw=1)
ax.scatter(roots.real,roots.imag,c=GOLD,s=100,zorder=5)
for r,dy in zip(roots,[.13,-.17]):
    ax.text(r.real+.14,r.imag+dy,'−½ '+('+' if r.imag>0 else '−')+' i√3/2',fontsize=14)
ax.set(xlim=(-1.35,1.35),ylim=(-1.35,1.35),xlabel='实部',ylabel='虚部',xticks=[-1,0,1],yticks=[-1,0,1])
ax.set_aspect('equal')
fig.text(.065,.08,'这是可手算的结构示例；不能把任意正矩阵，或这张三阶矩阵，直接当作黎曼猜想的证明。',fontsize=12,color='#a8bbd1')
save(fig,'12_toeplitz_circle.png')

def concentration(n, c=4.):
    x,w = np.polynomial.legendre.leggauss(n)
    K = c/np.pi*np.sinc(c*(x[:,None]-x[None,:])/np.pi)
    values,vectors = np.linalg.eigh(np.sqrt(w[:,None]*w[None,:])*K)
    f = vectors[:,-1]/np.sqrt(w)
    if f[n//2]<0: f=-f
    return x,w,f,float(values[-1])
x,w,f,lam = concentration(200)
check = concentration(120)[-1]
assert abs(check-lam)<1e-11
assert 0<lam<1 and abs(np.sum(w*f*f)-1)<1e-12
time = np.linspace(-1,1,1001)
wave = (4/np.pi*np.sinc(4*(time[:,None]-x[None,:])/np.pi))@(w*f)/lam
omega = np.linspace(-12,12,3001)
F = np.exp(-1j*omega[:,None]*x[None,:])@(w*f)
density = abs(F)**2/(2*np.pi)
# Independent frequency quadrature on the permitted band.
q,qw = np.polynomial.legendre.leggauss(180)
Fb = np.exp(-1j*(4*q[:,None])*x[None,:])@(w*f)
band_energy = float(np.sum(4*qw*abs(Fb)**2/(2*np.pi)))
assert abs(band_energy-lam)<1e-11
fig = frame('时间有限，余音未尽', '经典通信问题：只发两单位时间，怎样让最多的能量留在指定频带？')
left=fig.add_axes([.08,.27,.37,.46]);right=fig.add_axes([.57,.27,.36,.46])
left.axvspan(-1,1,color=TEAL,alpha=.08)
left.plot(time,wave,color=TEAL,lw=2.5)
left.plot([-1.55,-1,-1],[0,0,wave[0]],color=TEAL,lw=1.5)
left.plot([1,1,1.55],[wave[-1],0,0],color=TEAL,lw=1.5)
left.set(xlim=(-1.55,1.55),xlabel='时间 t',ylabel='波形 f(t)',title='时间窗以外，信号为零')
right.axvspan(-4,4,color=GOLD,alpha=.15)
right.plot(omega,density,color=GOLD,lw=2)
right.set(xlim=(-12,12),xlabel='角频率 ω',ylabel='能量密度',title=f'频带内保留约 {100*lam:.2f}% 的总能量')
for ax in (left,right): ax.grid(alpha=.1)
fig.text(.065,.14,'频带之外仍有尾巴。最优，是把泄漏压得尽可能小；不是同时把时间和频率锁死。',fontsize=14)
fig.text(.065,.075,'按 sinc 积分核求得的第一浓缩模态，带宽参数 c = 4。此图解释通信工具，不是黎曼零点实验。',fontsize=12,color='#a8bbd1')
save(fig,'12_prolate_signal.png')
np.savez_compressed(ROOT/'src/12_connes_data.npz',zeros=zeros,T=T,roots=roots,
                    quadrature_x=x,quadrature_w=w,f=f,time=time,wave=wave,omega=omega,density=density)
metadata={'description':'Original teaching calculations; no Connes/RH numerical proof',
          'zeta_zeros':zeros.tolist(),'matrix_eigenvalues':eigenvalues.tolist(),
          'concentration_c':4,'quadrature_nodes':200,'concentration_eigenvalue':lam,
          'comparison_120_nodes':check,'independent_band_energy':band_energy,
          'checks':'PSD, kernel, unit-circle roots, complex quadratic identity, normalization, quadrature convergence, band energy'}
(ROOT/'src/12_connes_metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(metadata,ensure_ascii=False,indent=2))
