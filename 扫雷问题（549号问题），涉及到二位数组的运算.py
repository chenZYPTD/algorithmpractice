#https://www.lanqiao.cn/problems/549/learning/
#扫雷问题，涉及到二位数组的运算
def input_list():
    return list(map(int,input().split(' ')))
n,m=input_list()
a=[]#把读入的0、1数组全部存到a中
for i in range(n):
    a.append(input_list())
b=[[0]*m for i in range(n)] #前面的[0]*m表示m列，后面的for i in range(n)表示n行
                            #b的初始状态为n*m的0矩阵
#枚举第i行第j列，<i,j>
#对于任意一个点，我们用Δx和Δy表示其周围的八个点的坐标,存的东西都是Δx和Δ
'''
即
(x-1,y+1)(x+0,y+1)(x+1,y+1)
(x-1,y+0)( x , y )(x+1,y+0)
(x-1,y-1)(x+0,y-1)(x+1,y-1)
'''
directions=[(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, -1), (1, 0)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:#即为1(bool数不为0)
            b[i][j] = 9
        else:
            b[i][j] = 0 #初始化这个位置的数字，然后再下列的代码一个一个统计
            for k in range(8):
                x, y = i + directions[k][0], j + directions[k][1]
                if 0 <= x < n and 0 <= y < m: #保证新坐标在矩阵内
                    b[i][j] += a[x][y]#如果新坐标不是0，那就加上去
        print(b[i][j], end=' ')#注意这里的缩进，这里每次打印只会打印一个数，然后打印m次（行数）
    print()#代表每次要换行n次,因为print函数默认是end='\n'的，所以不用再打一个"\n"了


#ChatGPT提供了一个更为易读的函数
# 1、将 dir 改为 directions，以避免与Python内置函数冲突。
# 2、将计算周围雷数的逻辑封装在 calculate_neighbor_mines 函数中，提高了代码的可读性和模块化。
# 3、添加了对边界情况的完整处理，确保不会出现索引错误。
# 4、将输出结果的逻辑封装在 print_matrix 函数中，提高了代码的可读性和可维护性。
# 5、将主要的逻辑放在 main 函数中，以便更好地组织和管理代码。
# 6、改进了变量名的可读性，提高了代码的清晰度。
# def input_list():
#     return list(map(int, input().split(' ')))
#
# def calculate_neighbor_mines(a, n, m):
#     directions = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, -1), (1, 0)]
#     b = [[0] * m for _ in range(n)]
#
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == 1:
#                 b[i][j] = 9
#             else:
#                 for dx, dy in directions:
#                     x, y = i + dx, j + dy
#                     if 0 <= x < n and 0 <= y < m:
#                         b[i][j] += a[x][y]
#
#     return b
#
# def print_matrix(matrix):
#     for row in matrix:
#         for cell in row:
#             print(cell, end=' ')
#         print()
#
# def main():
#     n, m = input_list()
#     a = []
#
#     for _ in range(n):
#         a.append(input_list())
#
#     b = calculate_neighbor_mines(a, n, m)
#     print_matrix(b)
#
# if __name__ == "__main__":
#     main()