'''
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками.
Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.
'''

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print("\t", end="")
for i in range(c, d+1):
    if i == c:
        for x in range(c, d+1):
            print(x, "\t", end="")
        print("")
        for j in range(a, b+1):
            print(j, "\t", end="")
            for x in range(c, d+1):
                print(x * j, end="\t")
            print("")
