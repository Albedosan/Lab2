#Вариант 4 задание 2
print('Введите значение числа N от 1 до 9')
N=int(input())
if(N<1) or (N>9):
    print('Число N должно быть больше 0 и меньше 10')
else:
    for i in range(10,100):
        if(i%N==0):
            print(i)
