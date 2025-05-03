# Open the file and read the grades
grades = []
with open('grades.txt', 'r') as file:
    for line in file:
        try:
            grade = float(line.strip())  # Convert each line to a float
            grades.append(grade)
        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")

# Display individual grades
print("Grades:")
for g in grades:
    print(g)

# Calculate statistics
total = sum(grades)
count = len(grades)
average = total / count if count > 0 else 0

# Display results
print(f"\nTotal: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
