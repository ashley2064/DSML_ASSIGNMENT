class Rectangle:
    def _init_(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


#Creating two different rectangles
rect1 = Rectangle(5, 3)
rect2 = Rectangle(7, 4)

#Output for first rectangle
print("Rectangle 1:")
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

#Output for second rectangle
print("\nRectangle 2:")
print("Area:", rect2.area())
print("Perimeter:", rect2.perimeter())
