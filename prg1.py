data = "Guvi Geeks network private Limited"
vowels = ['a','e','i','o','u']
vowelcount=0
count=0
# aindividualcount =0
# eindividualcount=0
# iindividualcount=0
# oindividualcount =0
# uindividualcount=0

for i in range(len(data)):
    if data[i] in vowels:
        vowelcount = vowelcount+1
                                
print("Overall vowel count= ",vowelcount)

#iterating the vowels individually and saving the count and printing it
for vowel in vowels: 
    count = data.count(vowel)
    print(vowel ,":" ,count)




#individual code to get the output

# for i in data:
#     if i=='a':
#         aindividualcount = aindividualcount+1
# print("Number of a in the given word: ",aindividualcount)

# for i in data:
#     if i=='e':
#         eindividualcount = eindividualcount+1
# print("Number of a in the given word: ",eindividualcount)

# for i in data:
#     if i=='i':
#         iindividualcount = iindividualcount+1
# print("Number of a in the given word: ",iindividualcount)

# for i in data:
#     if i=='o':
#         oindividualcount = oindividualcount+1
# print("Number of a in the given word: ",oindividualcount)
# for i in data:
#     if i=='u':
#         uindividualcount = uindividualcount+1
# print("Number of a in the given word: ",uindividualcount)


