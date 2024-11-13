import random
import string

alphabs = string.ascii_letters
numbers = string.digits 
special_chars = string.punctuation

# Updated combinations
combo_1 = alphabs + numbers
combo_2 = alphabs + special_chars
combo_3 = alphabs + numbers + special_chars

print("Welcome to the CLI-based Password Generator.\nDeveloped by PaomFarv.\n\nEnter (S) to start.\nEnter (Q) to quit.")
user_inp = input("Type Here: ").strip().upper()

if user_inp == 'S':
    print("How many digits do you want in your password? ")
    try:
        digits_pw = int(input("\nInsert the number: "))
    except ValueError:
        print("\nInvalid input. Input must be a number. Please try again.")
        exit()  # Exit if the input isn't valid

    print("\nWhat kind of Password do you want?\n")
    print("Enter (A) for only Letters.")
    print("Enter (B) for Letters and Numbers.")
    print("Enter (C) for Letters and Special Characters.")
    print("Enter (D) for all characters.")
    print("Enter (Q) to quit.")

    while True:
        user_Password = ''
        user_response = input("\nType in your Response Here: ").strip().upper()

        if user_response == "A":
            user_Password = ''.join(random.choice(alphabs) for _ in range(digits_pw))
            print(f"Here is your Password: {user_Password}")

        elif user_response == "B":
            user_Password = ''.join(random.choice(combo_1) for _ in range(digits_pw))
            print(f"Here is your Password: {user_Password}")

        elif user_response == "C":
            user_Password = ''.join(random.choice(combo_2) for _ in range(digits_pw))
            print(f"Here is your Password: {user_Password}")

        elif user_response == "D":
            user_Password = ''.join(random.choice(combo_3) for _ in range(digits_pw))
            print(f"Here is your Password: {user_Password}")

        elif user_response == "Q":
            print("You have exited this Program.")
            break  # Exit the loop if user wants to quit

        else:
            print("Invalid Input. Please Try Again.")

else:
    print("You have exited this Program.")