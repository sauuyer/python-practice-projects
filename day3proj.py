def collect_name():
    name = input("Enter full name: ")
    name = name.title().strip()
    return name

def collect_wage():
    #wage = input("Enter the amount of money you make per hour: ")
    while True:
        try:
            wage = float(input("Enter hourly rate: "))
            break
        except ValueError:
            print("Enter a number (5 or 5.0, not five).")
            continue
    return wage


def collect_hours():
    while True:
        try:
            hours_worked = float(input("Enter the number of hours you worked this week: "))
            break
        except ValueError:
            print("Enter a number (5 or 5.0, not five).")
            continue
    return hours_worked

collected_name = collect_name()
collected_wage = collect_wage()
collected_hours = collect_hours()

this_weeks_earnings = collected_wage * collected_hours

print(collected_name, "earned $", this_weeks_earnings, "this week.")
