#Լɪ��
#https://www.lanqiao.cn/problems/1111/learning/
n,m,k=map(int,input().split())
a=list(range(1,n+1))
i=k-1
while len(a)!=0:
    i=(i+m-1)%len(a)#����ѭ���Ƚ����ѣ������������Ϳ�����
    print(a.pop(i))
'''
----------------This is the END of the PROGRAM.----------------
'''