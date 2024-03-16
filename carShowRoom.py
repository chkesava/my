class selectCar:
    def __init__(self):
        self.carcompanieslist = ["Toyota", "Mahindra", "Mercedes"]
        self.options = [1, 2, 3]
        for i in range(len(self.carcompanieslist)):
            print(i + 1, ".", self.carcompanieslist[i])
        flag = True
        while flag:
            self.carInputText = input("select a car company(1 to 3) or Car Company Name:")
            if len(self.carInputText) == 0:
                flag = False
                continue
            if self.carInputText.isdigit():
                intval = int(self.carInputText)
                if intval not in self.options:
                    print("Invalid Option. Enter a valid input.")
                    continue
                else:
                    self.carInputNumber = intval
                    flag = False
            else:
                try:
                    self.carInputNumber = self.carcompanieslist.index(self.carInputText) + 1
                    flag = False
                except ValueError:
                    print("Invalid Option. Enter a valid input.")
        self.selectedCar = self.carcompanieslist[self.carInputNumber - 1]

    def CarModel(self):
        self.ModelsList = [["urban", "Innova", "Rumion"], ["suv", "xuv", "scorpio"], ["xm", "x3", "x7"]]
        print("Welcome to " + self.selectedCar + " Company!")
        self.selectedCompanyList = self.ModelsList[self.carInputNumber - 1]
        for i in range(len(self.selectedCompanyList)):
            print(i + 1, ".", self.selectedCompanyList[i])
        flag = True
        while flag:
            modelInputText = input("Select a car model (1 to 3) or Car Model Name:")
            if len(modelInputText) == 0:
                flag = False
                continue
            if modelInputText.isdigit():
                modelInputNumber = int(modelInputText)
                if modelInputNumber not in self.options:
                    print("Invalid Option. Enter a valid input.")
                    continue
                else:
                    self.modelInputNumber = modelInputNumber
                    flag = False
            else:
                try:
                    self.modelInputNumber = self.selectedCompanyList.index(modelInputText) + 1
                    flag = False
                except ValueError:
                    print("Invalid Option. Enter a valid input.")

        self.selectedModel = self.selectedCompanyList[self.modelInputNumber - 1]
        print(self.selectedModel)

    def varient(self):
        self.varientNumber = 0
        while True:
            self.varientOfCar = input("Enter the variant of the car: petrol or diesel:")
            if self.varientOfCar == "petrol":
                print("entered")
                self.varientNumber = 0
                break
            elif self.varientOfCar == "diesel":
                self.varientNumber = 1
                break
            else:
                print("Invalid variant. Please enter again.")
        print(self.varientOfCar)

    def display(self):
        self.exShowroomPrices = [
            [{"urban": 200000, "Innova": 500000, "Rumion": 1200000},
             {"suv": 2590000, "xuv": 5460000, "scorpio": 1255000},
             {"xm": 5000000, "x3": 9800000, "x7": 1232000}],
            [{"urban": 1654000, "Innova": 3200000, "Rumion": 1400000},
             {"suv": 2690000, "xuv": 5550000, "scorpio": 1288000},
             {"xm": 5045000, "x3": 9825000, "x7": 1542000}]
        ]
        
        self.selectedVarientPrices = self.exShowroomPrices[self.varientNumber]
        self.CompanyModelsprices = self.selectedVarientPrices[self.carInputNumber - 1]
        self.ModelPrice = self.CompanyModelsprices[self.selectedModel]
        self.onRoadPrice = self.ModelPrice + (8 * self.ModelPrice) // 100 + (10 * self.ModelPrice) // 100 + 10000
        print("Company: ", self.selectedCar)
        print("Model: ", self.selectedModel)
        print("Variant: ", self.varientOfCar)
        print("Ex-Showroom Price: ", self.ModelPrice)
        print("On-Road Price: ", self.onRoadPrice)

user1 = selectCar()
user1.CarModel()
user1.varient()
user1.display()
