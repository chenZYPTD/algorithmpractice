#栈的运用
#https://www.lanqiao.cn/problems/2490/learning/
#核心：先进后出，只处理栈顶(a[-1),a.append(),a.pop())
#可能的题型：括号匹配问题；表达式求值；递归机制
#括号串问题，左括号入栈，右括号出栈
n=int(input())
s=input()
stack_a=[]
ok=True
for c in s:
    if c=='(':
        stack_a.append(c)
    else:#如果是右括号就出栈
        if len(stack_a)==0:#出现右括号在前，就直接停了
            ok=False
            break
        stack_a.pop()#右括号出栈
#最后栈必须为空，排除左括号落单的情况
if ok and len(stack_a)==0:
    print("Yes")
else:
    print("No")
