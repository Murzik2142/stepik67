n = int(input())
s = []
for i in range (0,n):
    for j in range (i):
        s.append(i)
if n == 0:
    print()
elif n == 1:
    print("1")
elif n == 2:
    print("1 2")
else:
    print(*s[:n])