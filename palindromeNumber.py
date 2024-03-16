n=int(input())
dummyVal=n
sumOfDigits=0
while n>=0:
    rem=n%10
    sumOfDigits=sumOfDigits*10+rem
    n=n//10
print(sumOfDigits)
if(sumOfDigits==dummyVal):
    print("Palindrome")
else:
    print("Not a Palindrome")