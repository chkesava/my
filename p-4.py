"""
create a class ticket which will be the abstract class in  isde that create a function book ticket which will be 
the absstract method as nothing in it.
create a  class makeMyTrip witch will use the bookTicket function from ticket class to take the details such as name,
phoneNo,emailId,JourneyDate,and display a message saying tankyou for booking from make myTrip.
create a class irctc which uses the ticketBook of ticket class and take the same details as make my trip but in the end it give a 
option to user select weather one way or round trip.if the user option is round trip it again ask the user to return return date
as well and then print the message thank you for choosing irctc 
create a class indigo which takes inputs as irctc and just asks which mode of transport you are to go in train ,plane,bus 

"""

from abc import ABC,abstractmethod

class Ticket(ABC):
    @abstractmethod
    def BookTicket(self):
        pass

class MakeMyTrip(Ticket):
    def BookTicket(self):
        print("Welcome to MakeMyTrip")
        self.Name=input("Enter The Name: ")
        self.PhoneNo=input("Enter the Mobile No: ")
        self.EmailId=input("Enter the email Id: ")
        self.JourneyDate=input("Enter the Start Date")
        if(self.Name!="" and self.EmailId!="" and self.PhoneNo!=""):
            print("Thanks For Booking From MakeMyTrip")
        else:
            print("Invalid Enter Again!")
            self.BookTicket()
class IRCTC(Ticket):
    def BookTicket(self):
        print("welcome to IRCTC")
        self.Name=input("Enter The Name: ")
        self.PhoneNo=input("Enter the Mobile No: ")
        self.EmailId=input("Enter the email Id: ")
        self.JourneyDate=input("Enter the Start Date")
        self.TypeOfTrip=input("Enter the Trip type(round/oneway): ")
        if(self.Name!="" and self.EmailId!="" and self.PhoneNo!=""):
            if(self.TypeOfTrip=="round"):
                self.ReturnDate=input("Return Date: ")
                if(self.ReturnDate!=""):
                    print("Thanks For Booking From IRCTC")
                    return
            else:
                print("Thanks For Booking From IRCTC")
        else:
            print("Invalid Enter Again!")
            self.BookTicket()
class Indigo(Ticket):
    def BookTicket(self):
        print("Welcome to Indigo")
        self.Name=input("Enter The Name: ")
        self.PhoneNo=input("Enter the Mobile No: ")
        self.EmailId=input("Enter the email Id: ")
        self.JourneyDate=input("Enter the Start Date")
        self.TypeOfTrip=input("Enter the Trip type(round/oneway): ")
        if(self.Name!="" and self.EmailId!="" and self.PhoneNo!=""):
            if(self.TypeOfTrip=="round"):
                self.ReturnDate=input("Return Date: ")
                if(self.ReturnDate!=""):
                    self.TypeOfTRansport=input("type Of transport(bus/plane/train)")
                    if(self.TypeOfTRansport!=""):
                        print("Thanks For Booking From Indigo")
                        return
            else:
                print("Thanks For Booking From Indigo")
        else:
            print("Invalid Enter Again!")
            self.BookTicket()
        
ob1=MakeMyTrip()
ob1.BookTicket()
ob2=IRCTC()
ob2.BookTicket()
ob3=Indigo()
ob3.BookTicket()