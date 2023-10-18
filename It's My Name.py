#FOR N
length = 5
for row in range(1,length+1):
    for column in range(1,length+1):
        if column == 1  or column == length or row == column:
            print('*', end=' ')
        else:
            print(' ', end=' ')    
    print()

#FOR I
for row in range(length):
    for column in range(length):
        if row == 0 or row == 4 or column == 2:
            print('*', end=' ')
        else:
             print(' ', end=' ')
    print()

#FOR T
for row in range(length):
    for column in range(length):
        if row == 0 or column == 2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#FOR H    
for row in range(length):
    for column in range(length):
        if column == 0 or row == 2 or column == 4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#FOR I       
for row in range(length):
    for column in range(length):
        if row == 0 or column == 2 or row == 4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#FOR S     
for row in range(length):
    for column in range(length):
        if row == 0 or row == 4 or row == 2: 
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
 
#FOR H    
for row in range(length):
    for column in range(length):
        if column == 0 or row == 2 or column == 4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()



 
