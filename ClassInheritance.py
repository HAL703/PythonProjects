"""PROPERTIES"""

class Product:
    def __init__(self, price):
        self.price = price
#YOU CAN DO THE FOLLOWING CODES TO SOLVE THE ISSUE
    @property #DECORATOR
    def price(self):
        return self.__price #READ ONLY IN HERE
    #price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Price can't be 0")
        self.__price #WRITES
#^ "UNPYTHONIC"
    price = property(get_price, set_price)
#USE DECORATOR WHICH MAKES THE ABOVE STATEMENT USELESS

product = Product(40)
product.price = 150
print(product.price)

"""INHERITANCE"""
class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")
#THIS DOES WHAT THE TWO DOWN BELOW DO IN ONE CLASS
class Mammal(Animal): #Mammal IS an animal
    def eat(self):
        print("eat")
    def walk(self):
        print("walk")

class Fish(Animal): #Fish IS an animal
    def eat(self):
        print("eat")
    def swim(self):
        print("swim")

m = Mammal()
m.eat

# isinstance() is useful

# o = object() creates empty object

"""ONE CONSTRUCTOR OVER ANOTHER OVERRIDES A PREVIOUS CONSTRUCTOR"""

super().__init__() # GIVES ACCESS TO ANIMAL CLASS
#PUT SUPER LAST TO MAKE THAT CLASS GO FIRST

"""IF YOU DON'T USE MULTIPLE OR MULTI-LEVEL INHERITANCE APPROPRIATELY, BAD BAD""""