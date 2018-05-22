import os
import re
path = os.listdir('D:/workspace/code/test')
os.chdir('D:/workspace/code/test')

for file in path:
    target = re.compile("vpn")
    if target.search(file):
        dst = file.replace("vpn","")
        os.rename(file,dst)