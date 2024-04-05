#DFS--玩具蛇
#https://www.lanqiao.cn/problems/1022/learning/
#2020国赛
sum=0
n,m=4,4
lis=[[False for i in range(m)] for i in range(n)]

def dfs(x,y,n):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  if n==16:
      global sum
      sum+=1
      return
  else:
    for i in range(4):
      tx=x+dx[i]
      ty=y+dy[i]
      if 0<=tx<4 and 0<=ty<4 and  not lis[tx][ty] :
        lis[tx][ty]=True
        dfs(tx,ty,n+1)
        lis[tx][ty]=False
for i in range(n):
  for j in range(m):
    lis[i][j]=True
    dfs(i,j,1)
    lis[i][j]=False
print(sum)