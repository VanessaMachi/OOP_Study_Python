# let's Cry hard


# Object
class Computer:

    def __init__(self, cpu="1", ram="0"):  
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config " + self.cpu, self.ram)


computer1 = Computer("i5","16GB")
computer2 = Computer("Ryzen5","16GB")
computer3 = Computer()

computer1.config()

# Object
class Employee:


    def __init__(self, first, last, email=0):  
        self.first = first
        self.last = last
        self.email = email

    def config(self):
        print("Config ")

    def fullname(self):
        return '{} {} {}'.format("hi ", self.first, self.last)
        
# Own Instance
emp_1 = Employee('Lip Kang', 'Ee', 'callmekang1996@gamil.com')
emp_2 = Employee('Life is pretty nice', 'yeah~', 'cryharderplz@gmail.com')

print(emp_2.fullname())