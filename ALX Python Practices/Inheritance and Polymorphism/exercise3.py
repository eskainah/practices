"""
Create classes Dog, Cat, and Bird, each with a method make_sound().
Implement different behaviors for make_sound() in each class.
Create a function let_them_speak() that takes a list of objects and calls their make_sound() method polymorphically.
"""
class Dog: 
    def make_sound(self):
        print("wchoo wchoo")

class Cat:
    def make_sound(self):
        print("mewhee mewhee")

class Bird:
    def make_sound(self):
        print("tre tre tre")
    
for animal in Dog(), Cat(), Bird():
    animal.make_sound()
        