def find_n_letter_words(x, n):
    words=x.split()
    count =0
    for word in words:
        if len(word) == n:
            count=count+1
    return count

test_str = input("Enter string: ")
for k in range(1,11):
    x= find_n_letter_words(test_str, k)
    print("There are", x,"words with",k,"characters.")
