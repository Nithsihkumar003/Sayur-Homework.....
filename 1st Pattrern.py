#Square pattern
n = int(input("ente a number you wish"))
for i in range(n):
    for j in range(n):
        print('  *' ,end='')
    print()


#Inceasing triangle 
n = int(input("ente a number you wish"))
for i in range(n):
     for j in range(i+1):
         print('  *' ,end='')
     print()   

#Decreasing triange
n = int(input("ente a number you wish"))
for i in range(n):
    for j in range(i,n):
        print('  *' ,end='')
    print()     