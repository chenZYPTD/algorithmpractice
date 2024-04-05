#插入排序，authentic
n = int(input())
nums = list(map(int, input().split()))

for i in range(1, n):#我们默认第一个元素是被排序的，因此后面在排的时候，前面的已经默认排了，
                     #因此不会出现前面有2个比目标数字更大的数字。
    j = i - 1        #从后往前比，如果前面的比选取的这个更大那么就把前面的集体向后挪，直到这个存在没有
    current_num = nums[i]
    while j >= 0 and nums[j] > current_num:#如果current_num前面出现了更大的项，那就向后挪一格，相当于交换
        nums[j + 1] = nums[j]              #由于前面已经是排序好了的，所以就算前面所有数字都比current_num大，
        j = j - 1                          #也可以随着j变小被一个一个往后挪。

    nums[j + 1] = current_num  #最后，将 current_num 插入到正确的位置上，这个位置就是 j + 1(即nums[i])
print(' '.join(map(str,nums)))

# #插入排序(待分析)
# n=int(input())
# a=list(map(eval,input().split(' ')))#对于第i个数字，在区间[0,i-1]中从后往前找对应插入的位置
# for i in range(1,n):
#                          '''此时我们先认为第一位是排好的，
#                          若后面存在比第一位更小的数字（设其为a[k]），
#                          让a[0:k]全部往后挪一位即可(整体挪)'''
# value=a[i]
# insert_idx=0
# for j in range(i-1,-1,-1):
#     if a[j]>value:
#     #往后挪
#         a[j+1]=a[j]
#     else:
#         insert_idx=j+1
#     a[insert_idx]=value#更新最小值序列和其对应的索引
# print(' '.join(map(str,a)))

