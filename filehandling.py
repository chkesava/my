import csv 
class StudentDetails:
    def addStudent(self):
        f=open("student.csv","a",newline="")
        a=csv.writer(f)
        studentId=int(input("enter the studentId: "))
        rollNo=int(input("enter the rollNo: "))
        name=input("enter the name: ")
        mobileNo=int(input("Enter the mobile no:"))
        a.writerow([studentId,rollNo,name,mobileNo])
        print("student record saved sucessFul")
        userinput=input("enter 0ne more entry:")
    def ShowNameAndId(self):
        with open("student.csv","r",newline="") as file:
            read=csv.DictReader(file)
            print(read)
            for row in read:
                print([row["StudentId"],row["name"]])
obl1=StudentDetails()
obl1.ShowNameAndId()

