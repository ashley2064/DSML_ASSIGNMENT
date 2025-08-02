class Distance:
    def _init_(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet + total_inches // 12
        inches = total_inches % 12
        return Distance(total_feet, inches)

    def compare(self, other):
        # Convert both distances to total inches for comparison
        self_total = self.feet * 12 + self.inches
        other_total = other.feet * 12 + other.inches
        if self_total > other_total:
            return "First distance is greater"
        elif self_total < other_total:
            return "Second distance is greater"
        else:
            return "Both distances are equal"

    def display(self):
        print(f"{self.feet} feet {self.inches} inches")


#Create two Distance objects
dist1 = Distance(5, 8)
dist2 = Distance(6, 4)

#Add distances
sum_dist = dist1.add(dist2)

#Display distances
print("Distance 1:")
dist1.display()

print("Distance 2:")
dist2.display()

print("Sum of distances:")
sum_dist.display()

#Compare distances
print("Comparison result:")
print(dist1.compare(dist2))