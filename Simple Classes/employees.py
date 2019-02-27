class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = first + '.' + last + '@company.com'
        self.employee_nr = Employee.num_of_emps + 1
        Employee.num_of_emps += 1

    def fullname(self):
       return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
       self.pay = int(self.pay * self.raise_amt)
       if self.pay <= 0:
           self.pay = "!!KICK THIS MOFO!!"
           self.raise_amt = None

    #Use Class methode to change Global Variable
    @classmethod
    def set_raise_amt(cls, amount):
       cls.raise_amt = amount

''''
                                                Start a company with 4 persons 
'''
# creating instances of the class Employee
emp_1 = Employee('Corey','Schafer', 50000)
emp_2 = Employee('Test','User', 60000)
emp_3 = Employee('Dagobert','Duck', 1000000)
emp_4 = Employee('Dart','Fader', -999999)


# Class Funtion Methode
Employee.set_raise_amt(1.05)   # Set the new raise amount to whole class of Employee

# Objects Atribute Methode.
Employee.raise_amt = 1.05

## Both set the Class raise amnt because of the Class Function Usage!
# Bussness is bad no raise!
Employee.set_raise_amt(1.00)

emp_3.raise_amt = 1.20

#Special reward ...
emp_1.raise_amt = 1.15

print("General Raise : " + str(Employee.raise_amt))

print(str(emp_1.employee_nr) + " Pay:" + str(emp_1.pay) + " Raise: " + str(emp_1.raise_amt) + " " + emp_1.email)
print(emp_1.__dict__)
print(str(emp_2.employee_nr) + " Pay:" + str(emp_2.pay) + " Raise: " + str(emp_2.raise_amt) + " " + emp_2.email)
print(emp_2.__dict__)
print(str(emp_3.employee_nr) + " Pay:" + str(emp_3.pay) + " Raise: " + str(emp_3.raise_amt) + " " + emp_3.email)
print(emp_3.__dict__)
print(str(emp_4.employee_nr) + " Pay:" + str(emp_4.pay) + " Raise: " + str(emp_4.raise_amt) + " " + emp_4.email)
print(emp_4.__dict__)

print("----- Give the people some raise ------")
#emp_1.apply_raise()

Employee.apply_raise(emp_1)
Employee.apply_raise(emp_2)
Employee.apply_raise(emp_3)
Employee.apply_raise(emp_4)

print(str(emp_1.employee_nr) + " Pay: $" + str(emp_1.pay) + " Raise: " + str(emp_1.raise_amt) + " " + emp_1.fullname())
print(str(emp_2.employee_nr) + " Pay: $" + str(emp_2.pay) + " Raise: " + str(emp_2.raise_amt) + " " + emp_2.fullname())
print(str(emp_3.employee_nr) + " Pay: $" + str(emp_3.pay) + " Raise: " + str(emp_3.raise_amt) + " " + emp_3.fullname())
print(str(emp_4.employee_nr) + " Pay: $" + str(emp_4.pay) + " Raise: " + str(emp_4.raise_amt) + " " + emp_4.fullname())


