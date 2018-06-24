person={'name':'John', 'Age':30, 'Weight':160}
print(person)

print(person.keys())
print(person.values())

person['sex']= 'woman'
print(person)

if 'name' in person:
    print("name exist !")
    
del person['sex']
print(person)
