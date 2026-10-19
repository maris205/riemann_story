import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/riemann-mpl-cache')
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties,fontManager
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
FONT='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc';fontManager.addfont(FONT)
plt.rcParams.update({'font.family':FontProperties(fname=FONT).get_name(),'axes.unicode_minus':False,'mathtext.fontset':'dejavusans','svg.fonttype':'path'})
P=Path(__file__).resolve().parents[1];BG='#F7F3E9';N='#173346';T='#178A86';G='#B78734';M='#637782'
f=plt.figure(figsize=(16,8),facecolor=BG)
f.text(.055,.90,'一根针转过所有方向，集合能有多小？',fontsize=28,color=N,weight='bold')
f.text(.057,.846,'三维挂谷问题 · 每个方向都要有一条长为 1 的线段；各线段的位置可以不同',fontsize=14,color=M)
a=f.add_axes([.025,.265,.49,.54],projection='3d',facecolor=BG)
i=np.arange(72);z=(i+.5)/72;phi=i*np.pi*(3-np.sqrt(5));r=np.sqrt(1-z*z)
d=np.column_stack([r*np.cos(phi),r*np.sin(phi),z]);centers=.07*np.column_stack([np.sin(2*phi),np.cos(3*phi),np.sin(phi)])
ends=np.stack([centers-d/2,centers+d/2],axis=1)
assert np.allclose(np.linalg.norm(ends[:,1]-ends[:,0],axis=1),1,atol=1e-14)
for j,e in enumerate(ends):a.plot(*e.T,color=G if j%9==0 else T,alpha=.9 if j%9==0 else .48,lw=2.7 if j%9==0 else 1.25)
# One unit segment is emphasized; all lengths are measured in 3D, not projection.
e=ends[0];a.scatter(*e.T,s=16,color=G)
a.text(*e[1], '  长度 1',color=G,fontsize=12)
a.set(xlim=(-.6,.6),ylim=(-.6,.6),zlim=(-.6,.6));a.set_box_aspect((1,1,1),zoom=1.18);a.view_init(23,-58);a.set_axis_off()
f.text(.085,.285,'72 个方向的有限示意',fontsize=18,color=T,weight='bold')
f.text(.085,.245,'图中有限条线段的并集维数仍是 1。',fontsize=12,color=M)
f.text(.085,.211,'它不覆盖所有方向，也不是零体积挂谷集合的构造。',fontsize=12,color=M)
# Reference cube, a genuinely three-dimensional positive-volume object.
b=f.add_axes([.54,.55,.16,.255],projection='3d',facecolor=BG)
v=np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]])
faces=[[v[k] for k in ids] for ids in [[0,1,2,3],[4,5,6,7],[0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7]]]
b.add_collection3d(Poly3DCollection(faces,facecolors=T,alpha=.12,edgecolors=T,linewidths=1.1));b.set(xlim=(0,1),ylim=(0,1),zlim=(0,1));b.set_box_aspect((1,1,1));b.view_init(23,-58);b.set_axis_off()
f.text(.73,.715,'单位立方体',fontsize=18,color=N)
f.text(.73,.663,'体积 1   ·   维数 3',fontsize=18,color=T)
f.text(.56,.51,'真正出人意料的是',fontsize=17,color=N)
f.text(.56,.449,'存在零体积的挂谷集合',fontsize=22,color=G,weight='bold')
f.text(.56,.389,'但在三维中，它们的维数仍必须是 3。',fontsize=16,color=N)
f.text(.56,.316,'体积：占据多少空间？',fontsize=15,color=M)
f.text(.56,.270,'维数：覆盖它所需的细节，随尺度怎样增长？',fontsize=15,color=M)
f.add_artist(plt.Line2D([.055,.945],[.175,.175],color='#D5DED6',lw=1))
f.text(.06,.115,'王虹 · Joshua Zahl，2025',fontsize=16,color=N)
f.text(.39,.111,r'$\dim_{\mathrm{H}} K=\dim_{\mathrm{M}} K=3$',fontsize=26,color=T)
f.text(.06,.055,'K 在每个方向含单位线段；H 为 Hausdorff 维数，M 为 Minkowski（盒）维数。此图只解释问题与结论，不展示证明。',fontsize=12,color=M)
for ext in ['png','svg']:f.savefig(P/'img'/f'kakeya_dimension_volume.{ext}',dpi=180,facecolor=BG)
np.savetxt(P/'src'/'unit_segments.csv',ends.reshape(72,6),delimiter=',',header='x0,y0,z0,x1,y1,z1',comments='')
(P/'src'/'validation.json').write_text(json.dumps({'segments':72,'max_unit_length_error':float(np.max(abs(np.linalg.norm(ends[:,1]-ends[:,0],axis=1)-1))),'finite_union_dimension':1,'render_is_kakeya_set':False},indent=2))
