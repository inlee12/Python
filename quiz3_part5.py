def perfect_n(n):
    tot = 0
    for k in range(1,n):
        if n % k == 0:
            tot=tot+k
    if tot == n:
        return True
    else: 
        return False

x=input()
x=int(x)
print(perfect_n(x))


                
                
                
                
        
