class Employee:
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.Email = first_name + '.' + last_name + '@company.com'
    def getEmail(self):
        return self.Email
    def getfullname(self):
        return (self.first_name + ' ' + self.last_name )
    def getpay(self):
        return self.pay
a = Employee("Mohandas","Gandhi",50000)

print(a.getEmail())
print(a.getfullname())
print(a.getpay())
