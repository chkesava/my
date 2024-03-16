"""
list=[-1,42,65,1,-4,6,-66]
wrie a program to find the second smallest negative number in the list

"""
list_A=[-1,42,65,1,-4,6]
smallest_num1=0
smallest_num2=0
for i in list_A:
    if(i<smallest_num1):
        smallest_num2=smallest_num1
        smallest_num1=i
        
    else:
        continue
print(smallest_num2)
