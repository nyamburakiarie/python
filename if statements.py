maths = 90
english = 71

if maths > 90:
    print("maths greater than 90")

elif maths < 90:
    print("maths less than 90")

else:
    print("maths  equals 90")
    # else should always be the last option

#
if maths > 70 and english > 70:
    print("success")
elif maths > 70 or english > 70:
    print("you passed either maths or english")

k = 7
l = 9

if not k > l:
    print("k is not greater than l")
    if l > k:
        print("l is greater than k")
