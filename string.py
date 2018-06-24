def num(x):
    y=1
    while y < x+1:
        print(str(y)*y)
        y = y+1
    return


i = input("Enter positive int:")
i = int(i)
num(i)
