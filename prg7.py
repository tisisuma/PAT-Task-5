# Getting string input from the user 
get_data =  input('Enter the string : ')

# Finding the maximum frequency character of the string 
temp = {}
for i in get_data:
    if i in temp:
        temp[i] += 1
    else:
        temp[i] = 1

# Printing values 
print("Entered String is ", get_data)
print(temp)



