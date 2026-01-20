import math

class Calculator:
    def square(self, n):
        return n * n

    def cube(self, n):
        return n * n * n

    def sqrt(self, n):
        return math.sqrt(n)

# Example usage
c = Calculator()
num = 9

print("Square:", c.square(num))
print("Cube:", c.cube(num))
print("Square Root:", c.sqrt(num))
