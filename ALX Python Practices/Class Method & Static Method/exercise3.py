class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name, age = 0):
       return cls(name, age)
    
    def __repr__(self):
        return f"Person (name = '{self.name}', age = {self.age})"
    
parent = Person("Edwin", 26)
child = Person.create_child("Edwin Jr")

print(parent)
print(child)