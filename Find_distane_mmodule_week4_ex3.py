import math
def distance(x, y):
    z1=y[0]-x[0]
    z2=y[1]-x[1]
    z3=y[2]-x[2]
    d = math.sqrt(z1**2+z2**2+z3**2)
    return d
a=[2,3,-5]
b=[4,-3,12]
print(distance(a,b))
