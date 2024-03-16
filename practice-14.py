"""
take a number input from user check if the sum of factors of that number is greater than the original number or not if yes print yes if not print No
"""
n=int(input("enter the number:"))
sumOfFActors=0
for i in range(1,(n//2)+1):
    if(n%i==0):
        sumOfFActors=sumOfFActors+i
if(sumOfFActors>n):
    print("Abundant")
else:
    print("Not a Abundant")