def main():
    r, g, b = input().split()
    a = int(r) * int(g) * int(b)
    mg = round(a/8/1024/1024, 4)
    print('{:.2f}'.format(mg), end=' MB')

if __name__ == '__main__':
    main()
