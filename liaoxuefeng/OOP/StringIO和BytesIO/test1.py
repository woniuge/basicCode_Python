
'''
#StringIO顾名思义就是在内存中读写str。

#要把str写入StringIO，我们需要先创建一
#个StringIO，然后，像文件一样写入即可：

from io import StringIO
f = StringIO()
f.write('hello')
f.write('  ')
f.write('world!')
#getvalue()方法用于获得写入后的str。
print(f.getvalue())
'''

'''
#要读取StringIO，可以用一个str初始化StringIO，
# 然后，像读文件一样读取：
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s =='':
        break
    print(s.strip())
'''

'''
#StringIO操作的只能是str，如果要操作
# 二进制数据，就需要使用BytesIO

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
'''


#和StringIO类似，可以用一个bytes初始
# 化BytesIO，然后，像读文件一样读取：
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
