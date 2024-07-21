"""
Create a Person class with attributes like name and age. 
Implement a constructor (__init__) to initialize these attributes.
Also, implement a destructor (__del__) method to print a farewell message when an object is deleted.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print(f"Farewell, {self.name}. You have been deleted")

    def __repr__(self):
        return f"Full name is {self.name} and is {self.age} years old"
    
    

person1 = Person("Alice", 30)
print(person1) 

#del person1