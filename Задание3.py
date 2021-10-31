def f(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    else:
        return f(n-1)+f(n-2)
def F(n):
    s=0
    while n>0:
        s+=1
        n=n//10
    return s
k=0
for i in range(1000000):
    r=f(i)
    if(F(r)==4):
        k+=1
    if(F(r)>4):
        break
print(k)




