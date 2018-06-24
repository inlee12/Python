from my_math import *

#a = input("Enter integer 1:")
#b = input("Enter integer 2:")
#a= int(a)
#b= int(b)

x= map(int, input().split())
a, b = x

print("a = ",a,"b = ",b)
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(mod(a,b))
