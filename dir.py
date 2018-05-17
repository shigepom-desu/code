import os
path = os.listdir('D:/workspace')
for filename in path:
    #対象文字列を検索
    index = filename.find("vpn")
    if index != -1:
        print("found at")
    else:
        print("not found") 
    
