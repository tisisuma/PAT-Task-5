data = "umamaheswari"
print(data)
temp = [] # blank list
count=0
for i in range(len(data)):
    if data[i] not in temp:
        temp.append(data[i])
        count= count+1

    
for i in range(len(temp)):
    print(temp[i], end=" ")
print("\n")

print("Number of Unique Characters :",count)