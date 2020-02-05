# -*- coding:utf-8 -*-

#获取对象信息
'''
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))
print(obj.y)
print(getattr(obj,'z',405))
print(hasattr(obj,'power'))
print(getattr(obj,'power'))
fn = getattr(obj,'power')
print(fn)
print(fn())
'''

'''
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)

del s.name
print(s.name)
'''

#小结
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

#为了统计学生人数，可以给Student类增加一个类属性，
# 每创建一个实例，该属性自动增加
class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count+=1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('lisa')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')