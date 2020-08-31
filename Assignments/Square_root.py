import math


def mysqrt(a):
    x = a
    y = (x + a / x) / 2
    epsilon = 0.0000001

    while abs(y - x) > epsilon:
        x = y
        y = (x + a / x) / 2

    return y


def test_square_root():
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    a_c = 1
    while a_c >= 9:
        a_c += 1
        print(a_c)


print(mysqrt(9))
