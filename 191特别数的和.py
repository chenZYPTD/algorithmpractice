import os
import sys
# 191特别数的和
# 如果用循环，可以参考153中整除的方法判断某一个数字的某一位是否含有某个数字；不过这要求这个数字

sum=0
n=eval(input())
for i in range(1,n+1):
   if "2"in str(i) or "0"in str(i) or "1"in str(i)or"9"in str(i):
       sum+=i
print(sum)