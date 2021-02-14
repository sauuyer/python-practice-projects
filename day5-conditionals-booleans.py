# Prompt: Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.


def user_input_number_checker():
    while True:
        try:
            entered_number = float(input("Enter a number: "))
            break
        except ValueError:
            print("Enter a number value (5 or 5.0, but not five).")
            continue
    if entered_number > 0:
        print("That number is positive")
    elif entered_number < 0:
        print("That number is negative")
    else:
        print("That number is zero")


# create a while loop that will prompt the user to continue entering numbers into the checker function
# until they wish to exit the loop
while True:
    user_interest = input("Would you like to enter a number to be checked? Enter yes or no.")
    if user_interest.lower().strip() == "yes":
        user_input_number_checker()
    elif user_interest.lower().strip() == "no":
        break

user_input_number_checker()

