employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

# Print how much each employee is due to be paid at the end of the week in a nice, readable format.
for employee in employees:
    print(f"{employee[0]} will be paid {employee[1]*employee[2]} at the end of this week.")

# For the employees above, print out those who are earning an hourly wage above average.
wages = []
# Gather all wages from the data set to find the average wage and the number of employees
for employee in employees:
    wages.append(employee[1])
average_wage = sum(wages)/len(wages)
print(f"The average wage of employees in this group is: {average_wage}")

# Return employee names for those that earn a higher than average wage
for employee in employees:
    if employee[1] > average_wage:
        wage_difference_from_average = employee[1] - average_wage
        print(f"{employee[0]} earns a higher than average wage by ${wage_difference_from_average}")
