ptr = open("text.txt","w")
ptr.write("hello, how are you?")
ptr.close()

ptr = open("text.txt","r")
print(ptr.read())
ptr.close()

#############################
ptr = open("text.txt","a")
ptr.write("\nWhat is your name?")
ptr.close()

ptr = open("text.txt","r")
print(ptr.read())
ptr.close()

############################
ptr = open("text.txt","r")
print(len(ptr.readlines()))
ptr.close()





