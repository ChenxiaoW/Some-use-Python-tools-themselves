import os
import re
def drop():
    suff = input("�����뽫Ҫɾ���ļ��ĺ�׺���ԡ�.����ͷ��")
    file = os.listdir()
    reg = r'.*?'+suff
    r = re.compile(reg)
    for i in file:
        name = r.findall(i)
        if len(name) != 0:
            str = "".join(name)
            os.remove(str)
            print(str+'    ��ɾ��')
    print('Finish!!�� Please look��')
path = input("�����뽫Ҫɾ���ļ���·��")
try:
    os.chdir(path)
    drop()
except:
    print("û�����·������")