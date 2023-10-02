import datetime
name=input("what is your name?")
year=int(input("enter you birth year?"))
current_year = datetime.datetime.now().year
current_age = datetime.datetime.now().year-year
print("Hey, " + name + "!your age is " + str(current_age) + ".")
