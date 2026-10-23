"""Extract the two cited documentary frames from locally supplied source videos."""
import argparse
import subprocess
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('--ffmpeg', default='ffmpeg')
p.add_argument('--wang', type=Path, required=True)
p.add_argument('--deng', type=Path, required=True)
p.add_argument('--output', type=Path, required=True)
a = p.parse_args()
a.output.mkdir(parents=True, exist_ok=True)
for source, second, filename in [
    (a.wang, 142, '15_wang_red_coat.jpg'),
    (a.deng, 102, '15_deng_anime_desk.jpg'),
]:
    subprocess.run([a.ffmpeg, '-v', 'error', '-ss', str(second), '-i',
                    str(source), '-frames:v', '1', '-q:v', '2', '-y',
                    str(a.output / filename)], check=True)
