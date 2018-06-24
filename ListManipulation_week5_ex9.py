def divisor(k):
    data=[]
    for i in range(2,k+1):
        if k % i == 0:
             data.append(i)
    return data

k =input()
k =int(k, 10)
print(divisor(k))


