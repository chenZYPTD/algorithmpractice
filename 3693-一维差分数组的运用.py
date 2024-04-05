# https://www.lanqiao.cn/problems/3693/learning/
n,q=map(int,input().split())
a=list(map(int,input().split()))
def chafen(x):
  k=len(x)
  cha=[0]*(k+1)  #这里弄k+1目的是因为后面减b的r+1位的数字，要保证这个r+1是存在的（虽然后面是统一减了个的，但是b[k]就代表着存在b是(k+1)个元素的序列）
  cha[0]=x[0]
  for i in range(1,k):
    cha[i]=x[i]-x[i-1]
  return cha
def qianzhuihe(x):
  k=len(x)
  sum=[0]*k
  sum[0]=x[0]
  for i in range(1,k):
    sum[i]=sum[i-1]+x[i]
  return sum
b=chafen(a)
for i in range(q):
  l,r,c=map(int,input().split())
  b[l-1]+=c
  b[r]-=c#很多差分的题目序列都是从1开始，这是要注意的
m=qianzhuihe(b[:n])
k=map(str,m)
print(' '.join(k))
