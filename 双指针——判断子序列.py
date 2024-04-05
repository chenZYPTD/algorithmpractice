#https://www.acwing.com/problem/content/2818/
n,m = map(int,input().split())
a = list(map(int,input().split()))
b= list(map(int,input().split()))
i,j=0,0
while True:
    if i == n:
        print("Yes")
        break
    if j == m:
        print("No")
        break#如果j能够完全扫描完，那么就没有子序列了
    if a[i] == b[j]:#小数列i指针先定着，等到大数列指针扫到a[0]再开始动
        i += 1
        j += 1
        continue
    j += 1