# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def square(self, n):
        return n * n

    def cube(self, n):
        return n * n * n

    def square_root(self, n):
        return n ** 0.5


# Creating object of the class
calc = Calculator()

num = int(input("Enter a number: "))

print("Square:", calc.square(num))
print("Cube:", calc.cube(num))
print("Square Root:", calc.square_root(num))
