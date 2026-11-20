
# Global variable
x = 100

def display():
    # Local variable
    x = 50
    print("Local variable inside function:", x)

# Display global variable
print("Global variable before function call:", x)

# Function call
display()

# Display global variable again
print("Global variable after function call:", x)
