#encoding:utf-8

'''
    首先判断该字符串是否为空，如果为空，就返回该字符串，
    如果不为空的话，就判断字符串首尾字符是否为空，
    如果为空，就使用递归再次调用该trim（）函数，否则返回该字符串
'''
def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return (trim(s[1:]))
    elif s[-1] == ' ':
        return (trim(s[:-1]))
    return s
