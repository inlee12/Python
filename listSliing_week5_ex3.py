def select(input_list):
    k = len(input_list)
    out=[]
    for i in range(k):
         if i % 2 == 0:
             out.append(input_list[i])
    return out             

input_list = ["we", "love", "python", "so","much"]
print(select(input_list))

