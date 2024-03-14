def even_odd(number):
    return number / 2


ans = even_odd(int(input("number: ")))
if ans % 2 == 0:
    print("even")
else:
    print("odd")
