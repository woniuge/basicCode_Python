# -*- coding:utf-8 -*-

import re

#版本一，验证简单的Email
def is_valid_email(addr):
    re_email = re.compile(r'^(\w+\.\w+|\w+)@(\w+).(com|org)$')
    if re_email.match(addr):
        #print(re_email.match(addr).groups())
        return True
    else:
        #print(re_email.match(addr))
        return False

#测试：
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

#版本二，提取带名字的Email地址：
def name_of_email(addr):
    re_name_of_email = re.compile(r'^(<(\w+\s\w+)>\s\w+|\w+\.\w+|\w+)@(\w+).(com|org)$')
    print(re_name_of_email.match(addr).groups())
    if re_name_of_email.match(addr).group(2) == None:
        print(re_name_of_email.match(addr).group(1))
        return re_name_of_email.match(addr).group(1)
    else:
        print(re_name_of_email.match(addr).group(2))
        return re_name_of_email.match(addr).group(2)

#测试：
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')