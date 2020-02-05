


import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON
def student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

s = Student('Bob',20,98)
print(json.dumps(s,default=student2dict))
#下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以
# 偷个懒，把任意class的实例变为dict：
print(json.dumps(s,default=lambda obj:obj.__dict__))

#同样的道理，如果我们要把JSON反序列化为一个Student对象实例，
# loads()方法首先转换出一个dict对象，然后，我们传入
# 的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
json_str = '{"age":20,"score":100,"name":"Bob"}'
print(json.loads(json_str,object_hook=dict2student))

#练习
#对中文进行JSON序列化时，json.dumps()提供了一
# 个ensure_ascii参数，观察该参数对结果的影响：

# -*- coding:utf-8 -*-
import json
obj = dict(name='小明',age = 20)
s = json.dumps(obj,ensure_ascii=True)
print(s)
s = json.dumps(obj,ensure_ascii=False)
print(s)