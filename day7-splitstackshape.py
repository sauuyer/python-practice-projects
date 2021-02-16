name = input("Enter your first and last name in this format -> Lastname, Firstname: ")
name = name.title().strip()
split_name = name.split(",")

print(split_name)


num_list = [1, 2, 3, 4, 5]
str_list = []
for each in num_list:
    str_num = str(each)
    str_list.append(str_num)
str_list = " | ".join(str_list)
print(str_list)


quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

for quote in quotes:
    print(quote.strip("'"))



