def star(n):
    for x in range(1, n+1):
        print("*" * x)
    for y in range(n-1, 0, -1):
        print("*" * y)
x=input("Enter number:")
x=int(x)
star(x)
            
