# https://www.lanqiao.cn/problems/3694/learning/
n,m,q =map(int,input().split())
ori=[[0]*(m+1) for _ in range(n+1)]
processed=[[0]*(m+2) for _ in range(n+2)]#这里为了定坐标（左边的一堆0）加上右边的冗余（x2+1），所以是(n+2)*(m+2)的矩阵，当然下面是可以改索引的（左边的不用那么多0，但是右边还是有冗余）
for i in range(1,n+1):
    ori[i]=[0]+list(map(int,input().split()))
for i in range(1,n+1):#最好从1~n+1遍历
    for j in range(1,m+1):#差分这里就没必要先封装一个函数了，直接遍历即可
        processed[i][j]=ori[i][j]-ori[i-1][j]-ori[i][j-1]+ori[i-1][j-1]
for _ in range(q):
    x1,y1,x2,y2,c=map(int,input().split())
    processed[x1][y1]+=c
    processed[x1][y2+1]-=c
    processed[x2+1][y1]-=c
    processed[x2+1][y2+1]+=c
for i in range(1,n+1):#这里必须从从1~n+1遍历，不然出现了[-1]就不好办了
    for j in range(1,m+1):
        ori[i][j]=ori[i-1][j]+ori[i][j-1]-ori[i-1][j-1]+processed[i][j]
for i in range(1,n+1):
    print(' '.join(map(str,ori[i][1:m+1])))


