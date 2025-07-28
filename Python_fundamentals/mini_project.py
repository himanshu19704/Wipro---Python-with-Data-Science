# ------------------------------------------------------
# MINI PROJECT 1

# Create a python program that suggests transport mode based on distance
distance = int(input("\nMini Project 1: How far would you like to travel in miles? "))
if distance < 3:
    print("I suggest Bicycle to your destination")
elif 3 <= distance < 300:
    print("I suggest Motor-cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# ------------------------------------------------------
# MINI PROJECT 2

# Server cost calculation program
hourly_rate = 0.51

cost_per_day = hourly_rate * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30
budget = 918
days_with_budget = budget / cost_per_day

print("\nMini Project 2: Server Cost Calculation")
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate the server for {days_with_budget:.2f} days.")
