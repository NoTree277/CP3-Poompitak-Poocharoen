def name_input(lst):
    x = input("Name : ")
    lst.append(x)
    return x


def show(lst):
    list_count = len(lst)
    b = 0
    c = 1
    for i in range(list_count):
        print(f"({c}) {lst[b]}")
        c += 1
        b += 1


def quit():
    print("Bye")
    exit(0)


def delete(lst):
    while True:
        delete_v = input("Number? : ")
        x = delete_v.isdecimal()
        if x is False:
            print("Not a number")
        elif x is True:
            y = int(delete_v)
            if y > len(lst):
                print("Not in range")
            else:
                delete_n = int(delete_v)
                delete_n -= 1
                del lst[delete_n]
                show(lst)
                break


lst = []
while True:
    list_n = len(lst)
    if list_n == 0:
        user = input("(N)ew (Q)uit : ")
        if user == "N" or user == "n":
            print(name_input(lst), "added")
        elif user == "Q" or user == "q":
            print(quit())
    else:
        menu2 = input("(N)ew (S)how (D)elete (Q)uit : ")
        if menu2 == "N" or menu2 == "n":
            print(name_input(lst), "added")
        elif menu2 == "S" or menu2 == "s":
            show(lst)
        elif menu2 == "D" or menu2 == "d":
            delete(lst)
        elif menu2 == "Q" or menu2 == "q":
            quit()
