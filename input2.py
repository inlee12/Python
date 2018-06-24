def printNumberTriangle(x):
    for y in range(1, x+1):
        z=y;
        for w in range(z,0,-1):
            print(w, end="")
        print()

x = int(input("Enter a number: "))
printNumberTriangle(x)

