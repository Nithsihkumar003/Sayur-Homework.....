# Tables requirement

start_num = 7
end_num = 16
# here we can give any number for the required tables as integer
num_of_rows = 12

for num in range (start_num, end_num + 1):
    print(f"multiplication tables for{num}:")
    for row in range (1,num_of_rows + 1):
        result = row * num
        print(f"{row} * {num} = {result}")
    print()