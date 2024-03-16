#Write a recursve fun to calculate the sum of digitd of a number

# def sum(n):
#     s=0
#     if n == 0 :
#         return
#     else:
#         n=n%10
#         s = s+ n
#         n//10
#         return sum(s)
    
# sum(123)

#write a recursive function to count the number of digits of a number

def sod(n):
    if n ==0:
        return 0
    return sod(n//10) 
print(sod(12345))
    