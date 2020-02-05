


#当我们要把test1.py中保存的对象从磁盘读到内存时，可以先把内容读到一
# 个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接
# 用pickle.load()方法从一个file-like Object中直接反序列化出对象。
import pickle

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)

#注：Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能
# 用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能
# 用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。