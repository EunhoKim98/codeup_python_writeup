a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not(a or b))   # not (a or b) == not(a) and not(b)