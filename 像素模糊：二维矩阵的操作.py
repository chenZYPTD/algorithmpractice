#https://www.lanqiao.cn/problems/550/learning/
#像素模糊：二维矩阵的操作
def list_input():
    return list(map(int,input().split(' ')))
n,m=list_input()
a=[]
for k in range(n):
    a.append(list_input())
directions = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, -1), (1, 0),(0,0)]#注意，由于是包括其本身的，所以必须有（0，0）
b=[[0]*m for i in range(n)]
print("a={}".format(a))
for i in range(n):
    for j in range(m):
        lis_x = []#这个空列表应该在这里，因为(i,j)一定的时候，这个列表中收集的东西才是一个点（i,j）周围全部的数字
        for k in range(9):#因为包括点本身，所以遍历9次（用for dx,dy in directions 也是可以的）
                          #也可以for dx in[-1,0,1]:
                                     #for dy in [-1,0,1]:来做
            x, y = i + directions[k][0], j + directions[k][1]
            if 0<= x < n and 0<= y < m:
                lis_x.append(a[x][y])                   #也可以定义两个变量ans,num.只要执行到这个地方才会加一次，所以这样算的平均值也是可以的
                b[i][j] =int(sum(lis_x)/len(lis_x))
        print(b[i][j],end=' ')
    print()
#也可以这样输出结果
# for a in b:
#    print(' '.join(map(str,a)))