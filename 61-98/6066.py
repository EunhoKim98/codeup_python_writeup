def check(a):
    if int(a) % 2 == 0:
        print('even')
    else:
        print('odd')

a, b, c = input().split()
check(a)
check(b)
check(c)
