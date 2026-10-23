"""Chapter 11: exact prime spiral, continued-fraction cylinders, valuation turns.

Run from any working directory. Requires numpy, matplotlib and a CJK font.
All figures are finite calculations; no fractal dimension is fitted to pixels.
Sources and interpretation: ../../资料/11_素数与分形/04_图片与视频素材.md
"""
from pathlib import Path
import itertools
import json
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / 'img'
OUT.mkdir(exist_ok=True)
FONT = FontProperties(fname='C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family': FONT.get_name(), 'axes.unicode_minus': False,
                     'savefig.facecolor': '#101c2b', 'figure.facecolor': '#101c2b',
                     'axes.facecolor': '#101c2b', 'text.color': '#eee7d8',
                     'font.size': 12, 'axes.labelcolor': '#eee7d8',
                     'xtick.color': '#9faebb', 'ytick.color': '#9faebb'})
BG, GOLD, TEAL, WHITE, RED = '#101c2b', '#efc583', '#71c5ce', '#eee7d8', '#e68b86'


def sieve(n):
    a = np.ones(n + 1, dtype=bool)
    a[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if a[p]:
            a[p*p::p] = False
    return a


def spiral(side):
    """Coordinate at index n-1 is the cell labelled n; starts right then up."""
    assert side % 2 == 1
    pts = [(0, 0)]
    x = y = 0
    length = 1
    directions = itertools.cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    while len(pts) < side * side:
        for _ in range(2):
            dx, dy = next(directions)
            for _ in range(length):
                x, y = x + dx, y + dy
                pts.append((x, y))
                if len(pts) == side * side:
                    return np.array(pts, dtype=np.int32)
        length += 1


def save(fig, name):
    fig.savefig(OUT / (name + '.png'), dpi=180)
    plt.close(fig)


def clean(ax):
    ax.set_aspect('equal')
    ax.set_axis_off()


def hero(coords, primes):
    fig = plt.figure(figsize=(13, 14))
    ax = fig.add_axes([.035, .075, .93, .82])
    p = coords[primes[1:]]
    ax.scatter(p[:, 0], p[:, 1], s=1.05, color=GOLD, marker='s', linewidths=0)
    ax.set_xlim(-402, 402); ax.set_ylim(-402, 402); clean(ax)
    fig.text(.065, .958, '素数，落在方寸星河', fontsize=25, weight='bold')
    fig.text(.065, .932, '乌拉姆螺旋  ·  从中心的 1 开始，逆时针写到 641,601', color=TEAL, fontsize=13)
    fig.text(.065, .039, f'801 × 801 格  /  {len(p):,} 颗素数  /  金色为素数，暗处为其余整数', fontsize=12)
    fig.text(.065, .019, '按整数精确筛选；没有随机点，也没有为图案补线。', color='#9faebb', fontsize=11)
    save(fig, '11_ulam_starfield')


def diagonal(primes):
    fig = plt.figure(figsize=(16, 8.6))
    ax = fig.add_axes([.045, .19, .40, .66])
    coords = spiral(9)
    for n, (x, y) in enumerate(coords, 1):
        if primes[n]:
            ax.add_patch(plt.Circle((x, y), .40, facecolor=GOLD, alpha=.9))
        ax.text(x, y, str(n), ha='center', va='center', fontsize=14,
                color=BG if primes[n] else '#80909f', weight='bold' if primes[n] else 'normal')
    for r in range(1, 5):
        ax.add_patch(plt.Circle((r, -r), .43, fill=False, edgecolor=RED, lw=1.6))
    for v in np.arange(-4.5, 5, 1):
        ax.axhline(v, color='#263545', lw=.5); ax.axvline(v, color='#263545', lw=.5)
    ax.set_xlim(-4.6, 4.6); ax.set_ylim(-4.6, 4.6); clean(ax)
    ax.set_title('中心写 1：右下角一路都是平方数', fontsize=15, pad=18)
    ax = fig.add_axes([.54, .19, .40, .66])
    coords = spiral(45)
    values = np.arange(1, 45*45+1) + 40
    pts = coords[primes[values]]
    ax.scatter(pts[:, 0], pts[:, 1], s=14, color=GOLD, alpha=.65, linewidths=0)
    r = np.arange(-19, 21)
    ax.plot(r, r, color=TEAL, lw=1, alpha=.6)
    ax.scatter(r, r, s=24, color=TEAL, linewidths=0)
    ax.scatter([-20, 21], [-20, 21], s=75, facecolors='none', edgecolors=RED, linewidths=1.6)
    ax.annotate('1681 = 41²', (-20, -20), xytext=(-21, -26), color=RED, fontsize=11)
    ax.annotate('1763 = 41 × 43', (21, 21), xytext=(3, 25), color=RED, fontsize=11)
    ax.scatter([0], [0], s=65, facecolors='none', edgecolors=WHITE, linewidths=1)
    ax.annotate('41', (0, 0), xytext=(4, -3), color=WHITE, fontsize=12)
    ax.set_xlim(-23, 23); ax.set_ylim(-28, 28); clean(ax)
    ax.set_title('中心改成 41：一线串起 40 颗素数', fontsize=15, pad=18)
    fig.text(.055, .935, '同一支笔，两种命运', fontsize=25, weight='bold')
    fig.text(.055, .105, '左：9、25、49、81，都是奇数的平方。', fontsize=13)
    fig.text(.055, .065, '右：青色 40 点对应欧拉多项式 n² + n + 41（n = 0…39）；红圈处，连胜终止。', fontsize=13)
    fig.text(.055, .025, '右图改了起始数；不是左图的放大。两图均由整数逐一计算。', fontsize=11, color='#9faebb')
    save(fig, '11_ulam_diagonals')


def cylinder(word):
    """Exact Möbius matrix product gives endpoints of phi_word([0,1])."""
    a, b, c, d = 1, 0, 0, 1
    for p in word:
        a, b, c, d = b, a + b*p, d, c + d*p
    return sorted((b/d, (a+b)/(c+d)))


def continued_fraction():
    fig = plt.figure(figsize=(15, 8))
    fig.text(.06, .93, '把素数藏进一层又一层分母', fontsize=25, weight='bold')
    fig.text(.06, .878, '素数连分数：每深入一层，再从 2、3、5、7、11……里选一次', color=TEAL, fontsize=14)
    alphabet = np.flatnonzero(sieve(37)).tolist()
    prefixes = [(), (2,), (2, 3)]
    labels = ['第一位：选素数', '固定第一位为 2，放大', '固定前两位为 2、3，再放大']
    for row, prefix in enumerate(prefixes):
        ax = fig.add_axes([.09, .64 - row*.23, .85, .115])
        bounds = [0, .52] if not prefix else cylinder(prefix)
        for p in alphabet:
            lo, hi = cylinder(prefix + (p,))
            color = TEAL if p == (2 if row == 0 else 3 if row == 1 else 5) else GOLD
            ax.add_patch(Rectangle((lo, .22), hi-lo, .35, facecolor=color, edgecolor='none'))
            if p in [2, 3, 5, 7]:
                ax.text((lo+hi)/2, .71, str(p), ha='center', fontsize=12, color=color)
        span = bounds[1]-bounds[0]
        ax.set_xlim(bounds[0]-.025*span, bounds[1]+.025*span)
        ax.set_ylim(0, 1); ax.set_yticks([])
        ax.spines[['left', 'right', 'top']].set_visible(False)
        ax.spines['bottom'].set_color('#4b5b69')
        ax.set_title(labels[row], loc='left', fontsize=13, pad=10)
        ticks = np.linspace(bounds[0], bounds[1], 5)
        ax.set_xticks(ticks, [f'{x:.4f}' if row == 2 else f'{x:.3f}' for x in ticks], fontsize=10)
    fig.text(.06, .067, '每行只显示前 12 个素数对应的区间；真实集合允许全部素数，并延伸到无限层。', fontsize=12)
    fig.text(.06, .031, '区间按 x → 1/(p + x) 的复合映射精确计算；三行横轴尺度不同。', color='#9faebb', fontsize=11)
    save(fig, '11_prime_continued_fraction')


def valuations(n):
    return np.array([(k & -k).bit_length()-1 for k in range(1, n+1)], dtype=np.int16)


def dragon():
    steps = 65536
    vals = valuations(steps)
    # First edge 0->1 is east; at vertex n turn left 90*v2(n) before the next edge.
    turns = np.concatenate(([0], np.cumsum(vals[:-1]))) % 4
    unit = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]], dtype=np.int32)
    path = np.vstack(([0, 0], np.cumsum(unit[turns], axis=0)))
    assert vals[:8].tolist() == [0, 1, 0, 2, 0, 1, 0, 3]
    assert np.all(vals[1::2] == vals[:steps//2] + 1)
    assert np.all(vals[0::2] == 0)
    assert np.all(np.abs(np.diff(path, axis=0)).sum(axis=1) == 1)
    cmap = LinearSegmentedColormap.from_list('prime_ink', [TEAL, '#79aeb7', GOLD])
    fig = plt.figure(figsize=(16, 8.7))
    fig.text(.055, .937, '一枚素数，折出一条龙', fontsize=25, weight='bold')
    fig.text(.055, .88, '走到整数 n，数它能连续除以 2 几次，就向左转几个直角。', color=TEAL, fontsize=14)
    for i, count in enumerate([256, 4096, 65536]):
        ax = fig.add_axes([.035+i*.325, .24, .31, .55])
        p = path[:count+1].astype(float)
        segments = np.stack([p[:-1], p[1:]], axis=1)
        lc = LineCollection(segments, cmap=cmap, linewidths=[1.2, .65, .35][i])
        lc.set_array(np.linspace(0, 1, count))
        ax.add_collection(lc); ax.autoscale(); ax.margins(.04); clean(ax)
        ax.set_title(f'{count:,} 步', fontsize=16, pad=14)
    fig.text(.055, .15, '转弯次数：0，1，0，2，0，1，0，3，0，1，0，2，0，1，0，4……', fontsize=14)
    fig.text(.055, .10, '偶数位置重复原序列再加 1；奇数位置全部为 0。自相似写在除法里。', fontsize=13)
    fig.text(.055, .045, '依 Tillman（2025 预印本）第 4 节重绘。各幅独立缩放；色彩表示行进顺序。', fontsize=11, color='#9faebb')
    fig.text(.055, .021, '这里画的是因子 2 的重数所编码的有限折线，不是素数位置的分布。', fontsize=11, color='#9faebb')
    save(fig, '11_prime_factor_dragon')
    return vals, path


if __name__ == '__main__':
    primes = sieve(801**2)
    coords = spiral(801)
    assert primes[:101].sum() == 25
    assert coords[:9].tolist() == [[0,0],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
    assert np.unique(coords, axis=0).shape == coords.shape
    for r in range(1, 401):
        assert coords[(2*r+1)**2 - 1].tolist() == [r, -r]
        assert not primes[(2*r+1)**2]
    euler = np.array([n*n+n+41 for n in range(42)])
    assert primes[euler[:40]].all() and not primes[euler[40:]].any()
    lookup = {tuple(xy): n+41 for n, xy in enumerate(spiral(45))}
    highlighted = sorted(lookup[(r,r)] for r in range(-19,21))
    assert highlighted == sorted(euler[:40].tolist())
    assert cylinder((2,)) == [1/3, 1/2]
    assert cylinder((2,3)) == [3/7, 4/9]
    for prefix in [(), (2,), (2,3), (7,5,3)]:
        parent = cylinder(prefix)
        for p in [2,3,5,7,11,13,17,19,23,29,31,37]:
            lo, hi = cylinder(prefix+(p,))
            assert parent[0] <= lo < hi <= parent[1]
    hero(coords, primes)
    diagonal(primes)
    continued_fraction()
    vals, path = dragon()
    np.savez_compressed(HERE/'11_prime_fractals_data.npz', spiral_coordinates=coords,
                        prime_mask=primes, euler_values=euler, v2=vals, dragon_path=path)
    meta = {'date':'2026-10-22', 'spiral_side':801, 'integer_max':801**2,
            'prime_count':int(primes.sum()), 'dragon_steps':len(vals),
            'dragon_rule':'step 0->1 east, turn left by 90*v2(n) at vertex n',
            'checks':'known prime count; first spiral cells; unique cells; all odd-square corners; Euler 40 primes and next 2 composites; shifted diagonal identity; CF endpoints/nesting; valuation recursion; unit steps',
            'limitations':'Finite drawings only. CF figure truncates alphabet to first 12 primes. No numerical dimension claim. Dragon encodes factor multiplicity, not prime positions.'}
    (HERE/'11_prime_fractals_metadata.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(meta, ensure_ascii=False, indent=2))
