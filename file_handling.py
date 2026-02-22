# FILE HANDLING TASK - ShadowFox Internship


# open file in read mode
file = open("student_marks.csv", "r")

lines = file.readlines()

file.close()


# open new file in write mode
new_file = open("result.csv", "w")

# write header
new_file.write("Name,Math,Science,English,Total,Average\n")


# skip header line
for line in lines[1:]:

    data = line.strip().split(",")

    name = data[0]

    math = int(data[1])
    science = int(data[2])
    english = int(data[3])

    total = math + science + english

    average = total / 3

    new_file.write(f"{name},{math},{science},{english},{total},{average}\n")


new_file.close()

print("Result file created successfully")