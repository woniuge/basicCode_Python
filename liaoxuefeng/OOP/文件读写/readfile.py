

#1. 普通写法
f = open('D:\\DevelopSoft\\pycharm\\Projects\\liaoxuefeng\\OOP\\文件读写\\test.txt','r')
print(f.read())
f.close()

#2. 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会
# 调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使
# 用try ... finally来实现

try:
    f = open('D:\\DevelopSoft\\pycharm\\Projects\\liaoxuefeng\\OOP\\文件读写\\test.txt','r')
    print(f.read())
finally:
    if f:
        f.close()

#3. 更加简洁的写法
with open('D:\\DevelopSoft\\pycharm\\Projects\\liaoxuefeng\\OOP\\文件读写\\test.txt','r') as f:
    print(f.read())

#4. 按行读取
with open('D:\\DevelopSoft\\pycharm\\Projects\\liaoxuefeng\\OOP\\文件读写\\test2.txt','r') as f:
    for line in f.readlines():
        print(line.strip())

#5. 读二进制文件
with open('D:\\DevelopSoft\\pycharm\\Projects\\liaoxuefeng\\OOP\\文件读写\\test.jpg','rb') as f:
    print(f.read())

'''
字符编码问题，例如读取GBK编码的文件，且忽略非法编码的字符（即，若遇到编码错误，则直接忽略）：
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
'''

#6. 写文件
'''
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()
#注：当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存
#缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保
#证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写
#了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
'''

#简洁写法
with open('D:\\DevelopSoft\\pycharm\\Projects\\liaoxuefeng\\OOP\\文件读写\\test3.txt','w') as f:
    f.write('Hello,world!')
