number=int(input("enter te number:"))
times=0
divide_by_number=5
while number>=divide_by_number:
    number=number/5
    print(number)
    times=times+1
print("the number of times the number was divided",times)
