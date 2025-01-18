import sys
n = len(sys.argv)

print("No of arguments passed : ", n)

sum=0

for i in range(1,n):
    sum+=int(sys.argv[i])

print("sum of numbers given is : ",sum)