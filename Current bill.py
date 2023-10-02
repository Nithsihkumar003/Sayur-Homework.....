units=int(input("enter the number of units: ")) 

if units >500:

    print("your unit must be less than 500")

elif units <=100:

    print("there is no payment for first 100 unit")

elif units <=200:

    amount = (units -100)*2.25

    print("payable amount:",amount)
elif units <= 400:

    amount = 225+ ((units-200)*4.5)

    print("payable amount:",amount)
else:

    amount = 225+900+((units-200)*6)

    print("payable amount:",amount)
    


