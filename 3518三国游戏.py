import os
import sys
#2023蓝桥杯省赛A组python真题：三国游戏
# https://www.lanqiao.cn/problems/3518/learning/
def compare(a,b,c,n):
  cnt,s=0,0
  tmp=[0]*n#这里不能直接乘以100000，不然一排序，列表最前面的就是一堆0了
  for i in range(n):
    tmp[i]=a[i]-(b[i]+c[i])
  tmp.sort()
  for i in range(n-1,-1,-1):#为了贪心，保证和大于0，所以就是要尽可能找大的
    if s+tmp[i]>0:
      s+=tmp[i]
      cnt+=1
    else:#如果小于0，即不满足条件，就直接停了，最终cnt即为结果
      break
  return cnt
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=0
ans=compare(a,b,c,n)
ans=max(ans,compare(b,a,c,n))
ans=max(ans,compare(c,b,a,n))
if ans==0:
  print(-1)
else:
  print(ans)



