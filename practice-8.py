#calculate the sum of the digits of the number which the the input is taken from the user
n=int(input())
sum=0
while n!=0:
    temp=n%10
    sum=sum+temp
    n=int(n/10)
print(sum)