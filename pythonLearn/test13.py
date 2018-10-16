#!/usr/bin/python
# -*-coding: UTF-8 -*-

# 正则表达式

import re

re.match(r'^\d{3}\-\d{3,8}$', '010-12345678')


# 切分字符串

re.split(r'\s+','a b  c')

# 分组（用()表示的就是要提取的分组（Group））

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')


# 贪婪匹配

result = re.match(r'^(\d+)(0*)$', '102300').groups()  # ('102300', '') 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了


# 编译-----------------------------

# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

re_telephone.match('010-12345').groups()


def is_valid_email(addr):
    if re.match(r'^[a-zA-Z.]*@[a-zA-Z]*.com$',addr):
        return True
    return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')

def name_of_email(addr):
    return re.match(r'^<?(\w+\s?\w+)>?\s?\w*@\w+.org$',addr).group(1)


assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'


