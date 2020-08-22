# 1 Particles
"""spin = input("Spin: ")
charge = input("Charge: ")
if spin == "1/2" and charge == "-1/3":
    print("Strange Quark")
if spin == "1/2" and charge == "2/3":
    print("Charm Quark")
if spin == "1/2" and charge == "-1":
    print("Electron Lepton")
if spin == "1/2" and charge == "0":
    print("Neutrino Lepton")
if spin == "1" and charge == "0":
    print("Photon Boson") """

# 2 Calculator
"""first_num = float(input())
second_num = float(input())
operation = str(input())
if operation == "+":
    print(first_num+second_num)
elif operation == "-":
    print(first_num-second_num)
elif operation == "/" and second_num != 0:
    print(first_num/second_num)
elif operation == "*":
    print(first_num*second_num)
elif operation == "mod" and second_num != 0:
    print(first_num % second_num)
elif operation == "pow":
    print(first_num ** second_num)
elif operation == "div" and second_num != 0:
    print(first_num // second_num)
elif second_num == 0 and operation == "+" "-" "*" "/" "mod" "pow" "div":
    print("Division by 0!")
else:
    print("Error") """

# 3 Farm
"""money = int(input("Your money: "))
if money >= 6769:
    Num = money//6769
    if Num == 1:
        print(Num, "Sheep")
    else:
        print(Num, "Sheeps")
elif money >= 3848:
    Num = money // 3848
    if Num == 1:
        print(Num, "Cow")
    else:
        print(Num, "Cows")
elif money >= 1296:
    Num = money // 1296
    if Num == 1:
        print(Num, "Pig")
    else:
        print(Num, "Pigs")
elif money >= 678:
    Num = money // 678
    if Num == 1:
        print(Num, "Goat")
    else:
        print(Num, "Goats")
elif money >= 23:
    Num = money // 23
    if Num == 1:
        print(Num, "Chicken")
    else:
        print(Num, "Chickens")
else:
    print("None") """

# 4 Day
"""offset = int(input("Offset: "))
ref_time_hour = 10
if offset >= 0:
    time = ref_time_hour+offset
    if time <= 23:
        print("Tuesday")
    elif time >= 24:
        print("Wednesday")
elif offset < 0:
    time = ref_time_hour+offset
    if time >= 0:
        print("Tuesday")
    elif time <= -1:
        print("Monday") """


# 5
"""
def is_even(number):
    x = number % 2
    if x == 0:
        return print("True")
    else:
        return print("False")


is_even(2)
is_even(9)
is_even(988) """

# 6
"""def is_leap_year(year):
    x = year % 4
    y = year % 100
    z = year % 400
    if x != 0 or z != 0:
        return print("False")
    elif y != 0:
        return print("True")
    else:
        return print("True")


is_leap_year(2020)
is_leap_year(1945)
is_leap_year(2000)"""

# 7
"""def interval_intersect(a, b, c, d):
    if b >= c:
        return print("True")
    else:
        return print("False")


interval_intersect(1, 5, 3, 4)
interval_intersect(1, 8, 9, 15)
interval_intersect(15, 22, 22, 26) """

# 8
"""def print_digits(number):
    if 0 <= number < 100:
        tens = number // 10
        ones = number % 10
        return print("The tens digit is",tens,"and the ones digits is",ones)
    else:
        return print("Error: Input is not a two digit number")
a = print_digits(95)
b = print_digits(100)
c = print_digits(-150) """

# 9
def smaller_root(a,b,c):
    