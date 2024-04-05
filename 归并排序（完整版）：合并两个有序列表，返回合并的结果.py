#归并排序：合并两个有序列表，返回合并的结果
#注释，好像测试程序(例如本项目中的"main.py"才能通过暂停来分步骤来debug)
def Merge(A,B):
    result=[]
    while len(A)!=0 and len(B)!=0:
        if A[0]<=B[0]:
            result.append(A.pop(0))
        else:
            result.append(B.pop(0))
    result.extend(A)
    result.extend(B)  #保证两者之一的最后一个（即整个列表的最大值）可以被放进去
    return result
# a=[1,3,6,8]
# b=[0,2,7,12]
# sorted_1=Merge(a,b)#这里要重新定义一个变量，因为函数的返回值才是被排序后的结果
# print(' '.join(map(str,sorted_1)))
#然而还没完，因为a,b有序是不知道的
def MergeSort(A):
    if len(A)<2:
        return A
    mid=len(A)//2
    left=MergeSort(A[:mid]) #每一段是怎么排的我们不用管，用递归处理(看不懂的话debug一下就知道了)
    right=MergeSort(A[mid:])#可以理解为分段后的东西也会按照这段算法来排序,最终变成单元素列表后
    return Merge(left,right)#left和right就是分别切割后的"A"了，然后用Merge缝合并排序，从而形成上一迭代的left或right
n = int(input())           #写递归的核心在于，只考虑当前位置如何处理，子问题是怎么处理的，不管。
a = list(map(int, input().split()))
sorted_1=MergeSort(a)#这里要重新定义一个变量，因为函数的返回值才是被排序后的结果
print(' '.join(map(str,sorted_1)))

# #更高效的传参：不用pop函数
# def Merge(A, B):
#     result = []
#     a_index, b_index = 0, 0
#     while a_index < len(A) and b_index < len(B):
#         if A[a_index] <= B[b_index]:
#             result.append(A[a_index])
#             a_index += 1
#         else:
#             result.append(B[b_index])
#             b_index += 1
#     # 将剩余元素添加到结果列表中
#     result.extend(A[a_index:])
#     result.extend(B[b_index:])
#     return result
#
# def MergeSort(A):
#     if len(A) < 2:
#         return A
#     mid = len(A) // 2
#     left = MergeSort(A[:mid])
#     right = MergeSort(A[mid:])
#     return Merge(left, right)
#
# # 读取输入并调用归并排序
# n = int(input())
# a = list(map(int, input().split()))
# sorted_a = MergeSort(a)
# print(' '.join(map(str, sorted_a)))