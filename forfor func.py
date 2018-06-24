def sumfromMtoN(m,n):
       return sum(range(m,n+1))

print(sumfromMtoN(5,10) == 5+6+7+8+9+10)

def sumToN(n):
    total = 0
    for x in range(n+1):
        total += x
    return total

print(sumToN(5) == 0+1+2+3+4+5)



def sumEveryKthFromMToN(m, n, k):
    total = 0
    for x in range(m, n+1, k):
        total += x
    return total

print(sumEveryKthFromMToN(5, 20, 7) == (5 + 12 + 19))



def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(m, n+1):
        if (x % 2 == 1):   # add odd number
            total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))
