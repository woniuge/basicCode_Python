
'''
#normalize,利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)
'''

'''
#prod,请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    def times(x,y):
        return x * y
    return reduce(times,L)
print(prod([3,5,7,9]))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
'''

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]

def str2float(s):
    m,n = s.split('.')
    mf = reduce(lambda x,y:x*10 + y,map(char2num,m))
    nb = reduce(lambda x,y:x*10 + y,map(char2num,n))
    l = len(n)
    return mf + nb/pow(10,l)
print(str2float('123.456'))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

