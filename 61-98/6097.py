def main():
    # 입력
    h, w = input().split()
    h, w = int(h), int(w) #세로, 가로 초기화
    a = [[0]*w for i in range(h)] #배열 생성

    n = int(input())
    for i in range(n):
        l, d, x, y = input().split()
        l, d, x, y = int(l), int(d), int(x)-1, int(y)-1
        for j in range(l):
            if d == 0:
                a[x][j+y] = 1
            else:
                a[x+j][y] = 1


    # 출력
    for i in range(h):
        for j in range(w):
            print(a[i][j], end=' ')
        print() 

if __name__ == '__main__':
    main()

