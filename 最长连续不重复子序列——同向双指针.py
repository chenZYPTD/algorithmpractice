#最长连续不重复子序列——同向双指针
#https://www.acwing.com/problem/content/801/
#包括超长数列的建立和运用
n=int(input())
a=list(map(int,input().split()))
i,j=0,0
max_num=0
count=[0]*100010
while i < n:#反向扫描说不清楚要左挪还是右挪，可能错过了最大，试试同向扫描
     count[a[i]]+=1#count列表这样的用法就是记录原列表某一位的值的重复次数
     while count[a[i]]>1:
         count[a[j]] -= 1  # 因为区间缩小了，所以j从左往右来的时候经过的那些东西就要没了（当然，这些东西i也是经过了的）
         j+=1#注意这上下两行不要写反了，j在这里已经不是原来的j了
     max_num=max(max_num,i-j+1)
     i+=1#注意这上下两行不要写反了，i在这里已经不是原来我们要的i了(不放心的话用for 循环也可以)
print(max_num)