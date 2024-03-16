MyList=[12,42,23,96,7,18,10,133]
print(MyList)
#addition of min and max 
minNum=MyList[0]
maxNum=MyList[0]
minId=0
maxId=0
for i in range(len(MyList)):
    if(minNum>MyList[i]):
        minNum=MyList[i]
        minId=i
    if(maxNum<MyList[i]):
        maxNum=MyList[i]
        maxId=i
s=minNum+maxNum
d=maxNum-minNum
MyList[minId]=d
MyList[maxId]=s
print(MyList)