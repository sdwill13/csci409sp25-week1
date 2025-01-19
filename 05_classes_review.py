"""
    Program 5: Classes Review
    Student Name: Staci Williams
    Course: CSCI 409 D1
"""

# 1. Create a class named Rectangle
#    1pt
class Rectangle:
    # 2. Create 2 class variables called length and width
    #    2pts
    length = 2
    width = 4

    # 3. Create an init function
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # 4. Create a function called area
    def area(self):
        return self.length * self.width

# 5. Create a new instance of the rectangle class
#    with a length of 10 and a width of 8
#    assign the class to the variable r1
r1 = Rectangle(10, 8)

# 6. Print the length of the rectangle previously created
print("Previous Rectangle Length: ",r1.length)

# 7. Print the area of the rectangle previous created
print("Area of Rectangle 1: ",r1.area())