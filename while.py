count=0
while count < 5 :
    print('count = ', count)
    count=count+1
print('the end !')


# use while loops when there is an indeterminate number of iterations

def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n//10
    return n

print(leftmostDigit(72658489290098) == 7)


# eg: find the nth number that is a multiple of either 4 or 7
def isMultipleOf4or7(x):
    return ((x % 4) == 0) or ((x % 7) == 0)

def nthMultipleOf4or7(n):
    found = 0
    guess = -1
    while (found <= n):
        guess += 1
        if (isMultipleOf4or7(guess)):
            found += 1
    return guess

print("Multiples of 4 or 7: ", end="")

for n in range(15):
    print(nthMultipleOf4or7(n), end=" ")
print()
