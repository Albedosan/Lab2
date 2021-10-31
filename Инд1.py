#Вариант 4 задание 1
print(' введите количество секунд')
c=int(input())
print('введите количество минут')
m=int(input())
while c>60:
    c=c-60
    m+=1
if(c<10):
    c=str(c)
    c='0'+c
else:
    c=str(c)
if(m<10):
    m=str(m)
    m='0'+m
else:
    m=str(m)
s=m+':'+c
print(s)

