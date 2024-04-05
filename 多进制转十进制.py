#进制的转换+字典的使用
#代码作用，将k进制的数x转换为十进制


dec_to_char="01234567989ABCDEF"
char_to_decimal={}
for idx,chr in (enumerate(dec_to_char)):
    char_to_decimal[chr]=idx
def k_to_decimal(k,x):
    ans=0
    x=str(x)[::-1]#我们这里倒着来
    for i in range(len(x)):
        ans=ans+char_to_decimal[x[i]]*(k**i)#此处的char_to_decimal[x[i]]调用的就是后面的那个键值了
    return ans
k=8
x=3506
print(k_to_decimal(k,x))


dec_to_char="01234567989ABCDEF"
char_to_decimal={}
for idx,chr in (enumerate(dec_to_char)):
    char_to_decimal[chr]=idx
def f(k,x):
    ans=0
    for char in x:
        ans =ans *k +char_to_decimal[char]