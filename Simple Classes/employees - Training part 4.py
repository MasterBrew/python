class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
         return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
         self.pay = int(self.pay * self.raise_amt)

# Make a new class Developer with inheriting the features of class.Employee

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    raise_amt = 2.00

    def __init__(self, first, last, pay, employees=None):

        # calling its parrents for starting values from our base class 'Employee')
        # You can also use 'Employee.__init__(self, first,last,pay)'

        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
           print("-->", emp.fullname())




dev_1 = Developer('Corey','Schafer', 50000, 'Python')
dev_2 = Developer('Test','User', 60000, 'Java')

mgr_1 = Manager('Sue','Smith', 90000, [dev_1])

print(mgr_1.email)

#3print("manager Employee list:")
#mgr_1.print_emps()

print("manager Employee new list:")

mgr_1.add_emp(dev_2)
mgr_1.print_emps()


print("manager fire! Development :")

mgr_1.remove_emp(dev_1)
mgr_1.remove_emp(dev_2)


print("manager Employee new list:")

mgr_1.print_emps()


#print(help(man_1))
#print(man_1.__dict__)
#print(dev_1.__dict__)
# print(dev_1.email)
# print(dev_2.email)
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
#print(dev_1.email)
#print(dev_1.prog_lang)
