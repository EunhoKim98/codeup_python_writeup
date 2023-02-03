def main():
    n = int(input())
    d = [[0]*20 for i in range(20)]
    for i in range(n):
        x, y = input().split()
        if d[int(x)][int(y)] == 1:
            continue
        d[int(x)][int(y)] += 1

    for i in range(1, 20):
        for j in range(1, 20):
            print(d[i][j], end=' ')
        print() 

if __name__ == '__main__':
    main()
