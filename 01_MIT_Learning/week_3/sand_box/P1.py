# Write a program that counts up the number of vowels contained
# in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 


vowels = ['a', 'e', 'i', 'o', 'u']
s = "azcbobobegghakl"

count = 0
for i in s:
    if i in vowels:
        count +=1 

print ("Number of vowels:", count)


