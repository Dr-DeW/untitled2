class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return self.age == other.age
        return NotImplemented

tom = Person('df',45)
bob = Person('df',45)
print(tom == bob)
# from dataclasses import dataclass

# @dataclass
# class Person:
#   name: str
#  age: int

# tom = Person(67,45)
# bob = Person(67,46)
# print(tom == bob)
