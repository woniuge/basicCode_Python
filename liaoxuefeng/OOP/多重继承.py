class Animal(object):
    pass

#大类：
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

#各种动物：
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

#给动物加上Runnable和Flyable的功能
# 这种设计通常称之为MixIn
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal,RunnableMixIn):
    pass

class Bat(Mammal,FlyableMixIn):
    pass

