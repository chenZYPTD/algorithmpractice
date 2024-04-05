#统计子矩阵，100分的答案
#https://www.lanqiao.cn/problems/2109/learning/
#解释详见《专题挑战教程》P121
n, m, k = map(int, input().split())
a = [[0]*(m+1) for i in range(n+1)]#源矩阵
for i in range(1,n+1):
    a[i]=[0]+list(map(int,input().split()))
sum = [[0]*(m+1) for _ in range(n + 1)]#存储前缀和的矩阵
for i in range(1, n + 1):
    for j in range(1,m+1):
        sum[i][j]=sum[i-1][j]+a[i][j]#核心为分别算每一列的前缀和
ans = 0
for i in range(1,n+1):
    for j in range(i, n+1):
        l, r, t = 1, 1, 0#l左指针,r为右指针，t为矩阵所有数的和
        while r < m+1:
            t += sum[j][r] - sum[i-1][r]
            while t > k:
                t -= sum[j][l] - sum[i-1][l]
                l += 1
            ans += r - l + 1
            r += 1
print(ans)
'''
尺取法：
若sum[j2]-sum[j1]<=K,那么在sum列表的区间[j1,j2]上，有j2-j1+1个子区间满足区间和<=K
[1,3,6,10,15]
s[3]-s[0]<=10
j1,j2=0,3
j2-j1+1=4
'''