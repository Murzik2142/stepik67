'''
n = int(input())
if ((n // 100000) + (n // 10000) + (n // 1000 % 10)) ==\
      ((n % 1000 // 100) + ((n % 100 // 10)) + (n % 10)):
    print("Счастливый")
else:
    print("Обычный")

'''
x1, x2, x3, y1, y2, y3 = input()
if (int(x1) + int(x2) + int(x3)) == (int(y1) + int(y2) + int(y3)):
    print("Счастливый")
else:
    print("Обычный")
