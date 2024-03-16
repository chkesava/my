"""
check it if given year is a leap year or not
1.if year is divisible by 4 and not divisible by 100 or if it is divisible by 400 then it is called as leap year 
"""
year=int(input())
if( (year%4==0 and year%100!=0) or year%400==0):
    print("leap year")
else:
    print("not  a leap year")
