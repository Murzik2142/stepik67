s = str(input())
if s == "треугольник":
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2
    print(float((p * (p-a) * (p-b) * (p-c)) ** 0.5))
elif s == "прямоугольник":
    x, y = int(input()), int(input())
    print(float(x * y))
elif s == "круг":
    r = int(input())
    print(float(3.14 * (r ** 2)))
