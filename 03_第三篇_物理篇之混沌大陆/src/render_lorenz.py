"""Reproducible Lorenz phase portrait; numerical illustration, not prime data.

Run from any directory with Python, NumPy, Matplotlib. Classical parameters:
sigma=10, rho=28, beta=8/3. RK4, dt=0.002, initial state (1,1,1).
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'img'
FONT = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

def rhs(v):
    x, y, z = v
    return np.array([10*(y-x), x*(28-z)-y, x*y-(8/3)*z])

def integrate(dt, duration):
    a = np.empty((round(duration/dt)+1, 3))
    a[0] = (1, 1, 1)
    for i in range(len(a)-1):
        v = a[i]
        k1 = rhs(v)
        k2 = rhs(v + dt*k1/2)
        k3 = rhs(v + dt*k2/2)
        k4 = rhs(v + dt*k3)
        a[i+1] = v + dt*(k1+2*k2+2*k3+k4)/6
    return a

def main():
    dt = .002
    full = integrate(dt, 100)
    a = full[round(5/dt):]
    assert np.isfinite(a).all()
    # Early-time step-halving check only: chaotic long-time paths need not coincide.
    coarse = integrate(.002, 1)[-1]
    fine = integrate(.001, 1)[-1]
    err = float(np.linalg.norm(coarse-fine))
    assert err < 1e-4, err
    xy = a[:, [0, 2]]
    seg = np.stack([xy[:-1], xy[1:]], axis=1)
    cmap = LinearSegmentedColormap.from_list('ink_gold', ['#50b9c4','#9edccc','#edd6a0','#e99c61'])
    fig = plt.figure(figsize=(12, 8), facecolor='#101c2b')
    ax = fig.add_axes([.06,.13,.88,.67], facecolor='#101c2b')
    norm = Normalize(-19,19)
    for lw, alpha in [(2.8,.025),(.9,.075),(.34,.55)]:
        lc = LineCollection(seg, cmap=cmap, norm=norm, linewidths=lw, alpha=alpha)
        lc.set_array(a[:-1,0]); ax.add_collection(lc)
    ax.set(xlim=(-23,23),ylim=(0,49),aspect='equal'); ax.axis('off')
    fig.text(.08,.91,'混沌有形',fontproperties=FONT,fontsize=27,color='#f0e4ce')
    fig.text(.082,.855,'一条轨迹，两翼山河',fontproperties=FONT,fontsize=12,color='#96b2bc')
    fig.text(.92,.908,'LORENZ  /  1963',ha='right',fontsize=11,color='#a2b7bd')
    fig.text(.08,.09,'洛伦兹吸引子 · x–z 投影',fontproperties=FONT,fontsize=11,color='#d3d9d9')
    fig.text(.08,.05,'确定的方程，也能画出难以远望的未来。',fontproperties=FONT,fontsize=10,color='#8ea4b0')
    fig.text(.92,.054,'σ = 10   ρ = 28   β = 8/3',ha='right',fontsize=10,color='#a2b7bd')
    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT/'10_lorenz_butterfly.png',dpi=240,facecolor=fig.get_facecolor())
    plt.close(fig)
    np.savez_compressed(ROOT/'src/10_lorenz_trajectory.npz',time=np.arange(len(full))*dt,xyz=full)
    report={'model':'Lorenz 1963','sigma':10,'rho':28,'beta':8/3,'initial':[1,1,1],
            'integrator':'classical RK4','dt':dt,'duration':100,'discard_first':5,
            'projection':'x-z','color':'x coordinate, decorative encoding',
            'step_halving_difference_at_t1':err,'purpose':'finite numerical illustration; not prime data'}
    (ROOT/'src/10_lorenz_metadata.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report))

if __name__ == '__main__':
    main()
