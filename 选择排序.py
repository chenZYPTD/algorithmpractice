#选择排序
'''n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    #以a[i]为基准值，在a[i]后且比a[i]小的就直接调换
    for k in range(i,n):#注意，a[n-1]就已经是最后一位了，所以是n为右边的开区间
        if a[k]<a[i]:
            a[k],a[i]=a[i],a[k]

print(' '.join(map(str,a)))'''
# 上面这段代码没有问题，但是为了保险，应标记min_value和min_idx

n = int(input())
a = list(map(int, input().split()))
for i in range(n-1):
    min_value=a[i]
    min_idx=i
    for k in range(i,n):
        if a[k]< min_value:
           min_value=a[k]
           min_idx=k
           a[i],a[min_idx]=a[min_idx],a[i]
print(' '.join(map(str,a)))
# 当您尝试执行 a[i], min_value = min_value, a[i] 这样的交换时，
# 您实际上只是将 min_value 赋值给了 a[i]，    →因此，列表索引的互换才相当于对调列表中的元素
# 而没有将原来 a[i] 的值放到最小值原来的位置。
# 这样一来，列表中的两个元素并没有真正交换位置，而
# 且最小值的原始位置（min_idx）上的值没有被更新，
# 导致排序结果不正确。