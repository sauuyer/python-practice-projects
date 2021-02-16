def user_input_word_checker():
    while True:
        try:
            entered_word = input("Enter a word to be counted: ")
            entered_word = entered_word.strip()
            length_of_entered_number = len(entered_word)
            print(f"The length of {entered_word} is {length_of_entered_number}.")
        except ValueError:
            print("Enter a number value (5 or 5.0, but not five).")
            continue


while True:
    user_interest = input("Would you like to enter a word to count it's letters? Enter yes or no.")
    if user_interest.lower().strip() == "yes":
        user_input_word_checker()
    elif user_interest.lower().strip() == "no":
        break
    else:
        continue

print("OK, bye.")

