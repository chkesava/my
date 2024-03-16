"""
write a program to check the onroad price of a bike and the conditions i the peice us greater than 72k then income tax is 10% of the exshowroom price and the health insurance is 15% of actual price
of the price is greater than 150k and less than 200k the tax should be 25% and insurance will be 20%
if price is above 200k then tax will be 35% and insurance will be 28%
otherwise minprice is 72k
onroad price =actualprice+tax+insurrance
"""
original_price=int(input())

def calculate(amount, percent): 
    return (amount * percent) / 100

if(original_price>72000 and original_price<=150000):
    tax=calculate(original_price,10)
    print(tax)
    insurance=calculate(original_price,15)
    on_road_price=original_price+tax+insurance
    print(on_road_price)
elif(original_price>150000 and original_price<=200000):
    tax=calculate(original_price,25)
    print(tax)
    insurance=calculate(original_price,20)
    on_road_price=original_price+tax+insurance
    print(on_road_price)
elif(original_price>200000 ):
    tax=calculate(original_price,35)
    print(tax)
    insurance=calculate(original_price,28)
    on_road_price=original_price+tax+insurance
    print(on_road_price)

else:
    print("enter the price value greater than 72k")
