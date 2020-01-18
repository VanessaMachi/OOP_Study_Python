# Object
class Employee:
    num_of_emps = 0 # class variable
    raise_amount = 1.04
    def __init__(self, first, last, email, pay):  
        self.first = first
        self.last = last
        self.email = email
        self.pay = 1000

        Employee.num_of_emps += 1

    def config(self):
        print("Config ")

    def fullname(self):
        return '{} {} {}'.format("hi ", self.first, self.last)

    # class method can't access global variable in a class, why? but the weird thing self can work
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
# Own Instance
emp_1 = Employee('Lip Kang', 'Ee', 'callmekang1996@gamil.com', 1000)
emp_2 = Employee('Life is pretty nice', 'yeah~', 'cryharderplz@gmail.com', 2000)

emp_2.raise_amount # Instance variable
Employee.raise_amount # Class variable
print(emp_1.__dict__)