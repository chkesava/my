#Write  a recursive program to print the digits in reverse order

def rev(n):


    if n ==0:
        return 
        
    print(n%10)
    return rev(n//10)
           
rev(12345)