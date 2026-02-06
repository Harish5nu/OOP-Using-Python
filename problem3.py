#Q. Create a class attribute a; create an object from it and set 'a' directly using object.a=o. Does this change the class attribute?

class Demo:
    a=4

o=Demo()
print(o.a) # prints the class attribute because instance attribute is not present
o.a=0 # instance attribute is set
print(o.a) # prints the instance attribute because attribute is present
print(Demo.a)