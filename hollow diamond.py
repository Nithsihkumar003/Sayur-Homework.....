length = 7

for row in range(length):
    for column in range(length):
        if row == 0 and (column == 3) or row == 1 and (column == 4) or row == 2 and (column == 5) or row == 3 and (column == 6) or column == 0 and (row == 3)or column == 1 and (row == 4)or column == 2 and (row == 5)or column == 3 and (row == 6) or row == 1 and (column == 2 ) or row == 2 and (column == 1 ) or row == 4 and (column == 5)or row == 5 and (column == 4):
            print('*', end=' ')
        else:
             print(' ', end=' ')
    print()