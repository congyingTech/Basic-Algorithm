
for i in range(1001):
    sum = 0
    for j in range(i+1,1001):
        sum += j
        if sum == 1000:
            print(range(i,j+1))
        if sum > 1000:
            break



