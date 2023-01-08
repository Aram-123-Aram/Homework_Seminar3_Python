'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
a = int(input("Enter the number: a= "))
print(end="-> ")

text=""
while a/2!=0:
    text=text+str(a%2)
    a=a//2
    
for x in reversed(text):
    print(x, end="")