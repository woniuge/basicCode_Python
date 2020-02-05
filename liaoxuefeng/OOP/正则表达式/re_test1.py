# -*- coding:utf-8 -*-

import re

#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$','010 12345'))

#切分字符串
print('a b   c'.split(' '))
print(re.split(r'[\s\,\;]+','a,b;;   c d'))

#分组
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

#贪婪匹配
print(re.match(r'^(\d+?)(0*)$','102300').groups())

#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())