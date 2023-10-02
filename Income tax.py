annual_income = float(input("Enter the taxable income: "))

if annual_income <= 250000:

    old_tax = 0

    new_tax = 0

elif annual_income <= 500000:

    old_tax = (annual_income - 250000) * 0.05
    new_tax = (annual_income - 250000) * 0.05

elif annual_income <= 750000:

    old_tax = 250000*0.05+ (annual_income - 500000)* 0.20
    new_tax = 250000 *0.05+ (annual_income - 500000) * 0.10

elif annual_income <= 1000000:

    old_tax = 250000* 0.05+ 250000* 0.20+ (annual_income - 750000) * 0.20
    new_tax = 250000* 0.05+250000* 0.10+ (annual_income - 750000) * 0.15

elif annual_income <= 1250000:

    old_tax = 250000* 0.05+250000* 0.20+250000* 0.20+ (annual_income - 1000000)*0.30
    new_tax = 250000* 0.05+250000* 0.10+250000* 0.20+ (annual_income - 1000000) * 0.25

elif annual_income <= 1500000:

    old_tax=250000* 0.05+ 250000* 0.20+250000*0.20 +250000 *0.30+ (annual_income - 1250000)*0.30
    new_tax = 250000* 0.05+250000* 0.10+250000* 0.20+ 250000* 0.25 + (annual_income - 1250000) * 0.30

else:

    old_tax = 250000* 0.05+250000* 0.20+250000* 0.20+250000* 0.30 +250000* 0.30+ (annual_income - 1500000)*0.30
    new_tax = 250000* 0.05 + 250000*0.10+250000* 0.20+250000* 0.25 + 250000* 0.30+ (annual_income - 1500000)*0.30

print("Old Tax Amount: Rs.", old_tax)
print("New Tax Amount: Rs.", new_tax)
