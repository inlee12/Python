def u(v) :
    f=[0,0,0]
    n =  (v[0]**2 + v[1]**2 + v[2]**2)**(1/2)
    f[0] =v[0]/n
    f[1] =v[1]/n
    f[2] =v[2]/n
    return f

vector = [2, 3, -4]
print(u(vector))
