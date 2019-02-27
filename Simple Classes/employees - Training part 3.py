# Python OOP Object Oriantated Programming
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

    #Use Class methode decorator to change Global Variable
    @classmethod
    def set_raise_amt(cls, amount):
         cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
         first, last, pay = emp_str.split('-')
         return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey','Schafer', 50000)
emp_2 = Employee('Test','User', 60000)

import datetime
my_date = datetime.date(2016, 7 ,11)

print(Employee.is_workday(my_date))











'''

pay = 340000
first = 'Dagobert'
last = 'Duck'
emp_3 = Employee(first, last, pay)

#print(emp_1.__dict__)
#print(emp_2.__dict__)
#print(emp_3.__dict__)


# Use Class as a constructor for the Employee instances ..
# By using the from_string class funtion.

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.__dict__)
print(new_emp_2.__dict__)
print(new_emp_3.__dict__)



'''