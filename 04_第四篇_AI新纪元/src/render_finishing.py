from figure_style import *
from matplotlib.patches import Circle

def foot(f,t,s):f.text(.07,.12,t,fontsize=14,color=NAVY);f.text(.07,.052,s,fontsize=12,color=MUTED)
def rank():
 f=base('迹与平方和：贡献有多集中？','第16章 · 一个可手算的正半定矩阵例子；它解释基本秩界，不替代零点块的惯性论证')
 a=f.add_axes([.09,.3,.36,.44],facecolor=BG);vals=[4,1,1,0];a.bar(range(4),vals,color=[TEAL,TEAL,TEAL,LIGHT],width=.55);a.set_ylim(0,4.8);a.set_xticks(range(4),[r'$\lambda_1$',r'$\lambda_2$',r'$\lambda_3$',r'$\lambda_4$']);a.set_yticks([0,1,2,3,4]);a.spines[['top','right']].set_visible(False);a.set_ylabel('特征值',color=NAVY);a.set_title('A = diag(4, 1, 1, 0)',color=NAVY,fontsize=21)
 b=panel(f,[.52,.27,.41,.5]);txt(b,.5,.9,'两本账簿',22);txt(b,.5,.7,r'$\operatorname{tr}A=4+1+1=6$',23);txt(b,.5,.52,r'$\operatorname{tr}(A^2)=16+1+1=18$',23)
 txt(b,.5,.28,r'$\frac{(\operatorname{tr}A)^2}{\operatorname{tr}(A^2)}=2\ \leq\ \operatorname{rank}A=3$',24,TEAL)
 txt(b,.5,.06,'保底至少 2 个方向；实际有 3 个',17)
 foot(f,'Cauchy–Schwarz：对 r 个非零特征值，(Σλ)² ≤ r Σλ²。贡献越集中，保底值越小。','例子精确可算。第16章的新比例还要用在线／离线块结构；普通秩界本身不给出67.25%。')
 save(f,'trace_square_rank_example')
def counts():
 f=base('六个名额，三个位置，一个单零点','第16章 · 重数、不同零点、简单在线零点：分母相同，分子不同')
 a=panel(f,[.065,.41,.87,.34]);a.plot([.1,.9],[.43,.43],color=MUTED,lw=1.5)
 for x,m in [(.2,1),(.5,2),(.8,3)]:
  a.scatter([x],[.43],s=90,color=TEAL)
  for k in range(m):a.add_patch(Circle((x-.035*(m-1)/2+.035*k,.68),.012,facecolor=GOLD,edgecolor='none'))
  txt(a,x,.92,f'重数 {m}',19);txt(a,x,.19,'一个不同位置',14)
 txt(a,.5,-.02,'教学例：三个位置都假设在线；点的位置不是实际零点数据',13,MUTED)
 b=panel(f,[.06,.20,.88,.15]);
 for x,n,l in [(.16,'6','按重数总数 N'),(.5,'3','不同零点数'),(.84,'1','简单在线数')]:txt(b,x,.78,n,32,TEAL);txt(b,x,.28,l,16)
 foot(f,'同一证明框架分别给出：简单在线比例 ≥ 2−R；不同位置比例 ≥ (3−R)/2（渐近）。','优化窗对应约67.25%与83.625%。第二个界不是仅由第一个界推出；重零点不必只有二重。')
 save(f,'multiplicity_counting_units')
def symmetry():
 f=base('假设一个离线零点，对称性带来什么？','第17章 · ζ 的非平凡零点对称；四个空心点仅为假设位置，不是已发现的零点')
 a=f.add_axes([.14,.25,.72,.53],facecolor=BG);a.set_xlim(0,1);a.set_ylim(-1,1);a.axvline(.5,color=TEAL,lw=2,ls='--');a.axhline(0,color=MUTED,lw=1);a.spines[['top','right','left']].set_visible(False);a.set_yticks([]);a.set_xticks([0,.3,.5,.7,1],['0','1−σ','1/2','σ','1']);a.tick_params(labelsize=16)
 pts=[(.7,.6,r'$\rho=\sigma+i\gamma$'),(.3,.6,r'$1-\bar\rho$'),(.7,-.6,r'$\bar\rho$'),(.3,-.6,r'$1-\rho$')]
 for x,y,l in pts:a.scatter([x],[y],s=150,facecolors=BG,edgecolors=GOLD,lw=2.5);a.text(x,y+(.15 if y>0 else -.23),l,ha='center',fontsize=24,color=NAVY)
 for p,q in [((.32,.6),(.68,.6)),((.7,-.53),(.7,.53)),((.3,-.53),(.3,.53)),((.32,-.6),(.68,-.6))]:a.annotate('',xy=p,xytext=q,arrowprops=dict(arrowstyle='<->',color=MUTED,lw=1.5))
 a.text(.5,.12,'关于临界线反射',ha='center',color=TEAL,fontsize=15)
 foot(f,'上方镜像对是 ρ 与 1−共轭ρ；再取复共轭，得到下半平面的对应点。','图取σ=0.7、γ=0.6仅作布局。关于1/2的对称性让右侧无零结论传到左侧；并不自行排除这些假设点。')
 save(f,'zero_symmetry_quartet')
def envelope():
 f=base('实部，决定一项振荡的增长尺度','第17章 · 显式公式的直觉：先看单个零点项，不把它当作全部误差')
 a=f.add_axes([.085,.27,.48,.49],facecolor=BG);x=np.geomspace(2,1000,200)
 a.loglog(x,x**.875,color=GOLD,lw=2.5,label='β = 7/8');a.loglog(x,x**.5,color=TEAL,lw=2.5,label='β = 1/2');a.legend(frameon=False,fontsize=16);a.spines[['top','right']].set_visible(False);a.set_xlabel('x（对数刻度）');a.set_ylabel('归一化振幅 x^β（对数刻度）');a.grid(alpha=.12)
 b=panel(f,[.61,.27,.33,.49]);txt(b,.5,.92,r'$\rho=\beta+i\gamma$',26);txt(b,.5,.69,r'$x^\rho=x^\beta e^{i\gamma\log x}$',26)
 txt(b,.5,.45,'β：包络的幂次\nγ：随 log x 振荡',19);txt(b,.5,.13,'这里只比较 x^β\n完整单项另有系数 1/ρ',15,GOLD)
 foot(f,'素数加权计数的显式公式含 −xᵖ/ρ 型项（其中上标为零点ρ）；全局误差还要处理整个零点和。','曲线是精确幂函数，不是实测素数误差。截断、求和、对数因子和适用范围均不能由两条包络线替代。')
 # Avoid a Unicode superscript p that resembles the wrong mathematical symbol.
 f.texts[-2].set_text('素数加权计数的显式公式含零点项 −x^ρ/ρ；全局误差还要处理整个零点和。')
 save(f,'zero_real_part_envelope')
def checkers():
 f=base('两套检查器，仍可能共用同一份翻译','第18章 · 实现独立性与数学语义独立性是两条轴；此图不是任何实际运行日志')
 a=panel(f,[.06,.23,.88,.56]);
 for x,y,head,body in [(.17,.72,'原本的数学目标','全部相关对象与范围'),(.53,.72,'形式化陈述 F','具体对象、量词、假设'),(.53,.25,'共同依赖','库定理、基础公理、计算输入')]:
  a.add_patch(Rectangle((x-.14,y-.13),.28,.26,facecolor=LIGHT,edgecolor='none'));txt(a,x,y+.04,head,19);txt(a,x,y-.06,body,12)
 arr(a,(.32,.72),(.38,.72));txt(a,.35,.94,'翻译需审查',13,GOLD)
 for y,label in [(.81,'实现 A'),(.49,'实现 B')]:
  arr(a,(.68,.72),(.79,y));txt(a,.89,y,label,21);txt(a,.89,y-.10,'核对给定 F',12,MUTED)
 arr(a,(.59,.39),(.81,.73),MUTED,True);arr(a,(.67,.28),(.82,.43),MUTED,True)
 txt(a,.17,.28,'F 若译错，重复检查\n不会自动改成原目标',16,GOLD)
 foot(f,'不同实现通过同一证明，可降低单一实现缺陷的风险；共同陈述与依赖仍需分别审查。','A、B仅表示可能的独立实现，没有宣称复跑Lean、第二内核或任何公开项目；箭头不代表已完成验证。')
 save(f,'independent_checkers_shared_statement')
def odds():
 f=base('理解一份证明，能看见下一层为什么成立','第18章 · 奇数和等于平方：有限例子引路，一般的添层规则完成证明')
 a=f.add_axes([.08,.28,.35,.49],facecolor=BG);a.set_aspect('equal');a.set_xlim(0,5);a.set_ylim(0,5);a.axis('off')
 colors=[NAVY,TEAL,GOLD,'#72A6A0','#CEDBD2']
 for x in range(5):
  for y in range(5):a.add_patch(Rectangle((x,y),1,1,facecolor=colors[max(x,y)],edgecolor=BG,lw=2))
 for k in range(5):a.text(k+.5,k+.5,str(2*k+1),ha='center',va='center',color=BG if k<3 else NAVY,fontsize=20)
 b=panel(f,[.51,.27,.42,.5]);txt(b,.5,.91,'每加一圈，补上一个奇数',21);txt(b,.5,.68,r'$(n+1)^2-n^2=2n+1$',27,TEAL)
 txt(b,.5,.43,'从 1×1 正方形开始\n任意 n 都能用同一规则添层',18);txt(b,.5,.18,r'$1+3+\cdots+(2n-1)=n^2$',25)
 foot(f,'画出5×5只是一个例子；“对任意n都能添层”才给出归纳步骤，配合基例覆盖全部正整数。','这是一幅独立教学图，不是现成Lean证明或机器认证日志。可理解的结构解释为何成立，也帮助迁移方法。')
 save(f,'odd_sums_proof_geometry')
if __name__=='__main__':
 rank();counts();symmetry();envelope();checkers();odds()
 assert sum([4,1,1])**2/sum(v*v for v in [4,1,1])==2
 assert sum([1,2,3])==6 and sum(2*k+1 for k in range(5))==25
 print('six finishing figures produced; arithmetic assertions passed')
