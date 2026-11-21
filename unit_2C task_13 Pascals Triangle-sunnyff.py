rows = int(input("Enter the number of rows: "))

for row in range(rows):
    print(" " * (rows - row), end="")

    num = 1
    for col in range(row + 1):
        print(num, end=" ")
        num = num * (row - col) // (col + 1)

    print()