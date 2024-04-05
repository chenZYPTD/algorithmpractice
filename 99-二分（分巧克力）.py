import os
import sys
#合法+二分的主函数
# 二分也是一种求最值的方法
N,K=map(int,input().split())
a=[]
for i in range(N):
  x,y=map(int,input().split())
  a.append((x,y))

#二分只是个工具，需要判断其是否是合法的，然后才能缩小区间
#以下函数表示每一块巧克力在小巧克力边长为t的情况下切出的块数是否大于K
#只需把每一大块巧克力切块切的最大即可
def check(t):

  #cnt表示能够切出的块数
  cnt=0
  for H,W in a:
    cnt +=(H//t)*(W//t)#因为巧克力有k块，所以要算总块数
  return cnt>=K#注意这里要缩到外面去

#二分的主函数
left,right=1,100000#最大的取值是一万
ans=1
while left<=right:
#因为小方块小的话，当然可以满足，因此就要用二分来缩小区间。
#这类的最值就可以用二分了
#双指针是生成任意区间在判断的，二分的区间是逐次固定的
  mid=(left+right)//2
  if check(mid):
        ans=mid
        left=mid+1
  else:
        right=mid-1
print(ans)