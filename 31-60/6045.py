a, b, c= input().split()
sum = int(a) + int(b) + int(c)
avg = round(sum/3, 3)
print(str(sum) + ' {:.2f}'.format(avg))