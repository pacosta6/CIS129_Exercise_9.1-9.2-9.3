import csv

# Open the CSV file in write mode (overwrite if exists)
with open('grades.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)


    while True:
        first = input("Enter student's first name (or type 'done' to finish): ")
        if first.lower() == 'done':
            break
        last = input("Enter student's last name: ")
        
        try:
            exam1 = int(input("Enter grade for Exam 1: "))
            exam2 = int(input("Enter grade for Exam 2: "))
            exam3 = int(input("Enter grade for Exam 3: "))
        except ValueError:
            print("Please enter valid integer grades.")
            continue

        # Write the student record to the CSV
        writer.writerow([first, last, exam1, exam2, exam3])

print("All student records have been saved to grades.csv.")

'Done'
