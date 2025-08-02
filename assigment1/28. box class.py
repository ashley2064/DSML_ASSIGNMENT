class Box:
    def _init_(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self):
        return 2 * (self.width * self.height + self.height * self.depth + self.width * self.depth)


#Create two Box objects
box1 = Box(2, 3, 4)
box2 = Box(5, 6, 7)

#Output for first box
print("Box 1:")
print("Volume:", box1.volume())
print("Surface Area:", box1.surface_area())

#Output for second box
print("\nBox 2:")
print("Volume:", box2.volume())
print("Surface Area:", box2.surface_area())

