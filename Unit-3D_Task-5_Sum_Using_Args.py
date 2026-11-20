
# Function to find sum using *args

def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# Function calls with different numbers of arguments
print("Sum of 2 numbers:", find_sum(10, 20))
print("Sum of 3 numbers:", find_sum(10, 20, 30))
print("Sum of 5 numbers:", find_sum(10, 20, 30, 40, 50))
