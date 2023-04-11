tp = int(input())

if tp < 0:
    print('Ошибка, введите положительное число')
elif tp % 10 == 1 and tp % 100 != 11:
    print(tp, 'программист')
elif tp % 10 >= 2 and tp % 10 <= 4 and (tp % 100 < 10 or tp % 100 > 20):
    print(tp, 'программиста')
else:
    print(tp, 'программистов')
