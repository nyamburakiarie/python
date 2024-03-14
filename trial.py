# def sylvia(mark1,mark2):
#     return mark1/mark2
#
# div = sylvia(15,5)
#

# def check(x):
#     return x%2
#
# rem = check(int(input("number: ")))
#
# if rem == 0:
#     print("even")
# # else:
# #     print("odd")
# #
#
#
#
# def number(x):
#     return x
# value = number(int(input("value: ")))
# if value < 0:
#     print("invalid answer")
# elif value > 100:
#     print("invalid answer")
# else:
#     print("valid")

class People:
    def dan(self):
        print("can speak")

    def griffo(self):
        print("can walk")

    def sylvia(self):
        print("can talk")

pp = People()

class Person(People):
    def ezekiel(self):
        print("can scold")

ps = Person()

print(ps.ezekiel(), ps.sylvia(),)





