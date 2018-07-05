#!/usr/bin/env python
#coding=utf-8
#Author:Heitao

#有如下列表name_list=["ch_lisi","ch_zhangsan","wangwu"],我们需要找出非ch开头的名字，然后形成新的列表，我们利用函数实现如下
def start_ch(x):
    #这里返回的是一个布尔值
    return x.startswith('ch')

name_list=["ch_lisi","ch_zhangsan","wangwu"]
def find_name(func,array):
    new_name=[]
    for i in array:
        if not func(i):
            new_name.append(i)
    return new_name
print(find_name(start_ch,name_list))
#通过lambda函数实现找出除ch结尾的名字，如下
name_list1=["lisi_ch","zhangsan","wangwu_ch"]
def find_name(func,array):
    new_name=[]
    for i in array:
        if not func(i):
            new_name.append(i)
    return new_name
print(find_name(lambda x:x.endswith('ch'),name_list1))
#以上方式是我们根据自定义函数实现，接下来我们可以用内置函数filter函数实现，具体如下
#print(list(filter(lambda x:x.startswith('ch'),name_list)))    我们通过执行发现filter函数将匹配的名字生成了新的列表并输出了，我们需要不匹配的，因此改一下判断条件，如下
print(list(filter(lambda x:not x.startswith('ch'),name_list)))
print(list(filter(lambda x:not x.endswith('ch'),name_list1)))


