import os
import re
def drop():
    suff = input("请输入将要删除文件的后缀（以‘.’开头）")
    file = os.listdir()
    reg = r'.*?'+suff
    r = re.compile(reg)
    for i in file:
        name = r.findall(i)
        if len(name) != 0:
            str = "".join(name)
            os.remove(str)
            print(str+'    已删除')
    print('Finish!!！ Please look！')
path = input("请输入将要删除文件夹路径")
try:
    os.chdir(path)
    drop()
except:
    print("没有这个路径！！")