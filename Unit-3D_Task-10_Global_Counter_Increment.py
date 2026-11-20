
# Global counter variable
counter = 0

# Function to increment the global counter
def increment():
    global counter
    counter += 1
    print("Counter value:", counter)

# Function calls
increment()
increment()
increment()
increment()
