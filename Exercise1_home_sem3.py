'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

'''
n = int(input("Enter the number of elements: "))   # вводим количество элементов в списке
list=[]

import random
for i in range(n):                                 # задаем и запольняем случайними целими числами список 
    a = random.randint(1, 9)
    list.append(a)  #list+=[a]
print(f"list = {list}", end="")

sum=0                                               # считаем сумму элементов списка-на нечетных позициях
for i in range(n):
    if i%2!=0:
        sum = sum + list[i]
print(f" -> {sum}")

