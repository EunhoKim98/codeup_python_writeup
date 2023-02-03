def main():
    a, m, d, n = input().split()
    a = int(a)
    m = int(m)
    d = int(d)
    n = int(n)

    for i in range(1, n):
        a = a * m + d
    print(a)

if __name__ == '__main__':
    main()
