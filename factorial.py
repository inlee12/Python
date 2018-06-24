#edit test
def factorial_for(number):
    result=1
    for k in range(number,1,-1):
        result = result * k
    return result

def factorial_recursive(number):
    if number < 1:
        return 1
    else:
        return number * factorial_recursive(number-1)

i= input("Enter number:")
i= int(i)

y= factorial_for(i)
print("by for ",i,"! = ", y)

y= factorial_recursive(i)
print("by recursive ",i,"! = ", y)
      
