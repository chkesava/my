"""
1.write a program in which you take integer input from user if that integer if it is divisible by 3 and 6 print good number if the integer divisible by 2 and 7 then pint a average number
if a integer divisible by 4 or 9 then print aresome number else print bad  number  
"""
a=int(input())
if (a%3==0 and a%6==0):
    print("Good Number")
elif (a%2==0 and a%7==0):
    print("Average Number")
elif(a%4==0 or a%9==0):
    print("Awesome Number")
else:
    print("Bad Number")
