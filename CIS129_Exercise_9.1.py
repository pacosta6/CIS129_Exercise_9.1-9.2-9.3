with open('grades.txt', 'w') as file:
    while True:
        grade = input("Enter a grade (or type 'done' to finish): ")
        if grade.lower() == 'done':
            break
        # Optionally validate that input is a number
        try:
            float(grade)  # just to check if it's a valid number
            file.write(grade + '\n')
        except ValueError:
            print("Please enter a valid number or 'done'.")
Done
