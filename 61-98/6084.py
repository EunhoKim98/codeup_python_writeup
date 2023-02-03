def main():
    h, b, c, s = input().split()
    a = int(h) * int(b) * int(c) * int(s)
    mg = round(a/8/1024/1024, 1)
    print(mg, end=' MB')

if __name__ == '__main__':
    main()
