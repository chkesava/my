from Login_Reg import *

class Main_Class:
    def Application_initializer(self):
        self.isLogined=False
        print("Welcome To Ecommerce Website")
        LoginInstance=Authentication()
        while True:
            print("1.Login")
            print("2.Register")
            print("3.Products")
            print("4.user Info")
            print("5.exit")
            self.userChoice=int(input("Enter your choice: "))
            if(self.userChoice==1):
                LoginInstance.Login()
            elif(self.userChoice==2):
                LoginInstance.Registration()
                LoginInstance.Login()
ob1=Main_Class()
ob1.Application_initializer()


