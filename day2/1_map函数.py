#!/usr/bin/env python
#coding=utf-8
#Author:Heitao

#假如我们有一个列表num=[1,2,3,4],接下来我们要对这个列表进行加减乘除操作，具体实现方法如下
'''
num=[1,2,3,4]
new_num=[]
for i in num:
    new_num.append(i*2)
print(new_num)
'''
#现在我们有多个列表，要进行加减乘除操作。我们可以用一个函数来完成
'''
num=[1,2,3,4]
def sum(array):
    new_num = []
    for i in array:
        new_num.append(i*2)
    return new_num
print(sum(num))
'''
#现在我们来实现加减乘除。
'''
#加1
def jia(x):
    return x+1
#减1
def jian(x):
    return x-1
#乘2
def cheng(x):
    return x*2
#除1
def chu(x):
    return int(x/1)
#定义逻辑函数
num=[1,2,3,4]
def sum(func,array):
    new_num = []
    for i in array:
        new_num.append(func(i))
    return new_num
print(sum(jia,num))
print(sum(jian,num))
print(sum(cheng,num))
print(sum(chu,num))
'''
#我们也可以利用我们的lambda函数,如下
#定义逻辑函数
'''
num=[1,2,3,4]
def sum(func,array):
    new_num = []
    for i in array:
        new_num.append(func(i))
    return new_num
print(sum(lambda x:x+1,num))
print(sum(lambda x:x-1,num))
print(sum(lambda x:x*1,num))
print(sum(lambda x:int(x/1),num))
'''
#因此以上逻辑我们可以用map函数完成，如下
num=[1,2,3,4]
print(list(map(lambda x:x+1,num)))
print(list(map(lambda x:x-1,num)))
print(list(map(lambda x:x*2,num)))
print(list(map(lambda x:int(x/1),num)))


