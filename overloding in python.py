class Arithmatic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj1=Arithmatic()
#obj1.add(10)
#obj1.add(1,2)
obj1.add(1,2,3)



"""
python overloading means using the same function or operator but the behaviour s different for example if we add 
2+3 gives 5
and if we gives "3"+"4" gives '34' in previous it acts as a arthemetic operator but here it acts as a string concatination

but in python functional overloading is not supported       
"""