# Using the variable below, print "Hello, world!"

greeting = "hello, world"
print(greeting, "!")

# Ask the user for their name, and then greet the user,using their name
# as part of the greeting.
# The name should be in title case, and shouldn't be surrounded by
# any excess white space.
name = input("Enter your name (first or given name)")
name = name.title()
print("Hiya, ", name.title())

# Concatenate the string "I am " and the integer 29 to produce a string
# which reads "I am 29"
print("I am", str(29))

#Format and print the information below using string interpolation:
title = "Joker"
director = "Todd Phillips"
release_year = 2019

message = "The movie, {} was directed by {} and released during {}".format(title, director, release_year)
print(message)
