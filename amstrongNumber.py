n=153
numf=n
count=0
sumOfSquares=0
while n>0:
    count=count+1
    n=n//10
print(count)
n=numf
print(n)
while n>0:
    digit=n%10
    sumOfSquares=sumOfSquares+digit**count
    n=n//10
if(numf==sumOfSquares):
    print("amstrong Number")
else:
    print("not a amstrong number")