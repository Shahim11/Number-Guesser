import random


# Define function for guessing a number game.
def game():
    low = 1
    high = 50
    correct_answer = random.randint(low, high)

    print("- - - - Game Started - - - -")
    print("Caution: You will have 5 chances to guess a number between 1 and 50.")
    print("\n")  # For new line

    for i in range(5):
        guess = int(input("Enter your guess: "))

        if guess < correct_answer:
            print("Correct answer is greater!")
        elif guess > correct_answer:
            print("Correct answer is smaller!")
        else:
            print("Congratulations! You guessed the correct number!")
            break

    if i == 4:
        print("-----------------------------------------------------")
        print("Sorry, you lost! The correct answer was {}.".format(correct_answer))


# Define function for guessing a number game.
def menu():
    option = 10  # Arbitrary value for entering while loop
    # Loop to repeatedly display the menu
    while option != 0:  # Exit loop when the value is 0
        print("What do you wish to do?")
        print("1 -> Start the Game")
        print("0 -> End the Game")
        option = int(input("Select option: "))
        print("\n")  # For new line

        # Check chosen option and call the appropriate function
        if option == 0:
            print("Thank you for playing the game.")
        elif option == 1:
            # Call the game() function
            game()
            print("\n")  # For new line
        else:
            print("Non-existing Option.")
            print("\n")  # For new line


print("\n")  # For new line
print("****** Welcome to the Number Guesser App! ******")
print("\n")  # For new line
# Call the menu() function
menu()
