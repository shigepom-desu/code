import os
path = os.listdir('D:/workspace')
for index,filename in enumerate(path):
    #対象文字列を検索
    str_search = filename.find("vpn") 
    if str_search != -1:
        print(path[index])
    else:
        print("not found") 
    
