def main():
    a = [[0]*10 for i in range(10)] #배열 생성

    for i in range(10):     # 배열 입력
        d = input().split()
        for j in range(10):
            a[i][j] = int(d[j])
    check = True
    i, j = 1, 1
    while(check):
        if(i+1 == 10):
            break
        if(a[i][j] == 2):
            a[i][j] = 9
            break
        elif(a[i][j] == 0):
            a[i][j] = 9
            j = j+1
        elif(a[i][j] == 1):
            j = j-1
            i += 1

        
        
    # 출력
    for i in range(10):
        for j in range(10):
            print(a[i][j], end=' ')
        print() 

if __name__ == '__main__':
    main()
