from math import sin, cos

def calculate(x):
    y= sin(x) - cos(x) + sin(x) * cos(x)
    return y

x= int(input("Enter int :"), 10)
print(calculate(x))
    
