import csv 

class Authentication:
    def Login(self):
        with open('user_reg.csv','r',newline="") as file:
            store=csv.DictReader(file)
            self.userName=input("Enter the username: ")
            self.password=input("enter the password: ")
    
            for each in store:
                print(each)
                if(self.userName== each["user_name"] and self.password== each["password"]):
                    print("Login Success.......")
                    break
                else:
                    print("invalid user Credintials....")
                    self.Login()

    def Registration(self):
        userName=input("enter The user Name: ")
        Password=input("Enter the password:")
        phoneNo=int(input("enter the mobile Number: "))
        eMail=input("Enter the Email id: ")
        City=input("Enter the City Name: ")
        with open('user_reg.csv','a',newline="") as file:
            store=csv.writer(file)
            store.writerow([userName,Password,phoneNo,eMail,City])
            print("registered Successful")
            print("Login Now......")
