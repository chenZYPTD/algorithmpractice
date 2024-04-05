
#https://www.lanqiao.cn/problems/532/learning/
# 运用了贪心的思路，但是具体做起来是用了双指针的做法
#最值问题一般用的都是贪心的思想
#核心角度就是：局部最优（一个最大、一个最小和就是最小的）可以导致全局最优
#严谨的数学角度不好证，一般找反例来否定贪心算法
w=int(input())
n=int(input())
a=[]

ans=0
for _ in range(n):
    a.append(int(input()))
a.sort()#配对后才能实现一个大的配一个小的(局部最优)
l,r=0,n-1
while True:#以下四种情况都是有可能发生的
     if l==r:#这剩下的最后一个分为一组即可
          ans+=1
          break
     if l>r:#这两个特殊情况最好写前面，因为是对l和r都处理后的处理步骤
          break
     if a[l]+a[r]<=w:
         ans=ans+1
         l+=1
         r-=1
     else:
         ans+=1
         r-=1
print(ans)