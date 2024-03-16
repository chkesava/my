"""
create a class of name placements wj=hich has a function info which displays we have {number} placements and still contunu
create a another class dept with function display which will displays names of departments present in the college .
create a class pragati with a function welcome which displays the message welcome to pragati we are glad to on your college 
this pragati class should also displays the details about departments and placements 
"""
class Placements:
    def __init__(self,placements):
        self.placements=placements
    def info(self):
        print("we have",self.placements,"placements and still continue......")
class Departments(Placements):
    def displays(self):
        print("the departments present in college is ")
        print("1.cse,2.it,3.ece,4.civil,5.ai&ds,6.ds")
class Pragati(Departments):
    def welcome(self):
        print("welcome")
obj1=Pragati(654)
obj1.welcome()
obj1.info()

