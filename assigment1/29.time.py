class Time:
    def _init_(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        # Format time as hh:mm:ss with leading zeros
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def add(self, other):
        total_seconds = self.seconds + other.seconds
        total_minutes = self.minutes + other.minutes + total_seconds // 60
        total_hours = self.hours + other.hours + total_minutes // 60

        # Normalize seconds and minutes
        seconds = total_seconds % 60
        minutes = total_minutes % 60
        hours = total_hours % 24  # Assuming 24-hour format

        return Time(hours, minutes, seconds)


#Create two Time objects
time1 = Time(2, 45, 50)
time2 = Time(3, 20, 30)

#Add times
result = time1.add(time2)

#Display times and result
print("Time 1:")
time1.display()

print("Time 2:")
time2.display()

print("Sum of times:")
result.display()
