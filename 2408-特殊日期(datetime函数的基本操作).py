#https://www.lanqiao.cn/problems/2408/learning/
#datetime函数的操作
from datetime import *
dt1=datetime(1900,1,1)
dt2=datetime(9999,12,31)
ans=0
b=dt2-dt1
for _ in range(2958463):
  dt1+=timedelta(days=1)
  d=list(str(dt1.day))
  m=list(str(dt1.month))
  y=list(str(dt1.year))
  d_1=map(int,d)
  m_1 = map(int, m)
  y_1 = map(int, y)
  if sum(y_1)==sum(m_1)+sum(d_1):
    ans+=1
print(ans)
