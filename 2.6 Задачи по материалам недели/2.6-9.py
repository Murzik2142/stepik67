s = list(map(int, input().split()))
s1 = []
n = int(input())
for i in range(len(s)):
    if n == s[i]:
        s1.append(s.index(n, i))
if len(s1) == 0:
    print("Отсутствует")
else:
    print(*s1)
