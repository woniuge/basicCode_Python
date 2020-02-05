class Animal(object):
    def run(self):
        print('Animal is running ...')

class Dog(Animal):
    def run(self):
        print("Dog is running...")
    def eat(self):
        print("Eating meat...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

dog =Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog,Dog))
print(isinstance(cat,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型
# 的run_twice()等函数。
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

# 动态语言的“鸭子类型”
# 对于Python这样的动态语言来说，则不一定需要传
# 入Animal类型。我们只需要保证传入的对象有一
# 个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')
run_twice(Timer())

print(type(dog))

a= Animal()
print(type(a))
