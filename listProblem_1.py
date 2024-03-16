mylist=[2,0,1024,0,40,230,0]
numlist=[]
z=0
for i in mylist:
    if(i==0):
        z+=1
    else:
        numlist+=[i]
for j in range(z):
    numlist+=[0]
print(numlist)
        
            
            
            
