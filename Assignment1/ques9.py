import random
import string
nums = [random.randrange(1,101) for i in range(5)]
for i in range(5):
    print(nums[i])

#####################################
# randomNumber = random.randint(1,101)
# isPrime=True
# for i in range (2,int(randomNumber**0.5)+1):
#     if randomNumber%i==0:
#         isPrime = False
# if (isPrime):
#     print(f"{randomNumber} is prime")
# else:
#     print(f"{randomNumber} is not prime")

###################################
DiceOutcome = random.randrange(1,7)
print(f"number on the dice is {DiceOutcome}")

##################################
myList =[1,2,3,4,5]
random.shuffle(myList)
print(myList)

#######################
randomFromList = random.choice(myList)
print(randomFromList)

#######################
passwordLength = int(input("Enter length of password: "))
possibleList =string.ascii_letters+string.digits+string.punctuation
password="".join(random.choice(possibleList) for i in range(passwordLength))
print("Your password is: ",password)

############################
rank = ["spades", "hearts", "diamond", "clubs"]
values= [2,3,4,5,6,7,8,9,10,"jack","queen","king", "ace"]
randomCard = random.choice(values) + " of " +random.choice(rank)
print(randomCard)


