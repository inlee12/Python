def non_even(x):
    tot =0
    for k in x:
        if k%2 != 0:
            tot += k
    return tot

x=[2,4,6,7,9]
print(non_even(x))
