s = input()
s += " "
tmp = ""
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        tmp = tmp + s[i-1]
    elif tmp != "":
        print(s[i-1], len(tmp)+1, sep="", end="")
        tmp = ""
    else:
        print(s[i-1], "1", sep="", end="")
print()
