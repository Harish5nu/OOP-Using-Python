#Q1. create a class "progarmming" for storing information of few programmers working at Microsoft.

class programeer:
    company="Microsoft"
    def __init__(self, name, salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p= programeer("Harry", 120000, 2131)
print(p.name,p.pin, p.company)