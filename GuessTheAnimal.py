a = True
while a == True:
    print("\n")
    print(
        "Hello, Welcome to my Guessing Game!\nIn this game, you have to guess the world's best midfielder's name and you can guess maximum 3 times.")
    print("\n")
    Player = input("Enter your name: ")
    print("\n")
    print("Best of luck, " + Player + ". Let's start the game. ")
    print("\n")

    guessing_word = "Leopard"
    guess = ""
    guess_count = 0
    total_guess = 3
    guess_limit = 3
    out_of_limit = False

    while guess != guessing_word and not out_of_limit:
        if guess_count < guess_limit:
            print("Number of tries left: " + str(total_guess))
            guess = input("Enter the animal name: ").capitalize()
            guess_count += 1
            total_guess -= 1
        else:
            out_of_limit = True

    print("\n")
    if out_of_limit:
        print("Bad luck " + Player + ", you lose!")
    else:
        print("Congrats " + Player + ", you win!")

    answer = (input("Play again? (y/n): "))
    if answer == "y":
        continue
    else:
        exit()