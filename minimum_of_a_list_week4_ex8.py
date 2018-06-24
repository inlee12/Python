def min_in_list(list):
    low = list[0]
    for a in list:
        if a < low:
            low = a
    return low
    

list=[10, 15, 20, 49, 8, 34]
print(min_in_list(list))
