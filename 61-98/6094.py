def main():
    n = int(input())
    a = input().split()
    min = int(a[0])
    for i in range(1,n):
        if int(a[i]) < min:
            min = int(a[i])

    print(min)
if __name__ == '__main__':
    main()

