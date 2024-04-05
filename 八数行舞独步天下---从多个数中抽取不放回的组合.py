#https://www.lanqiao.cn/problems/16950/learning/
#八数行舞独步天下---从多个数中抽取不放回的组合

import math
from itertools import permutations
# def gcd(a,b):
#   return math.gcd(a,b)
# if math.gcd(i,j)==math.gcd(j,ic)==math.gcd(ic,ii)==1==math.gcd(i,ii):
#注意！！！！！！！！！！！！！！！！！！！！！！
#多个数互质不等于两两互质。

cp=0
nums=[1,2,3,4,5,6,8,9]
for i in permutations(nums):
  L=[i[0]*10+i[1],i[2]*10+i[3],i[4]*10+i[5],i[6]*10+i[7]]
  if math.gcd(math.gcd(math.gcd(L[0],L[1]),L[2]),L[3])==1 and L[0]>L[1]>L[2]>L[3]:

    cp+=1
print(cp)