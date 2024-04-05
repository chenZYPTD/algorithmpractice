#152号习题：反倍数
#www.lanqiao.cn/problems/152/learning
import os
import sys

a=int(input())
b,c,d=map(int,str(input()).split(' '))
num_sum=0
for i in range(1,a+1):
  if i%b!=0 and i%c!=0 and i%d!=0:
    num_sum+=1
print(num_sum)
'''
算法优化：容斥定理
对于两个数a,b而言
1~n中为a的倍数有n//a个；
1~n中为b的倍数有n//b个；
1~n中为ab的倍数有n//ab个；
故1~n中为a的倍数或为b的倍数有n//a+n//b-n//ab个，而其补集就是我们所求的反倍数的个数
对于三个数a,b,c的讨论是类似的
'''