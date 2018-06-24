5
def area_p(h,w):
    list =[]
    list.append(h * w)
    list.append(2*h + 2*w)
    return list

#input().split()
#map(int,    )
#a, b = map(int, input('Enter two int: ').split())
a=int(input("enter 1st integer:"))
b=int(input("enter 2nd integer:"))
print(area_p(a, b))
    
