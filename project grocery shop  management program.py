
# Project:- Grocessary Billing management program.
# index = 1
li = ["Shampoo ","Spices ","Soap ","Oil ","Sugar ","Rice ","Floor "]
print("srno.      Things    total aval.")
Total = []
i = 0
inForm = ["Packet's","gram","Pices","ml.","kg.","kg.","kg."]
#For find the key, value using enumerators function.
for index, item in enumerate(li):
    TotalAvailable = 0
    print(f"Enter quantity product {item} available in the shop=>",item,inForm[i],":",end="")
    aval = int(input())
    Total.append(aval)

    a = Total
    print()
    i = i+1

#Amount
def Amount():
    j = 0
    total = 0
    # print("Satyansh is a good boy",li)
    for rs in li:
        # print(rs)
        paisa = int(input(f"Enter price of {li[j]} {inForm[j]}"))
        j = j+1
        total = total+paisa
    print("\n\nYour total amount is",total," Only/.")
# Amount()

#here we are combining two list and make a dictionary.
# print("Total stock available in shop ",Total)
dictioary = dict(zip(li,Total))
print("Total available stock in the Shop:",dictioary)
inForm = ["Packet's","gram","Pices","ml.","kg.","kg.","kg."]
print("What all do you want to buy???")
l1 = 0
# Quant = []
for i in range(0,index+1):
    # print()
    qontity = int(input(f"Enter Quantity:{li[l1]}:{inForm[l1]}"))

    try:
        while(True):
            if(Total[i]>=qontity):
                print("ok!")
                i = i+1
                # Quant = Quant.append(qontity)
                break
            else:
                print("Please enter valid Quantity Available")
                qontity = int(input(f"Enter Quantity:{li[l1]}:{inForm[l1]}"))
                # Quant = Quant.append(qontity)
    except:
        print("Please enter correct input!")

    # print("This is real quontity:", Quant)

    l1 = l1+1
    print()
Amount()

input()
