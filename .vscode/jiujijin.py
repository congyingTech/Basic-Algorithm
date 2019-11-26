def go(p, d, t, n, a):
    while t:
        while True:
            p = (p+d+n)%n
            if a[p]!=-1:
                break
        t -= 1
    return p

if __name__ ==  "__main__":
    n = 10
    k = 4
    m = 3
    a = [i for i in range(n)]
    left = n
    p1 = 0
    p2 = n-1
    while left:
        p1 = go(p1, 1, k, n, a)
        p2 = go(p2, -1, m, n, a)
        left -= 1
        if p1 != p2:
            left -= 1
        a[p1]=a[p2]=-1
        print("p1:", p1)
        print("p2:", p2)


    
    