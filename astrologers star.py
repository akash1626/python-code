num_rows = int(input('Enter the number of rows\n'))
print("Enter 1 or 0")
bool_val = input("1 for True value or 0 for False\n")
if bool_val == "1":
    for i in range(0, num_rows + 1):
        print("*" * i)

if bool_val == "0":
    for i in range(num_rows, 0, -1):
        print("*" * i)
