"""
write   a login function which accepts the user only when the username and password are same and displays the message login sucessfull
otherwise it keeps asking the user to enter the credincials untill it was correct
"""
def CheckUserNameAndPassword():
    flag=0    
    while flag==0:
        userName=input("enter the userName:")
        Password=input("enter the password:")
        if(userName==Password):
            flag=1
            print("Login Sucess")
            break
        print("Login failed")
        print("Enter details again")
CheckUserNameAndPassword()
