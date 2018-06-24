def min_in_list(list):
    min= list[0]
    for a in list:
        if a < min:
            min = a
    return min
    

list=[10, 15, 20, 49, 8, 34]
print(min_in_list(list))
