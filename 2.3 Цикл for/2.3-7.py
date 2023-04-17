a, b = int(input()), int(input())
s1 = 0
s2 = 0
for i in range(a, b+1):
    if i % 3 == 0:
        s1 += i
        s2 += 1
print(s1/s2)
