def main():
    # 입력
    d = [[0]*20 for i in range(20)]
    for i in range(19):
        a = input().split()
        for j in range(19):
            d[i][j] = int(a[j])

    n = int(input())
    for i in range(n):
        x, y = input().split()
        x = int(x) -1
        y = int(y) -1
        for j in range(19):    
            if d[j][y] == 1:
                d[j][y] = 0
            else:
                d[j][y] = 1
            
            if d[x][j] == 1:
                d[x][j] = 0
            else:
                d[x][j] = 1

    # 출력
    for i in range(19):
        for j in range(19):
            print(d[i][j], end=' ')
        print() 

if __name__ == '__main__':
    main()
