'''
Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:
если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.

n = int(input())
while n <= 100:
    if n>= 10:
        print(n)
    n = int(input())

'''
n = 0
s = []
while n <= 100:
    if n >= 10:
        s.append(n)
    n = int(input())
for i in range(0, len(s)):
    print(s[i])
