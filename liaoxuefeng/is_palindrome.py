#利用filter()筛选出回数：

'''
#生成初始序列
def num():
    n = 0
    while True:
        n = n + 1
        yield n

def is_palindrome(n):
    n1 = str(n)
    n2 = n1[::-1]
    if n2 == n1:
        return n
'''

#牛人的简单写法
def is_palindrome(n):
    return str(n) == str(n)[::-1]

#print(is_palindrome(1222221))

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')