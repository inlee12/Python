def even_number(s_list):
    even_n=[]
    for item in s_list:
        if item % 2 == 0 :
            even_n.append(item)
    return even_n

s_list=[1,2,3,4,5,6]
print(even_number(s_list))
