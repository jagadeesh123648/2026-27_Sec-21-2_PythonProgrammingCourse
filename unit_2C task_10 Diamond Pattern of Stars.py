rows = int(input("Enter the number of rows: "))

# Upper part
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    print("* " * i)