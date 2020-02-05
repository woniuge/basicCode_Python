# -*- coding：utf-8 -*-

fpath = r'D:\DevelopSoft\pycharm\Projects\liaoxuefeng\OOP\文件读写\system.ini'

s = str()
with open(fpath,'r') as f:
    for line in f.readlines():
        s.__add__(line.strip())


print(len(s))

'''
print(s)
ST = str()
for i in s:
    ST.join(i)
print(ST)
print(len(ST))
'''
