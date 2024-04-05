#https://www.lanqiao.cn/problems/143/learning/
#”模拟“题（1）——换瓶盖
import os
import sys

# # 请在此输入您的代码
# n=int(input())
# ans=n
# while True:
#   if n>=3:       #这不是奥数题，这是计算机题，因此可以分轮次一次一次处理每一个步骤；
#      n = n - 3
#      ans=ans+1   #因为计算机可以大量逐次计算，所以把每一次换瓶盖的步骤模拟出来，即可满足我们的要求
#      n=n+1
#   else:
#     break
# print(ans)
#

#第二种解法：核心是明确变量所表示的含义：n就是从始至终的获得的饮料数，ans是你喝下的饮料数
n=int(input())
ans=n
while True:
    if n>=3:
        ans=ans+n//3
        n=n%3+n//3#等式右边的n都是n的初始值/最终值，因此不要到上面或者下面对n再赋值了，因为这是在整体操作而不是像第一种方法那样一步一步来了
    else:
        break
print(ans,n)