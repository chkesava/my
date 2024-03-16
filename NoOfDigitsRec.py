#write a recursive function to count the number of digits of a number

def nod(n):
    if n ==0:
        return 0
    return 1+ nod(n//10)
print(nod(12345))
    
    
