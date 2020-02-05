'''
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
'''


'''
def fn(self,name='world'):#先定义函数
    print('Hello,%s.' % name)

#要创建一个class对象，type()函数依次传入3个参数：
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，
# 如果只有一个父类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函
# 数fn绑定到方法名hello上。
Hello = type('Hello',(object,),dict(hello=fn)) # 创建Hello class
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
'''

'''
# metaclass是类的模板，所以必须从'type'类型派生：
# 例子:这个metaclass可以给我们自定义的MyList增加一个add方法：
class ListMetaclass(type):
    def __new__(cls, name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

#有了ListMetaclass，我们在定
# 义类的时候还要指示使
# 用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list,metaclass=ListMetaclass):
    pass
L=MyList()
L.add(1)
L.add('abc')
print(L)
'''

'''
#尝试编写一个ORM(Object Relational Mapping,对象-关系映射)框架
#比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的
# 数据库表User，我们期待他写出这样的代码：
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id = 12345,name='Michael',email='test@orm.org',password='my-pwd')
#保存到数据库：
u.save()
'''
#按上述接口来实现该ORM
#首先定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)
#在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

#编写最复杂的ModelMetaclass：
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s' % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name #假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)

#编写基类Model：
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) value (%s)' % (self.__table__,','.join(fields),
                                                  ','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))

#比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的
# 数据库表User，我们期待他写出这样的代码：
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id = 12345,name='Michael',email='test@orm.org',password='my-pwd')
#保存到数据库：
u.save()