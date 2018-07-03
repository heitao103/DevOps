#!/usr/bin/python3
#coding=utf8
#Author:HeiTao

"""
此脚本为字符串的联系，两个练习
1：输入一个字符串，遍历整个字符串并打印出每个字符的索引位置
2：输出整个字符串中有多少个数字，字母和特殊字符，查找字符串中是否有重复的字符，查找出重复字符的索引位置
"""

str_test=input("输入一个字符串: ")
A=""
B=""
C=""
#遍历字符串
print("索引\t字符".expandtabs(15))
# for i in str_test:
#     print("%d\t%s".expandtabs(20)%(str_test.index(i),i))
for a,b in enumerate(str_test):
    print("%d\t%s".expandtabs(20)%(a,b))
    #判断是否有重复字符
    if str_test.count(b) > 1:
        if b not in C:
            C+=b
    if b.isalpha():
        B+=b
    elif b.isdigit():
        A+=b
print("字母有%s个"%len(B))
print("数字有%s个"%len(A))
print("特殊字符有%s个"%(len(str_test)-len(A)-len(B)))

#重复字符个数
for i in C:
    print("重复字符%s有%d个"%(i,str_test.count(i)))

find_str=input("输入您要查找的字符: ")
if find_str not in str_test:
    print(find_str+"不存在与{test}中".format(test=str_test))
else:
    print("%s的索引位置是%s"%(find_str,str_test.index(find_str)))