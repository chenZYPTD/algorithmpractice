#DFS-N皇后搜索
# https://www.lanqiao.cn/problems/1508/learning/
n=int(input())
sum=0
t=[0]*15#一个表示行列的方式为用t[a]=i表示第a行第i列，精妙的表示法
def dk(k):
    for i in range(1,k):
        if abs(t[k]-t[i])==abs(k-i):
            return False
        elif t[k]==t[i]:#列数相等时;行数不用刻意判断，因为k==i时也会算的
            return False
    return True
def dfs(a):
    if a > n:  # 出局判断
        global sum
        sum += 1
        return
    else:
        for i in range(1, n + 1):
            t[a]=i#保存现场，第a个皇后的列数（行数本身就是不同的，所以只用管列数）
            if dk(a):
                dfs(a+1)
            else:
                         #为什么不还原现场了？原因：dk(k)已经判断了只要在走，就一定符合要求，因此不用回滚
                continue
dfs(1)
print(sum)

