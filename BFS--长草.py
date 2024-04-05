from collections import *  # 记得这个库，deque是在collection里面的，itertools是迭代器

# 14天培训班的代码太抽象了，下面才是比较正常的代码书写习惯
q = deque()
'''
本题的特色在于不需要设定一个记录路径的列表，原因显而易见。
'''
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
Map = []
for i in range(n):
    Map.append(list(input()))  # 日常输入操作
for i in range(n):
    for j in range(m):
        if Map[i][j] == 'g':
            q.append((i, j))  # 如果是在要求中的，那就直接入队
k = int(input())


def bfs():
    t = len(q)  # 本题与其它BFS的模型题的最大区别在于此
    # 特别关注(自己不亲手闭卷打一遍就根本不知道这里的问题)：#不能用全局变量，否则在下面for _ in range(k):中，t的值会一直被消耗的，而不会随着本轮bfs结束后初始化一边
    while t:  # 其它模型题是只要队列不空，就继续循环，直到不能继续往下走为止；但是本题只要求每一次走一遍即可，不需要走到底；
        # 如果这里还是while len(q):---->那全是'g'了。
        temppair = q.popleft()  # 先出队最前面的
        x, y = temppair[0], temppair[1]
        for i in range(4):
            nowx = x + dx[i]
            nowy = y + dy[i]
            if 0 <= nowx < n and 0 <= nowy < m and Map[nowx][nowy] == '.':
                q.append((nowx, nowy))
                Map[nowx][nowy] = 'g'
        t -= 1


for i in range(k):  # 这是重复次数，每一次基于上一次的BFS来BFS
    bfs()
for i in range(n):
    print(''.join(Map[i]))  # 不要打空格


