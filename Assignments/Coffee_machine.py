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
print(money, "of money")
user_input = str(input("Write action (buy, fill ,take): "))
if user_input == "buy":
    user_want = int(input("What do you want to buy? 1 - espresso, 2 - latte , 3 - cappuccino:"))
    if user_want == 1:  # buy espresso
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
    elif user_want == 2:  # buy latte
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7
    elif user_want == 3:  # buy cappuccino
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6
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
print("The coffee machine has:")
print(water, "of water")
print(milk, "of milk")
print(coffee_beans, "of coffee beans")
print(cups, "of disposable cups")
print(money, "of money")
