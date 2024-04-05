#2022国赛
#DFS--最大数字
#https://www.lanqiao.cn/problems/2193/learning/

N, a, b = map(int, input().split())
n = str(N)
m = len(n)
res = 0
def dfs(i, v, a, b):#这里的顺序是从0开始，一步一步往后面的位数加。
    global res#通过改位数可以吗？应该。即向原本是一串数字，然后转成字符串再转成列表，比大小又要转成字符串再转成列表；读取时要用字符串，操作时要用列表，太麻烦了！
    if i == m:
        res = max(res, v)
        return
    else:
        c = int(n[i])
        g = min(a, 9 - c)
        dfs(i + 1, v * 10 + g + c, a - g, b)#如果只传了dfs(i + 1, v * 10 + g + c)两个参数，那就要保存现场还原现场了，不过本代码集成了一下，直接把标记参数一同传进去了
        if b > c:
            dfs(i + 1, v * 10 + 9, a, b - c - 1)

dfs(0,0,a,b)#一般从0开始，到n-1(i==n时直接输出了，因此次数是没问题的)
print(res)


