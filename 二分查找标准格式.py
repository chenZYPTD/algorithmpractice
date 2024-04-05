#二分查找模板代码
#https://www.acwing.com/problem/content/791/
def erfen_min(lis,x):
    left,right=0,len(lis)-1
    while left < right:#left==right就是终点了
        mid=(left+right)//2#mid每次都要更新，因此在循环里面
        if lis[mid]>=x:
            right= mid#考虑到有时right指的地方就是第一次出现的情况，但此时left没过来，所以若在下一轮减一的话，那就错过了正确答案了
        else:
            left = mid + 1#看看这个1,可以不要，但由于mid必定不是解，所以干脆排了
    if x not in lis:
        return -1
    return left
def erfen_max(lis,x):
    left, right = 0, len(lis) - 1
    while left < right:  # left==right就是终点了
        mid = (left + right +1) // 2  # mid每次都要更新，因此在循环里面
        if lis[mid] <= x:
            left = mid
        else:
            right= mid - 1
    if x not in lis:
        return -1
    return right
n,q=map(int,input().split())
lis=list(map(int,input().split()))
for _ in range(q):
    k=int(input())
    a,b=erfen_min(lis,k),erfen_max(lis,k)
    print(a,b,sep=' ')



