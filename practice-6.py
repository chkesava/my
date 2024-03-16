n=int(input())
a=0
b=1
print("1 2",end=" ")
Wholesum=0
c=0
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
