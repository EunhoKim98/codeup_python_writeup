def gcd(a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    return a*b / gcd(a,b)

def main():
    a, m, d = input().split()
    a = int(a)
    m = int(m)
    d = int(d)
    result = lcm(a, m)
    result = int(lcm(result, d))
    print(result)

if __name__ == '__main__':
    main()
