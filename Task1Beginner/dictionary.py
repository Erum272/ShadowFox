# DICTIONARY TASK - ShadowFox Internship


# ----------------------------
# Program 1: Friends name length
# ----------------------------

friends = ["Amit", "Rahul", "Priya", "Sneha", "John"]

result = []

for name in friends:
    result.append((name, len(name)))

print("Friends and name length:")
print(result)



# ----------------------------
# Program 2: Expense Tracker
# ----------------------------

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transport": 500,
    "Attractions": 300,
    "Misc": 200
}


partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transport": 600,
    "Attractions": 400,
    "Misc": 150
}


# Total expenses

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour total expense:", your_total)
print("Partner total expense:", partner_total)


# Who spent more

if your_total > partner_total:
    print("You spent more")

else:
    print("Partner spent more")


# Find biggest difference

max_diff = 0
max_category = ""

for category in your_expenses:

    diff = abs(your_expenses[category] - partner_expenses[category])

    if diff > max_diff:
        max_diff = diff
        max_category = category


print("Biggest difference in:", max_category)
print("Difference amount:", max_diff)