#统计子矩阵，70分的答案
#https://www.lanqiao.cn/problems/2109/learning/
#考点：1.二维前缀和的运用
#2.带有坐标矩阵的操作
#3.生成任意坐标区间
#满分答案要用到双指针的内容
def matrix_minus(sum,x1,x2,y1,y2):
#求(x2,y2)-(x1,y1)内所有元素的和.sum也应为被前缀和后矩阵
     return  sum[x2][y2]-sum[x1-1][y2]-sum[x2][y1-1]+sum[x1-1][y1-1]#用容斥原理可以推一推
n,m,k=map(int,input().split())
a=[[0]*(m+1) for i in range(n+1)]#因为这里涉及到具体的坐标，而矩阵的数字肯定是从1开始，所以构造(n+1)*(m+1),
                                #输出的时候再把多的删掉，a[i][1:]
                                #那个扫雷的没这么搞是因为那个用的是Δx和Δy
sum=[[0]*(m+1) for i in range(n+1)]
for i in range(1,n+1):
    a[i]=[0]+list(map(int,input().split()))#扫雷题那样用for i in range(n):
                                            # a.append(list_input())不好，因为这前面有个0，这样搞的话在后面的索引都要减一。
#预处理二位前缀和
for i in range(1,n+1):
    for j in range(1,m+1):
        sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+a[i][j]
#记录和不超过K的矩阵的数量
ans=0
#枚举左上角     跟二分有点像，相当于弄出一对任意、随机、全面的四元数组（原来的是二元，即左区间一个右区间一个，这样才能覆盖全部区间长度）
for x1 in range(1,n+1):
    for y1 in range(1, m + 1):
        #枚举相应的右下角
        for x2 in range(x1, n + 1):
            for y2 in range(y1, m + 1):
                if matrix_minus(sum,x1,x2,y1,y2)<=k:
                    ans+=1
print(ans)