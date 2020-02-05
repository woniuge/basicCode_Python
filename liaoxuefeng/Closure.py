#利用闭包返回一个计数器函数，每次调用它返回递增整数：

#法一
def createCounter():
    m = 0
    def counter():
        nonlocal m
        m+=1
        return m
    return counter
'''
#法二
def createCounter():
    s = [0]
    def counter():
        s[0] = s[0]+1
        return s[0]
    return counter
'''


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')