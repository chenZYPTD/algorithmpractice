# 153:洁净数
# https://www.lanqiao.cn/problems/153/learning/
#问一下老师吧，莫名其妙不能执行，当然本题最好的方法就是字符串遍历
n=int(input())
nusum = 0
for i in range(1,n+1):
  ok = True
  for m in range(0,7):#考虑到题目最大输入数字为一百万。
     if i//(10**m)%10==2 :#i整除10的k次方为删去后k位，然后取10的余数就可以判断其末尾的数字了
       ok=False
       break
  if ok:
    nusum+=1
print(nusum)