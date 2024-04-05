n=int(input())
a=[]
for _ in range(n):
  a.append(input())
mark=[False]*(n+1)
t=[0]*(n+1)
def dfs(i):
    if i==n:
        r = list(t[0:n])
        for g in r:
            print(a[g-1],end=' ')
        print()
        return
    else:
        for y in range(1,n+1):
            if not mark[y]:
                t[i]=y#代表这一位（第i层迭代）是被占用的
                mark[y]=True#代表这个数字是被占用了，不是层数
                dfs(i+1)
                t[i] = 0
                mark[y] = False
dfs(0)
