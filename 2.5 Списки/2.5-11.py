s = list(map(int, input().split()))
if len(s) == 1:
    print(s[0])
else:
    for i in range(len(s) - 1):
        print(s[i + 1] + s[i - 1], end=" ")
    print(s[-2] + s[0])
