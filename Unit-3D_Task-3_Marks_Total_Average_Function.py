
# Function to calculate total and average marks

def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

# Get marks from user
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

# Function call
total, average = calculate_marks(m1, m2, m3)

# Display results
print("Total Marks:", total)
print("Average Marks:", average)
