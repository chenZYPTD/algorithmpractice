#利用循环绘制一个有*组成的菱形
n=int(input())
for k in range(n):
        print(' '*(n-k),end='')
        print('*'*(2*k+1))
print('*'*(2*n+1))
for k in range(n-1,-1,-1):
        print(' '*(n-k),end='')
        print('*'*(2*k+1))


