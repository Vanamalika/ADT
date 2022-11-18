from decimal import Decimal
from datetime import *

# defining variables
productlist=[{"soup" : "0.65"},
            {"bread" : "0.80"},
            {"milk" : "1.30"},
            {"apples" : "1.0"}
            ]

PriceBasket = []
Quantity = []
m = b = a = s = 0

# obtaining keys
all_keys = set().union(*(d.keys() for d in productlist))
print (all_keys)

# calculating 10% on apples if bought within dates
def apple():
    a = int(input("How many bags of apples do you want to buy: "))
    getValues = lambda key,inputData: [subVal[key] for subVal in inputData if key in subVal]
    f = (getValues(item, productlist))
    ap = a*Decimal(f[0])
    day = '16/Nov/2022'
    start = datetime.strptime(day, '%d/%b/%Y')
    end = start + timedelta(days=6)
    
    today = datetime.today()
    
    if start < today < end:
        tp = (10/100 * (a))
        app = int(ap)
        discount = (app-tp)
        print ("Apples 10% off: {} pounds".format(Decimal(tp)))
        return discount
    else:
        applesprice = (a*Decimal(f[0]))
        print("No offers available")
        #print("total apple price is {} pounds".format(a*Decimal(f[0])))
        return applesprice


# calculating bread price depending on number of soup tins
def bread():
    b = int(input("How many braad do you want to buy: "))
    getValues = lambda key,inputData: [subVal[key] for subVal in inputData if key in subVal]
    f = (getValues(item, productlist))
    bp = Decimal(f[0])
    fbp = float(bp)

       
    if s ==0:
        total = (bp*b)
        breadprice = total
        print("No offers available")
        return breadprice
    
    elif s % 2 == 0:
        # calculating total bread
        temp1 = s/2
        temp2 = b-temp1

        #calculating bread price
        hp = temp1 * (fbp/2)
        fp = temp2 * (fbp)
        
        #calculating total bread price
        tp = hp+fp
        breadprice = tp
        #print("total bread price is {} pounds".format(b*Decimal(f[0])))
        return breadprice
        
    else:
        # calculating total bread
        temp1 = (s-1)/2
        temp2 = b-temp1
        
        #calculating bread price
        hp = temp1 * (fbp/2)
        fp = temp2 * (fbp)
        
        #calculating total bread price
        tp = hp+fp
        breadprice = tp
        #print("total bread price is {} pounds".format(b*Decimal(f[0])))
        return breadprice
        
def milk():
    m = int(input("How many milk bottles do you want to buy: "))
    getValues = lambda key,inputData: [subVal[key] for subVal in inputData if key in subVal]
    f = (getValues(item, productlist))
    #print("total milk price is {} pounds".format(m*Decimal(f[0])))
    milkprice = m*Decimal(f[0])                
    return milkprice

def soup():
    s = int(input("How many soup tins do you want to buy: "))
    getValues = lambda key,inputData: [subVal[key] for subVal in inputData if key in subVal]
    f = (getValues(item, productlist))
    #print("total soup tins price {} pounds".format(s*Decimal(f[0])))
    soupprice = s*Decimal(f[0])
    return soupprice


entry = input(str("Enter the products with a space after each and press enter once you are done: "))

PriceBasket = entry.split(" ")
count = 0
for item in PriceBasket:
    if item not in all_keys:
        print("Product not available")
    else:
        if item == "apples":
            A = apple()
            print('returned', A)
            count = count + A
            print (count)
        elif item == "milk":
            M = milk()
            print('returned', M)
            count = count + M
            print (count)
        elif item == "bread":
            B = bread()
            print('returned', B)
            count = count + B
            print (count)
        elif item == "soup":
            S = soup()
            print('returned', S)
            count = count + S
            print (count)


print ("Total: {} pounds".format(Decimal(count)))

