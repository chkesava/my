class Father:
    def bike(self):
        print("buy a harly davidson bike")
    def laptop(self):
        print("Buy a laptop with 2gb ram and 500gb hdd")
class Son(Father):
    def laptop(self):
        print("as per my coding and software engineering life")
        print("but a laptop with 16gb ram and 1tb sdd")
obj1=Son()
obj1.bike()
obj1.laptop()