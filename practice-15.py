x=int(input())
sumOfNumbers=0
multipicationOFNumbers=1
CountOfNumbers=0
while(x>=1):
    r=x%10
    print(r)
    x=x//10
    sumOfNumbers=sumOfNumbers+r
    CountOfNumbers=CountOfNumbers+1
    multipicationOFNumbers=multipicationOFNumbers*r
print("count",CountOfNumbers)
print("MultiplyOfNumbers:",multipicationOFNumbers)
print("Sum of Num:",sumOfNumbers)