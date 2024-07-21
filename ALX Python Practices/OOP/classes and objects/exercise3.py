"""
Create a base class Animal with methods like eat and sleep.
Create a subclass Dog that inherits from Animal and adds a method bark.
Create instances of both classes and demonstrate method inheritance.
"""

class Animal:
    def eat(self):
        print("I can eat")
    
    def sleep(self):
        print("I can sleep")

class Dog(Animal):
    def bark(self):
        print("woof")

# Create instances of both classes
animal = Animal()
dog = Dog()

# Demonstrate method inheritance
animal.eat()     # Output: The animal is eating.
animal.sleep()   # Output: The animal is sleeping.

dog.eat()        # Output: The animal is eating.
dog.sleep()      # Output: The animal is sleeping.
dog.bark()       # Output: The dog is barking.