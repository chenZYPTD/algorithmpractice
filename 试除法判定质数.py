#试除法判定质数
#https://www.acwing.com/problem/content/868/
from math import *
def prime(x):
    if x==1:
        return False#1不是质数
    if x == 2:
        return True
    i=2
    while i<=sqrt(x):#这里一定要取等，因为可能x就是两个质数的平方，而只要是小于x都可以满足不被x整除
        if x%i==0:
            return False
            break
        i+=1
    return True

n = int(input())
t = []
for _ in range(n):
    t.append(int(input()))
for i in t:
    if prime(i):
        print("Yes")
    else:
        print("No")



