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
    
        
# Own Instance
# emp_1 = Employee('Lip Kang', 'Ee', 'callmekang1996@gamil.com', 1000)
# emp_2 = Employee('Life is pretty nice', 'yeah~', 'cryharderplz@gmail.com', 2000)
emp_1 = Employee('Lip Kang', 'Ee', 1000)
emp_2 = Employee('Life is pretty nice', 'yeah~', 2000)

emp_2.raise_amount # Instance variable
Employee.raise_amount # Class variable

print(emp_1.__dict__)

Employee.set_raise_amt(1.05)
emp_1.set_raise_amt1(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'L-k-3000'
emp_str_2 = 's-s-3002'
emp_str_3 = 'william-low-9000'

# class methods as alternative constructor
new_emp_1 = Employee.from_string(emp_str_1)


print(new_emp_1.email)
print(new_emp_1.pay)


