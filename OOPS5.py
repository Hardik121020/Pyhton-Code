class Employee:
    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)
    
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
    
        
        
emp_1_str = 'John-Abraham-5000'
emp_1 = Employee.from_string(emp_1_str)
print(emp_1.__dict__)
