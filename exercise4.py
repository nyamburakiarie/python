# 0 - 39 E
# 40 - 50 D
# 51 - 60 C
# 61 - 70 B
# 71 - 100 A
#
# chemistry = 66
# physics = 50
# geography = 75
# mathematics = 80
# business = 69
#

chemistry = int(input('chemistry: '))
physics = int(input("physics: "))
geography = int(input("geography: "))
mathematics = int(input("mathematics: "))
business = int(input("business: "))

average = (chemistry + physics + geography + mathematics + business)/5
print(f'average = {average}')

if average < 0:
    print("invalid value")

if average > 100:
    print("invalid value")

if average > 70:
    print("grade A")

if average > 60 and  average< 71:
    print("grade B")

if average > 50 and average<61:
    print("grade C")

if average > 39 and average <51:
    print("grade D")

if average > 0 and average <40:
    print("grade E")