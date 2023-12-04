def LongestSubString(s1,s2):
    temp = 0
    temp1 =len(s2)
    while(temp<temp1):
        if(s2[temp] not in s1):
            temp = temp+1
        else:
            if(s2[temp:temp1] not in s1):
                temp1 = temp1 - 1
            else:
                return(s2[temp:temp1])

s1 = "umalovescoffee"
s2 = "umalovesrosemilk"
print(LongestSubString(s1,s2))