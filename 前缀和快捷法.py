#https://www.acwing.com/problem/content/797/
# def qianzhuihe(a):
#     b=len(a)
#     sum=[0]*b
#     sum[0]=a[0]
#     for i in range(b):
#         sum[i]=sum[i-1]+a[i]
#     return sum
# def cha_qzh(sum,l,r):
#    if l==1:#特别关注：注意，由于题干的区间不是索引，故这里头区间应当是1，其它地方也有相应的修改
#        return sum[r-1]#这里索引区间是比实际区间小1的
#    else:
#         return sum[r-1]-sum[l-2]
# n,m=map(int,input().split())
# t=list(map(int,input().split()))
# for _ in range(m):
#     l,r=map(int,input().split())
#     a=qianzhuihe(t)
#     print(cha_qzh(a,l,r))

'''
虽然上面是标准算法，但是会超时，最大数字为十万
以下是不超时的方法：
①创建一个大0列表是很必要的
②prefix[i+1] = prefix[i] + nums[i]也是被推荐的，不用管a[0]的问题
③
'''

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefix = [0] * (n + 10)
for i in range(n):
    prefix[i+1] = prefix[i] + nums[i]  # 这样加那么prefix[1]=nums[0]+0了，就没有那么多分类讨论了，减少复杂度
for i in range(m):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l-1])  # 求部分和