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
    print(     )            
    

#FOR S     
 
   
for row in range(5):
    for column in range(5):
        if (row == 0 or row == 2 or row == 4) or column == 0 and (row > 0 and row < 2) or column == 4 and (row > 2 and row < 4):  
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(   )
 
#FOR H    
for row in range(length):
    for column in range(length):
        if column == 0 or row == 2 or column == 4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(  )

#For  K

for row in range(5):
    for column in range(5):
        if column == 0 or column == 1 and (row > 1 and row < 3)or column == 2 and (row > 0 and row < 2)or row == 0  and (column > 2)or row == 3 and (column > 1 and column < 3)or row == 4  and (column > 2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(  )

#For U
for row in range(5):
    for column in range(5):
        if column == 0 or column == 4 or row == 4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(  )

#for M 

for row in range(5):
    for column in range(5):
        if column == 0 or column == 4 or (row == 1 and (column > 0 and column < 2 ) or row == 1 and column > 2 and column < 4 ) or row == 2 and column > 1 and column < 3 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(  )   

#For A
for row in range(5):
    for column in range(5):
        if column == 0 or column == 4 or row == 0 or row == 2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(         )  

#For R
for row in range(5):
    for column in range(5):
        if column == 0 or row == 0 or column == 4 and (row > 0 and row < 3) or row == 2 and (column > 1 ) or row == 3 and (column > 2 and column < 4) or row == 4 and (column > 3):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(            )  
  

  





 
