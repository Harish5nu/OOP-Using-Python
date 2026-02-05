# Chapter 10 – Object Oriented Programming (Python)

Object-Oriented Programming (OOP) is one of the most popular approaches to solving problems in programming.  
Instead of only using functions, OOP focuses on **creating objects** that contain both data and behavior.

OOP helps in writing **reusable, clean, and organized code**, following the **DRY Principle (Don’t Repeat Yourself)**.

---

## What is a Class?

A **class** is a blueprint for creating objects.  
It defines the **properties (attributes)** and **behaviors (methods)** that the objects will have.

### Syntax
```python
class Employee:   # Class name is written in PascalCase
    # Variables & Methods
    pass
```

---

## What is an Object?

An **object** is an **instance of a class**.

- When a class is defined → no memory is allocated
- When an object is created → memory is allocated

Objects can use the methods of a class **without knowing how they are implemented**, which gives us:
- **Abstraction**
- **Encapsulation**

### Example
```python
harry = Employee()   # Object instantiation
```

---

## Modelling a Problem Using OOP

When converting a real-world problem into OOP, we identify:

- **Noun → Class**  
  Example: `Employee`

- **Adjectives → Attributes**  
  Example: `name`, `age`, `salary`

- **Verbs → Methods**  
  Example: `getSalary()`, `increment()`

---

## Class Attributes

A **class attribute** belongs to the **class itself**, not to a specific object.

### Example
```python
class Employee:
    company = "Google"   # Class attribute

harry = Employee()
print(harry.company)

Employee.company = "YouTube"   # Changing class attribute
```

- Class attributes are shared by all objects of the class.

---

## Instance Attributes

An **instance attribute** belongs to a **specific object**.

### Example
```python
harry.name = "Harry"
harry.salary = "30k"
```

### Important Note
- **Instance attributes take priority** over class attributes.
- Attribute lookup order:
  1. Object (instance)
  2. Class

---

## The `self` Parameter

- `self` refers to the **current object**
- It is automatically passed when a method is called using an object

### Example
```python
harry.getSalary()
```

This is equivalent to:
```python
Employee.getSalary(harry)
```

### Method Definition
```python
class Employee:
    company = "Google"

    def getSalary(self):
        print("Salary is not there")
```

---

## Static Methods

Sometimes, we need a method that **does not use `self`**.

For such cases, we use **static methods**.

### Example
```python
class Employee:

    @staticmethod
    def greet():
        print("Hello user")
```

- Static methods are not dependent on object or class data.

---

## `__init__()` Constructor

- `__init__()` is a **special method**
- It runs **automatically when an object is created**
- Used to initialize object data

### Example
```python
class Employee:
    def __init__(self, name):
        self.name = name

    def getSalary(self):
        print("Salary not defined")

harry = Employee("Harry")
```

---

## Practice Set – Chapter 10

1. Create a class **`Programmer`** to store information of programmers working at Microsoft.
2. Write a class **`Calculator`** to find:
   - Square
   - Cube
   - Square root of a number
3. Create a class with a **class attribute `a`**.  
   Create an object and set `object.a = 0`.  
   Does this change the class attribute?
4. Add a **static method** in the Calculator class to greet the user with **"Hello"**.
5. Write a class **`Train`** with methods to:
   - Book a ticket
   - Get seat status
   - Get fare information (Indian Railways)
6. Can you change the `self` parameter to another name like `slf` or `harry`?  
   Try it and observe the result.

---

## Key Takeaways

- Class → Blueprint  
- Object → Instance of a class  
- Class attributes → Shared  
- Instance attributes → Object-specific  
- `self` → Refers to current object  
- `__init__()` → Constructor  
- Static methods → No `self` required  

---

Happy Coding 🚀
