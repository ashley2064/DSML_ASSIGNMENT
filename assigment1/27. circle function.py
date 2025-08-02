class Circle:
    PI = 3.14159  # Class variable

    def _init_(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

    def circumference(self):
        return 2 * Circle.PI * self.radius


#Create two Circle objects
circle1 = Circle(3)
circle2 = Circle(5)

#Output for first circle
print("Circle 1:")
print("Area:", circle1.area())
print("Circumference:", circle1.circumference())

#Output for second circle
print("\nCircle 2:")
print("Area:", circle2.area())
print("Circumference:", circle2.circumference())

