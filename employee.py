"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, salary=0, hours=0, pHour=0, commission=0, bonus_commission=0, num_contracts=0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.pHour = pHour
        self.commission = commission
        self.bonus_commission = bonus_commission
        self.num_contracts = num_contracts

    def get_pay(self):
        return self.salary + (self.hours * self.pHour) + (self.commission * self.num_contracts) + self.bonus_commission

    def __str__(self):
        description = ""
        com=""
        bonus=""
        if self.commission > 0:
            com = f" and receives a commission for {self.num_contracts} contract(s) at {self.commission}/contract"
        if self.bonus_commission > 0:
            bonus = f" and receives a bonus commission of {self.bonus_commission}"
        if self.salary > 0:
            description += f"{self.name} works on a monthly salary of {self.salary}"
        elif self.hours > 0 and self.pHour > 0:
            description += f"{self.name} works on a contract of {self.hours} hours at {self.pHour}/hour"

        description += com + bonus + f". Their total pay is {self.get_pay()}."
        return description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee("Charlie", hours=100, pHour=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee("Renee", salary=3000, commission=200, num_contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee("Jan", hours=150, pHour=25, commission=220, num_contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee("Robbie", salary=2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee("Ariel", hours=120, pHour=30, bonus_commission=600)
