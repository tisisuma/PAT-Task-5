get_data=input("enter the data :")
print(get_data)
temp=""

vowels =["a","e","i","0","u"]
for i in range (len(get_data)):
    if get_data[i] not in vowels:
        temp = temp +get_data[i]

        
    
       
print(temp)