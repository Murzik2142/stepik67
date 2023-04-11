x, y, z = float(input()), float(input()), str(input())
if (z == "/" and y == 0) or (z == "mod" and y == 0) or (z == "div" and y == 0):
    print("Деление на 0!")
elif z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "/":
    print(x / y)
elif z == "*":
    print(x * y)
elif z == "mod":
    print(x % y)
elif z == "pow":
    print(x ** y)
elif z == "div":
    print(x // y)
