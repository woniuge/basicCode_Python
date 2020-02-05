class Student(object):
    pass
s = Student()
# 动态给实例绑定一个属性
s.name = "Michael"
print(s.name)

# 定义一个函数作为实例方法
def set_age(self,age):
    self.age = age

from types import MethodType
# 给实例绑定一个方法
s.set_age = MethodType(set_age,s)
# 调用实例方法
s.set_age(25)
# 测试结果
print(s.age)

def set_score(self,score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)
s2 = Student()
s2.set_score(99)
print(s2.score)


class StudentN(object):
    __slots__ = ('name','age')# 用tuple定义允许绑定的属性名称
# 创建新的实例
s=StudentN()
# 绑定属性'name'
s.name = 'Michael'
print(s.name)
# 绑定属性'age'
s.age = 25
print(s.age)
# 绑定属性'score'
s.score = 98

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，
# 对继承的子类是不起作用的：
# >>> class GraduateStudent(Student):
# ...     pass
# ...
# >>> g = GraduateStudent()
# >>> g.score = 9999
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性
# 就是自身的__slots__加上父类的__slots__。