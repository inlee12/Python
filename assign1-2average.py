def average(x) :
    tot = 0
    cnt=0
    for i in  x:
        tot+= i
        cnt=cnt+1
    return tot/cnt

x=[1,3,5,7,9,11]
print(average(x))
        
