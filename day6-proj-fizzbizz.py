for number in range(1, 16):
    if number % 5 == 0 and number % 3 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

