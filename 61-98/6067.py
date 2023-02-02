def check(a):
    if int(a) < 0:
        if int(a) % 2 == 0:
            print('A')
        else:
            print('B')
    else:
        if int(a) % 2 == 0:
            print('C')
        else:
            print('D')

def main():
    a = input()
    check(a)
 

if __name__ == '__main__':
    main()