#!/usr/bin/python3
#coding=utf8
#Author:HeiTao

"""
此脚本为字符串的联系，两个练习
1：输入一个字符串，遍历整个字符串并打印出每个字符的索引位置
2：输出整个字符串中有多少个数字，字母和特殊字符，查找字符串中是否有重复的字符，查找出重复字符的索引位置
"""

str_test=input("输入一个字符串: ")
a=""
b=""
c=""
print("索引位置\t元素".expandtabs(15))
for i in str_test:
    print("%s\t%s".expandtabs(20)%(str_test.index(i),i))
    if str_test.count(i) > 1:
        if i not in c:
            c+=i
    #判断字符是数字，字母或者其他
    if i.isalpha():
        a+=i
    elif i.isalnum():
        b+=i

print("重复字符有如下%s"%c)
print("字母有%d个"%len(a))
print("数字有%d个"%len(b))
print("特殊字符有%d个"%(len(str_test)-len(a)-len(b)))

