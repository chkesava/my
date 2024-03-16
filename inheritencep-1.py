class Faculty:
    def __init__(self,f_name,department,id):
        self.f_name=f_name
        self.department=department
        self.id=id
    def Print_info(self):
        print("faculty Information: ",self.f_name,self.department,self.id)
class Cse(Faculty):
    pass
class IT(Faculty):
    pass

obj1=Faculty("monish","information Technology",1233)
obj2=Cse("kesava","Cse",1238)
obj3=IT("Mohith","Information Technology",1241)
obj1.Print_info()
obj2.Print_info()
obj3.Print_info()
