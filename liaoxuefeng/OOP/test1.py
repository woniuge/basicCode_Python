'''
#
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))

    def get_grade(self):
        if self.__score > 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',99)
bart.print_score()
lisa.print_score()


#干坏事，破坏访问限制
bart._Student__score = 100
print(bart._Student__name, bart.get_grade())

bart.age = 6
print(bart.age)
'''


# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender!')

# 测试
bart = Student('Bart','male')
if bart.get_gender() != 'male':
    print('测试失败！')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败！')
    else:
        print('测试成功！')





















