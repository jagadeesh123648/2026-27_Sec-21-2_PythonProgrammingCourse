
# Function to print details using **kwargs

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Function call using keyword arguments
print_details(name="Krishna", age=26, city="Guntur")
