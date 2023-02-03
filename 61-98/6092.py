def main():
    n = int(input())
    a = input().split()
    d = [0 for i in range(24)]
    
    for i in range(len(a)):
        d[int(a[i])] += 1
    
    for i in range(1,24):
        print(d[i], end=' ')
    

if __name__ == '__main__':
    main()
