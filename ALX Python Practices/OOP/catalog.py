class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    
    def product_summary(self):
        product_details = f"The total value of {self.category} {self.name} in stock is : {self.price * self.quantity}"
        return product_details
    
#creating an object 
trouser = Product("Jeans", 5, 20, "male")
#print(trouser.product_summary())

#polymorphism
pants = [
    Product("Demin Jeans", 5, 20, "male"),
    Product("Oversize Jeans", 5, 50, "female"),
    Product("Cargo", 5, 20, "male"),
]
#Sort in alphabetical order
#pants.sort(key=lambda p: p.name)   


for pant in pants:
    print(pant.product_summary())


"""
searching for a particular data
for pant in pants:
    if pant.category == "male":
        print(pant.product_summary())
"""
shirts = [
    Product("v-neck shirts", 5, 20, "male"),
    Product("blousers", 5, 50, "female")
]
for shirt in shirts:
    print(shirt.product_summary())
