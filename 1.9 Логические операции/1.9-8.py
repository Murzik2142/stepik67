'''
Найдите результат выражения для заданных значений a и b.
Учитывайте регистр символов при ответе.

a = True
b = False
a and b or not a and not b
'''

a = True
b = False
if ((a and b) or ((not a) and (not b))):
    print("True")
else:
    print("False")
