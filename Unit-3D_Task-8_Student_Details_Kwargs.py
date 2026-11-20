
# Function to display student details using **kwargs

def student_details(**kwargs):
    print("Student Details:")

    for key, value in kwargs.items():
        print(key, ":", value)

# Function call
student_details(name="Krishna", Maths=90, Physics=85, Chemistry=88)
