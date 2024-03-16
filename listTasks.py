ListInput=list(map(int,input().split()))
#accessing
print(ListInput[2])
print(ListInput[-1])
#slicing
print(ListInput[1:3])
print(ListInput[3:])
print(ListInput[:5])
print(ListInput[:])
print(ListInput[::-1])
#Looping
for i in ListInput:
    print(i)
#Appending
ListInput.append(9)
print(ListInput)
#inserting
ListInput.insert(2,4)
print(ListInput)
#creatingMultiDimentionalList

MultiList=[[1,2,3,4,5,6],[13,12,44,3,55,88]]
#AccessingTHeList
print(MultiList[1][3])
print(MultiList[1][3])
#updating Values
MultiList[1][3]=443
ListInput[3]=3332
print(MultiList)
print(ListInput)