
#我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中
# 叫pickling，在其他语言中也被称之为serialization，marshalling，
# flattening等等
import pickle

d = dict(name='Bob',age=20,score=90)
print(pickle.dumps(d))

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()