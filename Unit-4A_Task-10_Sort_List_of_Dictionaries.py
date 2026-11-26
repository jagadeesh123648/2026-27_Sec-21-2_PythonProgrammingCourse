students = [
    {"name": "Sunny", "marks": 85},
    {"name": "Rahul", "marks": 70},
    {"name": "Kiran", "marks": 95},
    {"name": "Arun", "marks": 80}
]

# Ascending order
ascending = sorted(students, key=lambda x: x["marks"])

# Descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:")
for s in ascending:
    print(s)

print("\nDescending Order:")
for s in descending:
    print(s)