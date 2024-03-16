class Authentication:
    def Login(self):
        flag=True
        while flag:
            self.userName=input("Enter the Username: ")
            self.Password=input("Enter The Password: ")
            if(self.userName==self.Password):
                print("Login Success Proceed to next")
                break
            print("invalid user details enter again!")
