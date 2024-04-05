#汉诺塔问题的递归
#程序目的，显示移动的过程，从哪里挪到哪里的
def Move(n,A,B,C):#表示n的盘子通过B移动到C
    if n==0:
        return None
    Move(n-1,A,C,B)
    print("{}→{}".format(A,C))#第n个盘子从A挪到C
    Move(n-1,B,A,C)
Move(5,'A','B','C')#里面是字符串，不要写成变量