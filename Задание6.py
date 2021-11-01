print('Введите значение N от 1 до 100')
N=int(input())
if (N>=5) and(N<21):
    print(N,'Лет')
if(N%10==1) and((N<5) or(N>20)):
    print(N,'Год')
if(N%10>1) and(N%10<5) and((N<5) or(N>20)):
    print(N,'Года')
if((N%10==0) or(N%10>5)) and((N<5) or(N>20)):
    print(N,'Лет')
