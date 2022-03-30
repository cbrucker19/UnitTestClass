from datetime import datetime
class employee:
    """
    Employee Class
    """
    # Constructor
    def __init__(self, lname, fname, address, phone_number, salaried, start_date, salary):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = phone_number
        self.salaried = salaried
        self.start_date = start_date
        self.salary = salary

    def __str__(self):
        return  str(self.first_name) + " " + str(self.last_name) +  "\n" + str(self.address) + "\n" + str(self.phone_number) + "\n" + str(bool(self.salaried)) + ":" + str(float(self.salary)) + "\n" + "Start Date: " + str(self.start_date)

    def __repr__(self):
        return  str(self.first_name) + " " + str(self.last_name) +  "\n" + str(self.address) + "\n" + str(self.phone_number) + "\n" + str(bool(self.salaried)) + ":" + str(float(self.salary)) + "\n" + "Start Date: " + str(self.start_date)

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_salaried(self, salaried):
        self.salaried = salaried

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_salary(self, salary):
        self.salary = salary

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + ", " + str(self.address) + ", " + str(self.phone_number) + ", " + str(bool(self.salaried)) + ", " + str(self.start_date) + ", " + str(float(self.salary))

# Driver
emp = employee("Holt", "Mathew", "123 Main St", "555-555-5555", True, "3/29/2022", 40000)
print(emp.display())
print()
print(str(emp))
print()
print(repr(emp))
del emp
