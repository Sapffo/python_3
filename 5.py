#.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
a=int(input('введите число'))
b=int(input('введите число'))

f3=1
f1=0
f2=1
for i in range(a):
    f1,f2=f2,f1+f2
   #f1,f3=f3,f1-f3
    print(f2)
    #print(f3)
for j in range (b):
    f1,f3=f3,f1-f3
    print(f3)
