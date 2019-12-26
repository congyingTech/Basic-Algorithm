# encoding:utf-8

def findNfibonacciNumber(n):
    fibo_l = [0]*(n+1)
    fibo_l[0]=0
    fibo_l[1]=1

    for i in range(2, n+1):
        fibo_l[i] = fibo_l[i-1] + fibo_l[i-2]
    
    return fibo_l[-1]


if __name__ == "__main__":
    findNfibonacciNumber(3)