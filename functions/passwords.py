import random
import string

def create_new():
    is_exit = True

    # A function to shuffle all the characters of a string
    def shuffle(string):
        tempList = list(string)
        random.shuffle(tempList)
        return ''.join(tempList)

    # Input for the desired length of uppercase letters
    print("\n------------------ Welcome to generator password -----------------------\n\n\n")
    while is_exit:
        letter = int(input("Type how many letters in your password? "))
        choose = input("\n\n\nWant to choose the percentage of each characters in your password?(y/n) ")
        if choose == 'y' or choose == 'yes':
            special_percent = int(input("\nPercentage of special characters in your password? "))/100
            lowercase_percent = int(input("Percentage of lowercase letters in your password? "))/100
            uppercase_percent = int(input("Percentage of uppercase letters in your password? "))/100
            numbers_percent = int(input("Percentage of numbers characters in your password? "))/100
            summing = special_percent+lowercase_percent+uppercase_percent+numbers_percent
            if summing != 1:
                print(summing)
                new_lowercase_percent = (1-summing)
                lowercase_percent = new_lowercase_percent+lowercase_percent
        else:
            # Define the desired distribution percentages
            special_percent = 0.10  # 20% special characters
            lowercase_percent = 0.60  # 60% lowercase letters
            uppercase_percent = 0.10  # 20% uppercase letters
            numbers_percent = 0.20  # 20% numbers characters


        # Calculate the total length of the password
        total_length = letter

        # Calculate the number of characters for each category based on percentages
        num_special = int(total_length * special_percent)
        num_lowercase = int(total_length * lowercase_percent)
        num_uppercase = int(total_length * uppercase_percent)
        num_numbers = int(total_length * numbers_percent)

        # Generate characters for each category
        special_chars = ''.join(random.choice(string.punctuation) for n in range(num_special))
        lowercase_chars = ''.join(random.choice(string.ascii_lowercase) for n in range(num_lowercase))
        uppercase_chars = ''.join(random.choice(string.ascii_uppercase) for n in range(num_uppercase))
        num_chars = ''.join(random.choice(string.digits) for n in range(num_numbers))

        # Combine the characters from all categories
        password = special_chars + lowercase_chars + uppercase_chars + num_chars

        print('\nOriginal Password:', password)

        # Shuffle the password
        shuffled_password = shuffle(password)

        # Output the shuffled password
        print('\nShuffled Password:', shuffled_password)

        answer=input("Want to do a new password?(y/n):")

        if answer == 'y' or answer == 'yes':
            is_exit = True
        else:
            print('Byee!\n\n')
            is_exit = False