def main():
    r = int(input())
    sum, i = 0, 1

    for i in range(1, r+1):
        if i % 3 == 0:
            continue
        print(i, end=' ')

if __name__ == '__main__':
    main()
