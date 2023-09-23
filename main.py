def main_menu():
    print("\n" + "_" * 66)
    print("|" + " " * 64 + "|")
    print("|" + " " * 25 + "Welcome to the Main Menu" + " " * 15 + "|")
    print("|" + " " * 64 + "|")
    print("|" + "_" * 64 + "|" + "\n\n")

    print("1. Roll Dices")
    print("2. Create Password")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            from functions import dice
            dice.roll_dice()
        elif choice == "2":
            from functions import passwords
            passwords.create_new()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
