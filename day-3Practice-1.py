"""
write a function which takes 2 parameters a and b typecast the value of second argument into integer
then multiply the both the both arguments and print the last digit of result
"""

def PrintLastDigit(a,b):
    b=int(b)
    Mul=a*b
    lastDigit=Mul%10
    print(lastDigit)

def KeyWordArguments(a,b):
    b=int(b)
    mul=a*b
    lastDigit=mul%10
    print(lastDigit)
def PersonDetails(name="kesava",dept="information technology"):
    print("My Name is",name,"Department of",dept)
def addingNumbers(**numbers):
    length=len(numbers)
    print(length)
PrintLastDigit(2,3.5)
KeyWordArguments(b=45.33,a=33)

PersonDetails()
addingNumbers(first=223,second=2334,third=334)
