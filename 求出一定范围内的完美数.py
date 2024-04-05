#求出一定范围内的完美数
n=int(input())
for i in range(1,n+1):
   sum = 0
   #6-8行是求出一个数字的因子和
   for k in range(1,i):
      if i%k==0:
         sum+=k
   #判断这个数字是否为完美数，注意缩进的区间，因为判断核心为i，因此，这里的if应在外面的循环里。
   if sum==i:
      print(i,end=' ')

