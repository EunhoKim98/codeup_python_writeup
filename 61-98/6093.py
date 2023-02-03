def main():
    n = int(input())
    a = input().split()

    for i in range(n-1,-1,-1):
        print(int(a[i]), end=' ')
    

if __name__ == '__main__':
    main()

