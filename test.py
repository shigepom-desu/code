from pathlib import Path
import glob

#PathObjectを生成
po = Path("D:/workspace")

print(list(po.glob("*")))