string1 = "hello how are you?"
count =0
vowels="aeiouAEIOU"
for i in range (0 ,len(string1)):
    if(string1[i] in vowels ):
        count+=1
print("number of vowels are: ",count)

############################
string1=string1[::-1]
print(string1)

#######################
myStr = input("Enter a string: ")
if(myStr==myStr[::-1]):
    print("string is palindrome")
else:
    print("string is not a palindrome")