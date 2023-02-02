a, b, c = input().split()
a = a if(int(a) < int(b)) else b
a = a if(int(a) < int(c)) else c
print(int(a))
   