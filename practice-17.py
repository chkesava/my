n=1578
numf=n
count=0
sumOfSquares=0
while n>0:
    count=count+1
    n=n//10

n=numf
while n>0:
    digit=n%10
    sumOfSquares=sumOfSquares+digit**count
    n=n//10
    count=count-1
print(sumOfSquares)