import os
import sys
# https://www.lanqiao.cn/problems/502/learning/
# 请在此输入您的代码
num=int(input())
a=[]
for i in range(num):
    a.append(int(input()))
b=[i*1 for i in a if i>=60]
c=[i*1 for i in a if i>=85]
print(int(round(100*(len(b)/len(a)),0)),"%",sep='')#round函数是能够四舍五入的，但是int直接抹掉了小数点
print(int(round(100*(len(c)/len(a)),0)),"%",sep='')
