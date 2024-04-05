#BFS-走迷宫(2)
#https://www.lanqiao.cn/problems/1216/learning/
from collections import *
n, m = map(int, input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int,input().split())))

mark=[[-1]*m for  _ in range(n)]#至于为什么是-1
x1,y1,x2,y2=map(int,input().split())
q=deque()
dy=[1,-1,0,0]
dx=[0,0,1,-1]
def bfs(x,y):#提供初始值然后bfs(当然也可以不提供，这到无所谓，直接bfs()也可以)_
    q.append([x,y])
    mark[x][y]=0
    while q:
        now=q.popleft()
        nx,ny=now[0],now[1]
        if nx==x2-1 and ny==y2-1:
            break
        for i in range(4):
            x_n=nx+dx[i]
            y_n=ny+dy[i]
            if 0<=x_n<n and 0<=y_n<m and mark[x_n][y_n]==-1 and maze[x_n][y_n]==1:
                q.append([x_n,y_n])
                mark[x_n][y_n]=mark[nx][ny]+1
    return mark[x2-1][y2-1]
print(bfs(x1-1,y1-1))

        

