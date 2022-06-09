#Coffe machine program
#Samira

primary_resources={
    "water":300,
    "milk":200,
    "coffe":100,

}

options = {"espersso":{
    "water":50,
    "milk":0,
    "coffe":18,
    "price":1.5,
},

"latte" : {
    "water":200,
    "milk":150,
    "coffe":24,
    "price":2.5,
},
"coppochino":{
    "water":250,
    "milk":100,
    "coffe":24,
    "price":3,
}}

coins= {"penny":1.5,
        "dime":0.1,
        "quarter":0.25,
        "nickle":0.5}



residue = primary_resources
source = ["water", "coffe", "milk"]

while residue["water"]>49 and residue["coffe"]>18:


    answer = input("Hello.What do you want to drink?espersso, latte or coppochino?  ")

    #report


    print(f"Report: The total remain sources are {residue}")
    if residue["water"]<50:
        print("The spources are in limitation. Please charge all of them")

    total_price = options[answer]["price"]

    print(f"The price of your {answer} would be ${total_price}")
    # coin processing

    penny= int(input("How many penny do you want pay?  "))
    nickle = int(input("How many nickle do you want pay?  "))
    dime = int(input("How many dime do you want pay?  "))
    quarter = int(input("How many quarter do you want pay?  "))

   # Value of each coin
    p=(penny*0.01)
    n=(nickle * 0.05)
    d= (dime * 0.1)
    q=(quarter*0.25)

    total_payment = (p+n+d+q)
    print(f"Your payment is ${round(total_payment, 2)}")

    change = round(total_payment - total_price , 2)
    if change>=0:
        print(f"Your change is {change}. Thank you for your buy.")
    else:
        print("Your payment was not enough. please try a gain")
    if residue["water"]<50:
        print("you run out of resources please charge again.")


    for i in source:

       residue[i] = residue[i]- options[answer][i]
       if residue[i]<0 :
           print(f"Sorry, we run out of {i}.Please charge")
           residue[i]= residue[i]+ options[answer][i]

    print(f"Report: now you have these {residue} sources")