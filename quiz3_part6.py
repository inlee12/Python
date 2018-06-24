def prime(x):
    if x == 0 or x == 1:
        return False
    for n in range(2,x):
        if x % n == 0:
            return False
    return True

x= input()
x= int(x)
print(prime(x))
