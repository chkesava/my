"""
calculate the difference of sum of numbers that are divisible by 6 and not divisible by 6 in the range of first 30 numbers 
"""
n=30
sumOfDigitsDivisibleBy6=0
sumOfDigitsNotDivisibleBy6=0
difference=0
for i in range(1,n+1):
    if(i%6==0):
        sumOfDigitsDivisibleBy6=sumOfDigitsDivisibleBy6+i
    else:
        sumOfDigitsNotDivisibleBy6=sumOfDigitsNotDivisibleBy6+i
if(sumOfDigitsDivisibleBy6>sumOfDigitsNotDivisibleBy6):
    difference=sumOfDigitsDivisibleBy6-sumOfDigitsNotDivisibleBy6
else:
    difference=sumOfDigitsNotDivisibleBy6-sumOfDigitsDivisibleBy6
print(difference)