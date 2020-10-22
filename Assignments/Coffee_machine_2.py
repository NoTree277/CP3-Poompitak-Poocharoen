water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550
print("The coffee machine has:")
print(water, "of water")
print(milk, "of milk")
print(coffee_beans, "of coffee beans")
print(cups, "of disposable cups")
print(f"${money} of money")

while True:
    user_input = str(input("Write action (buy, fill ,take, remaining, exit): "))
    if user_input == "buy":
        user_want = int(input("What do you want to buy? 1 - espresso, 2 - latte , 3 - cappuccino:"))
        if user_want == 1:  # buy espresso
            if water >= 250 and coffee_beans >= 16 and cups >= 1:
                water -= 250
                coffee_beans -= 16
                cups -= 1
                money += 4
                print("I have enough resources, making you a coffee!")
            elif water < 250:
                print("Sorry, not enough water!")
            elif coffee_beans < 16:
                print("Sorry, not enough coffee beans!")
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
        elif user_want == 2:  # buy latte
            if water >= 350 and milk >= 75 and coffee_beans >= 20 and cups >= 1:
                water -= 350
                milk -= 75
                coffee_beans -= 20
                cups -= 1
                money += 7
                print("I have enough resources, making you a coffee!")
            elif water < 350:
                print("Sorry, not enough water!")
            elif milk < 75:
                print("Sorry, not enough milk!")
            elif coffee_beans < 20:
                print("Sorry, not enough coffee beans!")
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
        elif user_want == 3:  # buy cappuccino
            if water >= 200 and milk >= 100 and coffee_beans >= 12 and cups >= 1:
                water -= 200
                milk -= 100
                coffee_beans -= 12
                cups -= 1
                money += 6
                print("I have enough resources, making you a coffee!")
            elif water < 200:
                print("Sorry, not enough water!")
            elif milk < 100:
                print("Sorry, not enough milk!")
            elif coffee_beans < 12:
                print("Sorry, not enough coffee beans!")
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
    elif user_input == "fill":
        fill_water = int(input("Write how many ml of water do you want to add: "))
        fill_milk = int(input("Write how many ml of milk do you want to add: "))
        fill_coffee = int(input("Write how many grams of coffee do you want to add: "))
        fill_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        water += fill_water
        milk += fill_milk
        coffee_beans += fill_coffee
        cups += fill_cups

    elif user_input == "take":
        print("I gave you $", money)
        money -= money

    elif user_input == "remaining":
        print("The coffee machine has:")
        print(water, "of water")
        print(milk, "of milk")
        print(coffee_beans, "of coffee beans")
        print(cups, "of disposable cups")
        print(f"${money} of money")

    elif user_input == "exit":
        break

