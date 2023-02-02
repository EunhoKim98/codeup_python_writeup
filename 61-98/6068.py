def check(a):
    if a >= 90:
        print('A')
    elif a >= 70:
        print('B')
    elif a >= 40:
        print('C')
    else:
        print('D')

def main():
    a = input()
    check(int(a))
 

if __name__ == '__main__':
    main()