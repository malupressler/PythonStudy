import random

is_exit = True
min_val = 1
max_val = 1  # Initialize max_val to a default value

while is_exit:

    print("\nWelcome to dice roler!\n")
    start_dice = input("Want to start a dice?(yes or no) ")
    if start_dice == "y" or start_dice == "yes":
        max_val_input = input("Choose the maximum value of the dice: ")
        roll_again = "yes"
    else:
        print("Bye!")
        break

    while roll_again == "yes" or roll_again == "y":

        if max_val_input.isnumeric():
            max_val = int(max_val_input)
            print("Rolling The Dices...")
            print("The Values are:", max_val)
            print(random.randint(min_val, max_val))
            print(random.randint(min_val, max_val))
        else:
            print('Error: Please enter a numeric value for the maximum.')
            break  # Exit the loop if there's an error

        roll_again = input("Roll the same Dices Again? \n(yes or no):\n ")

        if roll_again.lower() == 'yes' or roll_again.lower() == 'y':
            continue  # Continue the loop
        elif roll_again.lower() == 'no' or roll_again.lower() == 'n':
            is_exit = True
            break  # Exit the loop
        else:
            is_exit = False
            print('Invalid input. Exiting.')
            break 

