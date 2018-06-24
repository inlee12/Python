import math 
def func_(x):
    y = abs(x**3) + math.cos(math.sqrt(3*x))
    return y

x=int(input("Enter int :"),10)
print(func_(x))
    
