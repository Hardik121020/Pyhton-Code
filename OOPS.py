class Employee:
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.Email = first_name + '.' + last_name + '@company.com'
a = Employee("Mohandas","Gandhi",50000)
print(a.first_name)
print(a.last_name)
print(a.pay)
print(a.Email)
print(a.__dict__)
