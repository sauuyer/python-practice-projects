# Create a movies list containing a single tuple
movies_list = [("The Seventh Seal", "Ingmar Bergman", 1957, 150000)]
print(movies_list)

# Gather input about movie details from user
title = input("Movie title: ")
director = input("Movie director: ")
year_released = input("Year released: ")
production_budget = input("Production budget: ")

movie_tuple = (title, director, year_released, production_budget)
movies_list.append(movie_tuple)

print(f"{movies_list[1][0]} was released in {movies_list[1][2]}!")

for movie in movies_list:
    print(movie)

del movies_list[0]
print("+++++")
print(movies_list)

