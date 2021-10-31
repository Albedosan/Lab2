def f(n):
    fact=1
    while n>1:
        fact=fact*n
        n=n-1
    return fact
print('введите значение переменной x')
x=int(input())
print('введите значение переменной q')
q=float(input())
s=1
p=2
for i in range(10000000000000000000000):
    per=(x**p)/f(p)
    if(abs(per)<q):
        break
    else:
        if(i%2==0):
            s=s-per
        else:
            s=s+per
print(s)




