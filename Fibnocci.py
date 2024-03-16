
#fibnocci

def fabinoci(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    return fabinoci(n-2)+fabinoci(n-1)
res=fabinoci(5)
print(res)