
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

area, perimeter = rectangle(length, breadth)

print("Area of Rectangle:", area)
print("Perimeter of Rectangle:", perimeter)
