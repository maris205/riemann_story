import os
os.environ.setdefault('MPLCONFIGDIR','/tmp/riemann-ai-mpl')
os.environ.setdefault('XDG_CACHE_HOME','/tmp/riemann-ai-cache')
from pathlib import Path
import json,hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties,fontManager
from matplotlib.patches import FancyArrowPatch,Rectangle
FONT=next(str(p) for p in [Path('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'), Path('C:/Windows/Fonts/msyh.ttc')] if p.exists())
fontManager.addfont(FONT)
plt.rcParams.update({'font.family':FontProperties(fname=FONT).get_name(),'font.size':15,'axes.unicode_minus':False,'mathtext.fontset':'dejavusans','svg.fonttype':'path'})
BG='#F7F3E9';NAVY='#173346';TEAL='#178A86';GOLD='#B78734';MUTED='#637782';LIGHT='#D9E6DF'
PART=Path(__file__).resolve().parents[1]; IMG=PART/'img'
def base(title,subtitle):
 f=plt.figure(figsize=(16,8),facecolor=BG)
 f.text(.055,.915,title,fontsize=28,color=NAVY,weight='bold')
 f.text(.057,.864,subtitle,fontsize=13,color=MUTED)
 return f
def panel(f,rect):
 a=f.add_axes(rect,facecolor=BG);a.set_xlim(0,1);a.set_ylim(0,1);a.axis('off');return a
def txt(a,x,y,s,size=16,c=NAVY,ha='center',**kw): a.text(x,y,s,fontsize=size,color=c,ha=ha,va='center',**kw)
def arr(a,p,q,c=GOLD,dashed=False): a.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=17,lw=2,color=c,linestyle='--' if dashed else '-'))
def save(f,name):
 for ext in ['png','svg']:
  output=IMG/f'{name}.{ext}'
  f.savefig(output,dpi=180,facecolor=BG)
  if ext=='svg':
   output.write_text('\n'.join(line.rstrip() for line in output.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
 plt.close(f)
