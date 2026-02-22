# FOR LOOP TASK - ShadowFox Internship

import random


# -------------------------------
# Program 1: Dice Simulation
# -------------------------------

print("DICE SIMULATION")

rolls = []
count_6 = 0
count_1 = 0
two_6_in_row = 0

# roll dice 20 times
for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        count_6 += 1

    if roll == 1:
        count_1 += 1

# check two 6s in a row
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i+1] == 6:
        two_6_in_row += 1


print("All rolls:", rolls)
print("Number of times rolled 6:", count_6)
print("Number of times rolled 1:", count_1)
print("Two 6s in a row:", two_6_in_row)



# -------------------------------
# Program 2: Jumping Jacks
# -------------------------------

print("\nJUMPING JACKS WORKOUT")

total = 0

for i in range(1, 11):

    total += 10

    print("You completed", total, "jumping jacks")

    if total == 100:
        print("Congratulations! You completed the workout")
        break

    tired = input("Are you tired? (yes/no): ")

    if tired.lower() == "yes":
        skip = input("Do you want to skip remaining? (yes/no): ")

        if skip.lower() == "yes":
            print("You completed total", total, "jumping jacks")
            break

        else:
            continue

    else:
        print("Remaining:", 100 - total)