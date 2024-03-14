class Person:
    def james(self):
        print("can talk")


    def tom(self):
        print("speaks english")

class Parrot(Person):
    def kilo(self):
        print("can walk")


yy = Parrot()
print(yy.james(),yy.tom(), yy.kilo(),  )