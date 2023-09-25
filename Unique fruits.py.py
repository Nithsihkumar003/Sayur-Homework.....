fruit_name = input("ente your fruit name in your basket:")
fruits = fruit_name .split()
unique_fruits = set()
for fruit in fruits :
    unique_fruits .add(fruit)
for fruits in unique_fruits:
    print(fruits)