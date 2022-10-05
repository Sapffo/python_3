#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

a=int(input('введите число '))
#b=int(input('введите число '))
numbers=list(range(a))
print (numbers)
id=0
i=len(numbers)
sum=0
elem=0
# for elem in numbers:
#     if i%2 !=0:
#         sum=sum+numbers.index(elem)
# print(sum)
for elem in range(0,len(numbers),2):
   #if i%2!=0:
        sum=sum+elem
        elem=elem+1
print(sum)