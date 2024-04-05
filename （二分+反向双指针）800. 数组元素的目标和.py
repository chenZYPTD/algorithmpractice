#800. 数组元素的目标和
#https://www.acwing.com/problem/content/802/
#核心，两个给定列表都是单调递增的
#方法一：二分法→→→→→→→→→→→→可以用的东西很多，包括快速找东西、排序、最值，核心在于能够缩小范围
#因为a[i]+b[j]=x，因此确定a[i]时，b[j]=x-a[i]
n, m, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    y = x - a[i]
    l, r = 0, m - 1
    while l <= r:#底下就是对b列表的标准二分操作，总时长为（nlogn）。虽然可以在这里再次遍历找数字，但是很可能超时（两重了）。
        mid = (l + r) // 2
        if b[mid] == y:
            print(i, mid)
            break
        elif b[mid] < y:
            l = mid + 1
        else:
            r = mid - 1
#方法二：双指针，反向的

#题目的核心不是“唯一”，并且还有两个列表，所以不要多想了。
n, m, x = map(int, input().split())
a =list(map(int, input().split()))
b =list(map(int, input().split()))

# 算法寻找对
j = m - 1
for i in range(n):#i不变,j慢慢找。
    while j >= 0 and a[i] + b[j] > x:
        j -= 1
    if j >= 0 and a[i] + b[j] == x:  # 检查和是否等于x
        print(i, j)