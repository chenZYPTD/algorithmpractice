#https://www.lanqiao.cn/problems/156/learning/
#螺旋矩阵
def list_input():
    return list(map(int,input().split(' ')))
n,m=list_input()
r,c=list_input()
pos=[[0]*m for i in range(n)]
x,y=0,0
value=1#可以用while一步一步加，也可用range(1,n*m+1)来一起填
pos[x][y]=value
while value < n*m:#不要忘记循环条件
    #要求：保证下一个点不越界；保证下一点没有数字
    while y+1<m and pos[x][y+1]==0:#因为要判断下一个点，因此这里都是y+-1的条件判断
        y +=1
        value +=1
        pos[x][y] = value
    while x+1<n and pos[x+1][y] == 0:
        x += 1
        value += 1
        pos[x][y] = value
    while y-1>=0 and pos[x][y-1]==0:
        y -=1
        value +=1
        pos[x][y] = value
    while x-1>=0 and pos[x-1][y] == 0:
        x -= 1
        value += 1
        pos[x][y] = value
print(pos[r-1][c-1])
#思考：可否用range(1,n*m+1)来填，感觉不是很好搞
#基于此会有很多改编，数字会按照各种各样的要求来走，实际上都是本题目的举一反三