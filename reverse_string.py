def rev_str1(x):
    out_s=""
    for c in x:
        out_s= c + out_s 
    return out_s

def rev_str2(x):
    out_s=""
    for k in range(len(x)-1,-1,-1):
        out_s=out_s+ x[k]
    return out_s

if __name__ == "__main__":
    test_str=input("Enter a string:")
    result_str=rev_str2(test_str)
    print(result_str)
