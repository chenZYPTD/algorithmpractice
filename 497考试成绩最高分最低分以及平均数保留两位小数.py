import os
import sys
# https://www.lanqiao.cn/problems/497/learning/
# 请在此输入您的代码
num=int(input())
a=[]
for i in range(num):
    a.append(int(input()))
print(max(a))
print(min(a))
print("{:.2f}".format(sum(a)/num))
# 如果用round函数的话，可能会出现这样的情况：
# round(12.80,2)=12.8输出的就不是两位小数了，我们可以用{:.2f}.format(n)来进行四舍五入运算

