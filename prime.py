i = 3
while(i < 21):  #until 20
    j = 2
    while(j <= (i/j)):
        if not(i%j): 
            print('%d is %d * %d' %(i, j, i/j))
            break
        j = j + 1
    if (j > i/j):
        print(i, " is prime")
    i = i + 1
print('The end')
