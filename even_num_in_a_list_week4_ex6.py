def even_number(list):
    even_list=[]
    for item in list:
        if item % 2 == 0 :
           even_list.append(item)
    return even_list

list=[1,2,3,4,5,6]
print(even_number(list))
