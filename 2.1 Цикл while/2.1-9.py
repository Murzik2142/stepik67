i = 0
j = 0
while i < 5:
    print('*')
    j += 1
    if i % 2 == 0:
        print('**')
        j += 2
    if i > 2:
        print('***')
        j += 3
    i = i + 1
print(j)
