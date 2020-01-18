# Object
class Employee:
    num_of_emps = 0 # class variable
    raise_amount = 1.04
    def __init__(self, first, last, pay):  
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = 1000

        Employee.num_of_emps += 1

    def config(self):
        print("Config ")

    def fullname(self):
        return '{} {} {}'.format("hi ", self.first, self.last)

    # class method can't access global variable in a class, why? but the weird thing self can work
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Regular Method, I don't understand
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


    def set_raise_amt1(self,amt):
        self.raise_amount = amt

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # static method don't take instance or class as the first arg
    @staticmethod
    def is_workday(day):      
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
# Own Instance
# emp_1 = Employee('Lip Kang', 'Ee', 'callmekang1996@gamil.com', 1000)
# emp_2 = Employee('Life is pretty nice', 'yeah~', 'cryharderplz@gmail.com', 2000)
emp_1 = Employee('Lip Kang', 'Ee', 1000)
emp_2 = Employee('Life is pretty nice', 'yeah~', 2000)

import datetime
my_date = datetime.date(2016, 7, 13)
print(my_date.weekday())
print(Employee.is_workday(my_date))


