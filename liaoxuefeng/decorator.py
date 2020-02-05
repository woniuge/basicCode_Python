#decorator


'''
#1.一个完整的decorator的写法如下：

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
    
@log
def now():
    print('2015-3-25')

now()
print(now.__name__)
'''

'''
#2. 或者针对带参数的decorator：

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')


now()
print(now.__name__)
'''


'''
#3.1请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# _*_ coding: utf-8 _*_
import time,functools


#两层嵌套的decorator
def log_time(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        res = fn(*args,**kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
        return res
    return wrapper

@log_time
def fast(x,y):
    time.sleep(0.0012)
    return x + y

@log_time
def slow(x,y,z):
    time.sleep(0.1234)
    return x * y * z
    
f = fast(11,22)
s = slow(11,22,33)
print('The result and the name of the first function is {} and {}'.format(f,fast.__name__))
print('The result and the name of the second function is {} and {}'.format(s,slow.__name__))

if f != 33:
    print('测试失败！')
elif s != 7986:
    print('测试失败！')

'''
'''
#3.2请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# _*_ coding: utf-8 _*_
import time,functools

#三层嵌套的decorator,#给装饰器log_time()传入一个参数
def log_time(text):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kw):
            start = time.time()
            res = fn(*args,**kw)
            end = time.time()
            print('%s executed in %s ms' % (fn.__name__,end-start))
            return res
        return wrapper
    return decorator

@log_time("Dean is a handsome man!")
def fast(x,y):
    time.sleep(0.0012)
    return x + y

@log_time("Dean is a handsome man!")
def slow(x,y,z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11,22)
s = slow(11,22,33)
print('The result and the name of the first function is {} and {}'.format(f,fast.__name__))
print('The result and the name of the second function is {} and {}'.format(s,slow.__name__))

if f != 33:
    print('测试失败！')
elif s != 7986:
    print('测试失败！')
'''
'''
#4.在函数运行的前后输出begin call和end call:
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('begin call %s():' % func.__name__)
        func(*args,**kw)
        print('end call %s().'%func.__name__)
        #return func(*args,**kw)
    return wrapper

@log
def now():
    print('2015-3-25')
now()

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin to %s %s():' % (text,func.__name__))
            func(*args,**kw)
            print('end to %s %s().' % (text,func.__name__))
            #return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')
now()
'''


#5.再思考一下能否写出一个@log的decorator，使它既支持@log,又支持@log('execute')：

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if text != None:
                print("the text is %s and the call %s():" % (text,func.__name__))
                res = func(*args,**kw)
                return res
            else:
                print("call %s():" % func.__name__)
                res = func(*args,**kw)
                return res
        return wrapper

    #首先如果有参数，就跟原来一样直接返回decorator即可
    if isinstance(text,str):
        return decorator
    ##如果没有参数 其实log(func)就是log里边其实直接传的参数就是func 返回的应该是wrapper
    else:
        func = text
        text = None
        #所以这里的应该是直接decorator(func) 返回wrapper
        return decorator(func)

@log("there is a parameter in this edition")
def f1(x,y):
    return x*y

def main1():
    result=f1(2,3)
    print("the result is {}".format(result))
    print("the name of this function(with parameter) is " +f1.__name__)
@log
def f2(x,y):
    return x + y

def main2():
    result = f2(5,8)
    print("the result of this function(no_parameter) is {}".format(result))
    print("the name of this function is "+f2.__name__)

def main():
    number =int(input("please input a number to decide which the function to run:"))
    print(type(number))
    if number == 1:
        main1()
        print("run successfully!")
    else:
        main2()
        print("Run successfully!")

main()





