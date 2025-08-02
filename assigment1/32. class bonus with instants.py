
class Bonus:
    def __init__(self, salesperson_id, sales_amount):
        self.salesperson_id = salesperson_id
        self.sales_amount = sales_amount

    def calculate_bonus(self):
        if self.sales_amount >= 5000:
            return self.sales_amount * 0.1
        else:
            return self.sales_amount * 0.05


#Create Object and Use:


salesperson1 = Bonus("S001", 5000)
print("Bonus:", salesperson1.calculate_bonus())
Bonus:("{salesperson2.get_premium_bonus()}")


