def printStar(x):
    for i in range(x):
        for j in range(i+1):
            print('*',end="")
        print()

x = int(input("Enter a number: "))
printStar(x)
    
