#!/usr/bin/env python
#coding=utf-8
#Author:Heitao

#我们有一个列表num=[1,2,3,4],我们要计算这个列表的综和我们可以根据内置方法sum，进行计算如下
num=[1,2,3,4]
print(sum(num))
#但是如果我们要计算加减乘除以及设定初始计算的数字，我们需要自定义函数来实现，但是我们的reduce函数帮我们解决了这一难题，具体实现如下
#我们要先导入reduce模块，在py2中是直接可以用的
from functools import reduce
#计算列表的加减乘除
num=[1,2,3,4]
print(reduce(lambda x,y:x+y,num))
print(reduce(lambda x,y:x-y,num))
print(reduce(lambda x,y:x*y,num))
print(reduce(lambda x,y:x/y,num))
#以上是没有指定初始范围，默认是None，如果指定初始范围，如下
print(reduce(lambda x,y:x+y,num,1)) #(相当于1+1+2+3+4)
print(reduce(lambda x,y:x-y,num,10)) #（相当于10-1-2-3-4）
print(reduce(lambda x,y:x*y,num,0)) #(相当于0*1*2*3*4)
print(reduce(lambda x,y:x/y,num,10)) #(相当于10/1/2/3/4)
