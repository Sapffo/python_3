#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

numbers = [1, 2, 3, 4, 5, 6, 9,11]
i =1
j = -2
for x in numbers:
    if i < len(numbers)/ 2 + 1:
        slice = numbers[:i]
        slice2 = numbers[j:]
        res = slice[i - 1] * slice2[j + 1]
        i+=1
        j-=1
        print(res)