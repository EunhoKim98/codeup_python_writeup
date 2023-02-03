def main():
    r = int(input())
    sum, i = 0, 1

    while(True):
        sum = sum + i
        if sum >= r:
            print(sum)
            break
        i += 1

if __name__ == '__main__':
    main()
