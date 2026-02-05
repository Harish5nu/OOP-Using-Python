#Q1. create a class "progarmmer" for storing information of few programmers working at Microsoft.

class programmer:
    company="Microsoft"
    def __init__(self, name, salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin 

p= programmer("Harry", 120000, 2131)
print(p.name,p.pin, p.company)
p= programmer("Logan", 12000, 231)
print(p.name,p.company,p.pin,p.salary)