import math


def mysqrt(a):
    x = a-1
    epsilon = 0.0000001
    if x == 0:
        x = 1
        a = 1
        y = (x + a / x) / 2
        return y
    y = (x + a / x) / 2
    while x != 0:
        x = y
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
    return y


def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    a_c = 1
    while a_c <= 9:
        if a_c == 1 or a_c == 4 or a_c == 9:
            print(f"{a_c:3.1f} {mysqrt(a_c):<13.1f} {math.sqrt(a_c):<13.1f} {math.sqrt(a_c) - mysqrt(a_c)}")
        elif a_c != 0:
            print(f"{a_c:3.1f} {mysqrt(a_c):<13.11f} {math.sqrt(a_c):13.11f} {math.sqrt(a_c) - mysqrt(a_c)}")
        a_c += 1


print(test_square_root())
