"""
calculate the vale of seven factorial using for loop
"""

n=int(input("enter the number:"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)
