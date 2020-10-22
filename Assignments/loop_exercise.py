"""def fib(n):
    f = 0
    s = 1
    print(s, end=" ")
    for x in range(n):
        next = f + s
        print(next, end=" ")
        f = s
        s = next


print("fib(n) result:")
n = 0
while n < 10:
    fib(n)
    print("")
    n += 1"""

#################################################################


"""def diamond(n):
    space = n
    if n == 0:
        return
    for i in range(1, n+1):
        print(" " * space, end="")
        print("*" * (i * 2))
        space -= 1
    i = n
    space = 1
    while i >= 1:
        print(" " * space, end="")
        print("*" * (i * 2))
        space += 1
        i -= 1


print("diamond(n) result:")
for i in range(0, 8):
    diamond(i)
    print("")"""


#################################################################


"""def hailstone(n):
    while n >= 1:
        print(n, " ", end="")
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


print("hailstone(n) result:")
for i in range(1, 8):
    hailstone(i)
    print("")"""


#################################################################


"""def arith_sum(n):
    count = 1
    num_sum = 0
    while count <= n:
        print(count, end="")
        num_sum += count
        if count < n:
            print(" + ", end="")
        count += 1
    print(" = ", num_sum, end="")


print("arith_sum(n) result:")
for i in range(1, 10):
    arith_sum(i)
    print("")"""
