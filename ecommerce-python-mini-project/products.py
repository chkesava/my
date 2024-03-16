import csv
class Products:
    def Clothing(self):
        with open('products.csv','r',newline="") as file:
            store=list(csv.DictReader(file))
            self.ClothsList=[product for product in store if product['category']=='clothing']
            print("select the Product:")
            print("Id Product")
            for clothItem in self.ClothsList:
                print(str(clothItem["product_id"])+" "+clothItem["product_name"])
            self.ProductIdByUser=int(input("select the product by using its id :"))
            
ob1=Products()
ob1.Clothing()