'''
Write a program to determine whether an employee is owed any overtime.
You should ask the user how many hours the employee worked this week,
as well as the hourly wage for this employee.

If the employee worked more than 40 hours, you should print a message
which says the employee is due some additional pay, as well as the amount due.
The additional amount owed is 1.5x the employees hourly wage for each
hour worked over the 40 hours. Double overtime is 2x standard wage and is achieved after 80
hours are worked in a week.
'''


def overtime_calculator():
    while True:
        try:
            hours_worked_this_week = float(input("How many hours did you work this week?: "))
            break
        except ValueError:
            print("Enter a numerical value (5 or 5.0, but not five).")
            continue
    while True:
        try:
            hourly_wage = float(input("What is your hourly wage?: "))
            break
        except ValueError:
            print("Enter a numerical value (5 or 5.0, but not five).")
            continue
    if hours_worked_this_week > 80:
        standard_earnings = 40 * hourly_wage
        overtime_earnings = 40 * (hourly_wage * 1.1)
        double_overtime_earnings = (hours_worked_this_week - 80) * (hourly_wage * 2)
        total_weekly_earnings = standard_earnings + overtime_earnings + double_overtime_earnings
        print(f"You earned {double_overtime_earnings} in double overtime, plus {overtime_earnings} in overtime earnings, and {standard_earnings} at your standard rate. Your total earnings this week is: {total_weekly_earnings}.")
    elif hours_worked_this_week > 40:
        standard_earnings = 40 * hourly_wage
        overtime = (hours_worked_this_week - 40) * (hourly_wage * 1.5)
        total_pay = standard_earnings + overtime
        print(f"You earned {overtime} in overtime pay this week. Total pay earned this week is {total_pay}.")
    else:
        earnings = hours_worked_this_week * hourly_wage
        print("This week you earned: $", earnings, ". With no overtime.")


overtime_calculator()
