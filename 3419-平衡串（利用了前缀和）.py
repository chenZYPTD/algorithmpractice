#区间的统计就可以考虑用前缀和
#https://www.lanqiao.cn/problems/3419/learning/
#令L=1,Q=-1,如果是平衡串，那么和为0
# 这个题也是对如何求“最大值”的一个例子
from itertools import accumulate
def pre_sum(q):
    return list(accumulate(q))
#或者
def s_pre_sum(q,l,r):
    if l==0:
        return q[r]
    else:
        return (q[r]-q[l-1])
S =input()
n=len(S)
a=[]
for x in S:
    if x=="L":
       a.append(1)
    else:
        a.append(-1)
sum=pre_sum(a)
ans=0
for i in range(n):
    for j in range(i,n):#核心还是枚举，枚举所有可能的区间
        if s_pre_sum(sum,i,j)==0:#若等于0，那就是一个合法的区间，但不一定是最大的
            ans=max(ans,j-i+1)
print(ans)

# 另外一种纯切片的方式，最直接的方法
# x=list(input())
# n=len(x)
# ans=0
# for i in range(n):
#     for j in range(i,n):
#         tes=x[i:j+1]
#         if tes.count("L")==tes.count("Q"):
#            ans=max(ans,j-i+1)
# print(ans)


