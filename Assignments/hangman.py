import random

llist = ["python", "java", "kotlin", "javascript"]


def hangman():
    print("H A N G M A N")
    random_w = random.choice(llist)
    hidden_w = "-" * len(random_w)
    hp = 8
    guess_list = []
    while True:
        if hp == 0:
            print("You are hanged")
            break
        if hidden_w == random_w:
            print(" ")
            print(random_w)
            print("You guessed the word!")
            print("You survied!")
            break
        print(" ")
        print(hidden_w)

        input_guess = str(input("Input a letter: >"))
        if input_guess in guess_list:
            hp -= 1
            print("No improvements")
        if input_guess in random_w:
            correct_w = ""
            for i in range(len(random_w)):
                if input_guess == random_w[i]:
                    correct_w += input_guess
                    guess_list.append(input_guess)
                else:
                    correct_w += hidden_w[i]
            hidden_w = correct_w
        else:
            print("No such letter in the word")
            hp -= 1


hangman()
