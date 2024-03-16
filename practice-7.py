num=int(input("enter the number:"))
count=0
for i in range(2,num):  
    if(num%2==0):
        count=1
        break
if(count):
    print("Not a prime Number")
else:
    print("Prime Number")