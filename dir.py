import os
path = os.listdir('D:/workspace/code/test')
for index,filename in enumerate(path):
    #対象文字列を検索
    str_search = filename.find("vpn") 
    if str_search != -1:
        rename = path[index].replace("vpn","")
        print(rename)
        os.rename(path[index],rename)
    