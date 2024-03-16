"""
write a function to calculate teh sum of first and last digit of a number
the number take as a argument 
"""
def SumOfFirstAndLastDigits(number):
    lastDigit=number%10
    while number>10:
        number=number//10
    lastDigit=number%10
    print(number+lastDigit)    
SumOfFirstAndLastDigits(222)
