a, b, h = int(input()), int(input()), int(input())
if a <= h <= b:
    print("Это нормально")
elif h < a:
    print("Недосып")
elif h > b:
    print("Пересып")
