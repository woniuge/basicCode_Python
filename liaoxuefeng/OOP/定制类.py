class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    def __call__(self):
        print('My name is %s.' % self.name)

print(Student('Michael'))
s = Student('Dean')
print(s.name)
print(s.score)
print(s.age())
#print(s.abc)
m=Student('Amy')
m()
print(callable(Student('Bob')))
print(callable(max))
print(callable([1,2,3]))
print(callable(None))
print(callable('str'))


class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1 #初始化两个计数器a,b

    def __iter__(self):
        return self#实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b#计算下一个值
        if self.a > 100000:#退出循环的条件
            raise StopIteration()
        return self.a#返回下一个值
    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    def __getitem__(self, n):
        if isinstance(n,int):#n是索引
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):#n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b=1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

for n in Fib():
    print(n)
f=Fib()
print(f[100])
print(list(range(100))[5:10])
print(f[:10])

#利用完全动态的__getattr__，可以写出一个链式调用：
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)