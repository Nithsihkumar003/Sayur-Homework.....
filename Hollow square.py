#Hollow Square
length = 5
breadth = 7
for row in range (length):
    for column in range (breadth):
        if row == 0 or row == 4 or column == 0 or column== 6:
            print('*', end=' ')
        else:
             print(' ', end=' ')
    print()
            
            
            

