def main():
    a, r, n = input().split()
    
    result = int(a)*int(r)**(int(n)-1)
    print(result)

if __name__ == '__main__':
    main()
