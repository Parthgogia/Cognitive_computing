myList=[1,34,32,13,2]
print(max(myList))
print(min(myList))

########################
myDict = {1:"rahul",2:"sneha", 3:"ishan"}
key = int (input("Enter key to search: "))
if key in myDict:
    print(myDict[key])
else:
    print("key not present")

########################
myList.sort()
for i in range(0,len(myList)):
    print(myList[i])

myList.sort(reverse=True)
for i in range(0,len(myList)):
    print(myList[i])

##########################
myDict2 = {4: "harry" , 5: "sahil"}
myDict.update(myDict2)
print(myDict2)