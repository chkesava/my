n=int(input())
x=n
digit=0
sumOfdigits=0
while(x>0):
    digit=x%10
    x=x//10
    sumOfdigits=sumOfdigits+digit
if(n%sumOfdigits==0):
    print("divisible")
else:
    print("not divisible")