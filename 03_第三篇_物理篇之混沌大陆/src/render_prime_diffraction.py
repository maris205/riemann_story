"""Prime structure factor, following Torquato et al. arXiv:1804.06279.
Finite numerical experiment; no conjecture assumed in computing these data.
"""
from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
M, L = 10**10+1, 120120
font = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

def main():
    limit = math.isqrt(M+L-1)
    small = np.ones(limit+1, dtype=bool); small[:2] = False
    for p in range(2, math.isqrt(limit)+1):
        if small[p]: small[p*p::p] = False
    base = np.flatnonzero(small)
    selected = np.ones(L, dtype=bool)
    for p in base:
        start = max(int(p)*int(p), ((M+int(p)-1)//int(p))*int(p))
        selected[start-M::int(p)] = False
    positions = np.flatnonzero(selected)
    primes = M+positions
    # Deterministic spot check against trial division, independent of segment slicing.
    for n in primes[np.linspace(0,len(primes)-1,101,dtype=int)]:
        assert all(int(n)%int(p) for p in base if int(p)*int(p)<=n)
    spectrum = np.abs(np.fft.rfft(selected.astype(float)))**2/len(primes)
    u = 2*np.fft.rfftfreq(L)  # k/pi; unit integer spacing
    checks=[]
    for m in [L//6,L//3,L//2]:
        direct=abs(np.exp(-2j*np.pi*m*positions/L).sum())**2/len(primes)
        assert np.isclose(direct,spectrum[m],rtol=1e-9,atol=1e-6)
        checks.append({'k_over_pi':float(u[m]),'S':float(spectrum[m])})
    assert np.isclose(spectrum[-1],len(primes)) # all primes in interval are odd
    bg,ink,teal,gold='#101c2b','#e9e4d8','#71c5ce','#efc583'
    fig=plt.figure(figsize=(14,9),facecolor=bg)
    fig.text(.08,.92,'素数的光谱',fontproperties=font,fontsize=28,color=ink)
    fig.text(.08,.865,'看似散乱的一列数，照出层层叠叠的秩序。',fontproperties=font,fontsize=12,color='#9cb5bf')
    fig.text(.92,.92,'PRIME DIFFRACTION',ha='right',color='#9cb5bf',fontsize=11)
    for rect,lo,hi,caption in [([.08,.46,.84,.32],.001,1.003,'全景'),([.08,.17,.84,.20],.25,.40,'局部放大 · 同一份数据')]:
        ax=fig.add_axes(rect,facecolor=bg)
        sel=(u>=lo)&(u<=hi)
        ax.plot(u[sel],1+spectrum[sel],color=teal,lw=.55,alpha=.85)
        bright=sel&(spectrum>30)
        ax.vlines(u[bright],1,1+spectrum[bright],color=gold,lw=.9,alpha=.9)
        ax.set_yscale('log'); ax.set_xlim(lo,hi);ax.set_ylim(1,len(primes)*1.8 if hi>1 else 2200)
        ax.set_yticks([1,10,100,1000]);ax.set_yticklabels(['1','10','100','1000'])
        ax.tick_params(colors='#9cb5bf',labelsize=10,length=3)
        for side in ['top','right']:ax.spines[side].set_visible(False)
        for side in ['bottom','left']:ax.spines[side].set_color('#49606d')
        ax.grid(axis='y',color='#526a77',alpha=.17)
        ax.set_ylabel('1 + S(k)',color='#9cb5bf',fontsize=11)
        ax.text(.015,.94,caption,transform=ax.transAxes,fontproperties=font,color=ink,fontsize=11,va='top')
        if hi>1:
            ax.set_xticks([0,1/3,2/3,1]);ax.set_xticklabels(['0','1/3','2/3','1'])
            ax.axvspan(.25,.40,color=gold,alpha=.06)
        else:ax.set_xlabel('k / π',color='#9cb5bf',fontsize=11,labelpad=8)
    fig.text(.08,.075,f'真实素数 {len(primes):,} 个  ·  区间 [{M:,}, {M+L:,})',fontproperties=font,fontsize=10,color=ink)
    fig.text(.08,.038,'纵轴采用对数刻度；浅金区在下图放大。有限数值实验，展示多尺度结构。',fontproperties=font,fontsize=10,color='#9cb5bf')
    fig.savefig(ROOT/'img/10_prime_diffraction.png',dpi=220,facecolor=bg)
    plt.close(fig)
    np.savez_compressed(ROOT/'src/10_prime_diffraction_data.npz',primes=primes,k_over_pi=u,S=spectrum)
    meta={'M':M,'L':L,'prime_count':len(primes),'interval':'[M,M+L)',
          'formula':'S(k)=abs(sum_p exp(-i*k*(p-M)))**2/N',
          'grid':'k=2*pi*j/L, j=0,...,L/2','plot':'1+S on logarithmic y axis',
          'zoom':[.25,.40],'direct_sum_checks':checks,
          'reference':'https://arxiv.org/abs/1804.06279v2','status':'finite numerical experiment, not proof of chaos or RH'}
    (ROOT/'src/10_prime_diffraction_metadata.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    print(json.dumps(meta))

if __name__=='__main__':main()
