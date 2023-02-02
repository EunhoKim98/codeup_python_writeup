def main():
    a = int(input())
    sum = 0
    for i in range(0, a):
        sum += i
        if sum >= a:
            break
    print(i)

    
if __name__ == '__main__':
    main()
