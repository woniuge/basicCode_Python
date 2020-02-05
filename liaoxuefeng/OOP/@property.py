
'''
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score=value

s = Student()
s.set_score(60)
print(s.get_score())
'''

'''
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
#实际转化为s.set_score(60)
s.score = 60
print(s.score)
'''

'''
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2018-self._birth

s= Student()
s.birth = 1994
print(s.birth)
print(s.age)
s.birth = 1998
print(s.birth)
print(s.age)
'''

# -*- coding:utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height=value

    @property
    def resolution(self):
        return self._height * self._width

#测试：
s = Screen()
s.width = 1024
s.height = 768
print('resolution =',s.resolution)
if s.resolution == 786432:
    print('测试通过！')
else:
    print('测试失败！')