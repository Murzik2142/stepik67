s1 = list(map(int, input().split()))
s1.sort()
# print(*s1)
s2 = []
s3 = []
for item in s1:
    if item not in s2:
        s2.append(item)
# print(*s2)
for i in range(len(s2)):
    if s1.count(s2[i]) > 1:
        s3.append(s2[i])
print(*s3)
