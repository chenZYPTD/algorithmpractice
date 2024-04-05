#https://www.lanqiao.cn/problems/3194/learning/
s=input()
# while '5'in s and '7' in s and '9' in s:#字符串replace函数是全部替换。列表中的那个是remove函数
s=s.replace('5','')#replace字符串可以用。记住：字符串处理函数侧重于“子串”，列表处理函数侧重于“索引”
s=s.replace('7','')#replace里面一定有两个元素
s=s.replace('9','6')#注意要赋值，这不是列表
#配对问题（如之前的括号）用栈来模拟
a=[]#因为栈是要加东西的，所以不用[0]*N
s=list(s)#字符串就不能往后加东西了，此处转成列表
for i,c in enumerate(s):
    if c=='3':
        a.append(i)
    elif c=='4' and len(a)!=0:#出栈，要求栈非空。之后很多题出栈的条件是不同的，要分情况讨论。
        idx=a.pop()
        s[i],s[idx]=s[idx],s[i]#34对调
print(''.join(s))