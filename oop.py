# object orieneted programming

class Fruits:
    def __init__(self):
        self.name = "apple"
        self.color = "red"


fruits = Fruits()
fruits.name = "mango"
fruits.color = "yellow"
print(fruits.name)

#projecttwo

class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color


fruit1 = Fruits("apple","red")
fruit2 = Fruits("banana","yellow")

print(f" fruit name one is: {fruit1.name} " )