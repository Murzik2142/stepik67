a = [1, 2, 3]
b = a
# значения списка b?
print(*b, end="")
print("; ", end="")
a[1] = 10
# значения списка b?
print(*b, end="")
print("; ", end="")
b[0] = 20
# значения списка a?
print(*a, end="")
print("; ", end="")
a = [5, 6]
# значения списка b?
print(*b, end=" ")
