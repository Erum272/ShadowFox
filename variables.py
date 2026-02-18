# variables.py
# ShadowFox Python Development Intern

# Task 1: Working with pi
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))


# Task 2: Trying to use 'for' as a variable name
# 'for' is a reserved keyword in Python, so it cannot be used as a variable name.
# If we write: for = 4
# It will give a SyntaxError because Python uses 'for' for loops.


# Task 3: Simple Interest Calculation
principal = 1000
rate = 5
time = 3

simple_interest = (principal * rate * time) / 100

print("\nSimple Interest Details:")
print("Principal:", principal)
print("Rate:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:", simple_interest)