from render_physics_depth import *
from matplotlib.patches import Circle

def inverse():
 f=base('一段几何振荡，怎样在声音里消失？','分形弦的逆谱问题：乘积中的零点，可以抵消另一因子的极点')
 a=axis(f,[.07,.50,.87,.30],True)
 txt(a,.15,.90,'几何ζ函数',20,TEAL);txt(a,.50,.90,'黎曼ζ函数',20,GOLD);txt(a,.85,.90,'谱ζ函数',20,NAVY)
 txt(a,.15,.59,r'$\zeta_{\mathcal{L}}(s)$',28,TEAL);txt(a,.50,.59,r'$\zeta(s)$',28,GOLD);txt(a,.85,.59,r'$\zeta_{\nu}(s)$',28,NAVY)
 txt(a,.325,.59,'×',28,MUTED);txt(a,.675,.59,'＝',28,MUTED)
 txt(a,.15,.25,r'$\sim a/(s-s_0)$',21,TEAL);txt(a,.50,.25,r'$\sim b(s-s_0)$',21,GOLD);txt(a,.85,.25,r'$\sim ab$',23,NAVY)
 txt(a,.15,.03,'一个简单极点',14);txt(a,.50,.03,'恰在同处的简单零点',14);txt(a,.85,.03,'乘积在此不再有极点',14)
 b=axis(f,[.07,.22,.87,.20],True)
 b.add_patch(FancyBboxPatch((.01,.12),.97,.78,boxstyle='round,pad=.01',edgecolor=TEAL,facecolor=BG,lw=1.5))
 txt(b,.50,.72,r'$s_0=D+i\tau,\quad 0<D<1$',23,TEAL)
 txt(b,.50,.39,'极点携带的尺度振荡信息，可能在谱的对应项中被抵消。',17)
 f.text(.075,.145,'逆向定理问的是：对固定维数 D 的所有合格分形弦，稳定的谱第二项能否推出几何稳定？',fontsize=14,color=NAVY)
 f.text(.075,.09,'这个普遍命题等价于 Re(s)＝D 上没有ζ零点；不是检查一根康托尔弦就能证明RH。',fontsize=14,color=NAVY)
 f.text(.075,.035,'上方是可亚纯延拓处的局部简单零点／极点示例；频率采用归一化约定，实际定理另有渐近条件。',fontsize=12,color=MUTED)
 save(f,'11_inverse_spectral_cancellation')

def quantum():
 f=base('把十六项级数，变成探针能读出的相干信号','2026年核自旋方案的有限编码：四个工作比特提供16个基态，另一个比特负责探测')
 beta=.5;t=14.134725141734693;n=np.arange(1,17);w=n**(-beta);w=w/w.sum();z=(-1.)**(n+1)*w*np.exp(-1j*t*np.log(n));cum=np.r_[0,np.cumsum(z)]
 a=axis(f,[.075,.38,.26,.38]);a.bar(n,w,color=TEAL,width=.73);a.set_xticks([1,4,8,12,16]);a.set_xlabel('基态编号 n');a.set_ylabel('归一化权重');a.set_title('① 按幂次准备布居',color=NAVY,fontsize=17,pad=16)
 b=axis(f,[.405,.38,.26,.38]);b.axhline(0,color=LIGHT,lw=1);b.axvline(0,color=LIGHT,lw=1)
 for k in range(16):
  b.add_patch(FancyArrowPatch((cum[k].real,cum[k].imag),(cum[k+1].real,cum[k+1].imag),arrowstyle='-|>',mutation_scale=10,color=TEAL if k%2==0 else GOLD,lw=1.7))
 b.scatter([cum[-1].real],[cum[-1].imag],color=RED,s=45,zorder=6);b.set_aspect('equal',adjustable='datalim');b.set_xlabel('实部');b.set_ylabel('虚部');b.set_title('② 十六个复向量首尾相接',color=NAVY,fontsize=17,pad=16);b.margins(.2)
 c=axis(f,[.725,.40,.22,.34],True);c.set_aspect('equal',adjustable='box');txt(c,.5,1.03,'③ 抵消是什么？',17)
 for p,q,co in [((.25,.25),(.75,.25),TEAL),((.75,.25),(.75,.75),GOLD),((.75,.75),(.25,.75),TEAL),((.25,.75),(.25,.25),GOLD)]:arrow(c,p,q,co)
 txt(c,.5,.5,'和为0',17);txt(c,.5,.12,'四个等长箭头的玩具示例',12);txt(c,.5,-.01,'不是实际ζ零点数据',12,MUTED)
 f.text(.07,.265,r'$\mathcal{L}_{16}(\beta,t)=\sum_{n=1}^{16}(-1)^{n+1}w_n e^{-it\log n},\quad w_n=n^{-\beta}/Z_{16},\quad Z_{16}=\sum_{m=1}^{16}m^{-\beta}$',fontsize=20,color=TEAL)
 f.text(.07,.19,f'中图真实计算：β＝1/2，t≈14.134725；有限16项的 |L|≈{abs(cum[-1]):.4f}，并未精确归零。',fontsize=14,color=NAVY)
 f.text(.07,.125,'实验样品为305 K（约32℃）；β是所模拟模型的无量纲逆温度，不是样品温度。',fontsize=14,color=NAVY)
 f.text(.07,.065,'有限交替和可以近似零点响应；它没有给出独立产生所有ζ零点的完整Hilbert–Pólya算子。',fontsize=13,color=MUTED)
 save(f,'14_sixteen_state_phase_encoding')
 import json
 (ROOT/'quantum_validation.json').write_text(json.dumps({'beta':beta,'t':t,'N':16,'weights':w.tolist(),'sum_weights':float(w.sum()),'response_real':float(cum[-1].real),'response_imag':float(cum[-1].imag),'response_norm':float(abs(cum[-1]))},indent=2))
if __name__=='__main__': inverse();quantum()
