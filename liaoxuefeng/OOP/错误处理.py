'''
def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass
'''

'''
try:
    print('try...')
    r = 10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')
'''

'''
#可以有多个except来捕获不同类型的错误：
try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
finally:
    print('finally...')
print('END')
'''

'''
#Python内置的logging模块可以非常容易地记录错误信息：
# err_logging.py
import logging

def foo(s):
    return 10/ int(s)

def bar(s):
    return 2* foo(s)

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
'''

'''
#err_raise.py
#用raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value:%s' % s)
    return 10 / n

foo('0')
'''
'''
#err_reraise.py
#另一种错误处理的方式
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value:%s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise   #raise语句如果不带参数，就会把当前错误原样抛出

bar()
'''

#练习
# -*- coding：utf-8 -*-
from functools import reduce

def str2num(s):
    if s.count('.') == 1:
        return float(s)
    else:
        return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()


