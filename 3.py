#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

a=int(input('введите число'))
import random
from re import I
list=[]
for i in range(a):
    list.append(random.uniform(1.5,10.39))
print(list)
#i=0
#diff=0
#result=0
#for i in list:
    #i=i%1
    #print(i)
#print(str(max(i)))
#print(min(i))

min = 1
max = 0
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(max-min)