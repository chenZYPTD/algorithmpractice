from collections import deque
#deque队列，可以左添加和左删除
#https://www.lanqiao.cn/problems/1519/learning/
q=deque([])#队列的建立
N=int(input())
for _ in range(N):
    op=list(map(int,input().split()))#因为可能一行要输入两个数，所以就当作列表了.每次输入都会更新，所有数据存在队列里
    if op[0]==1:
      q.append(op[1])
    elif op[0]==2:
      if len(q)==0:
        print("no")
      else:
        print(q.popleft())
    else:
        print(len(q))
