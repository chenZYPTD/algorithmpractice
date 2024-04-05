#BFS--走迷宫
#https://www.acwing.com/problem/content/846/
from collections import *
def bfs():
    queue=deque([])
    queue.append([0,0])#让起点（0,0）入队
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    mark[0][0]=0#mark为标记列表
    while queue:
        cur=queue.popleft()#cur即为队列被顶出来的坐标，接下来再四周要遍历
        for i in range(4):#遍历4个方向
            y = cur[1] + dy[i]
            x = cur[0] + dx[i]#注意下面0<=x<n，0<=y<m 不要取等，因为是从0开始
            if 0<=x<n and 0<=y<m and not maze[x][y] and mark[x][y]==-1:#即代表这三个条件同时满足：没出界；下一坐标（maze[x][y]）不是1；没走过
                queue.append([x,y])#满足上述所有条件即可入队，队的层数+1
                mark[x][y]=mark[cur[0]][cur[1]]+1#mark函数即为能够走到的层数，这一行代码相当于从上一个能走的坐标对应的层数mark[cur[0]][cur[1]]加上一，即层数+1
    return mark[-1][-1]#最外层的数即为我们所求
n,m=map(int,input().split())
maze=[]
for i in range(n):
    maze.append(list(map(int,input().split())))
mark=[[-1]*(m) for _ in range(n)]
print(bfs())
