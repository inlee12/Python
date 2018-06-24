def f_max(x) :
    m =x[0]
    for a in  x:
        if( a > m ):
           m = a
    return m

x=[1,3,5,7,9,11]
print(f_max(x))
        
