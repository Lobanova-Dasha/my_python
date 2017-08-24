# emp_class.py


class Employee:

    num_of_emps = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last) 



    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)      



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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
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
                print('-->', emp.fullname())   

        


dev_1 = Developer('Dude', 'Lebowski', 50000, "Python")
dev_2 = Developer('Test', 'User', 60000, "Java")


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])


# emp_1 = Employee('Dude', 'Lebowski', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# import datetime
# my_date = datetime.date(2017, 2, 8)

# print(Employee.is_workday(my_date))
# emp_str_1 = 'Jhon-Doe-70000'
# emp_str_2 = 'Steve_Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'


# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

#print(Employee.__dict__)
# print(Employee.num_of_emps)

# emp_1.raise_amount = 1.05
# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)


