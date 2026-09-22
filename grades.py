# grade checker
grade_input = (input("enter yo grade: "))

try:
    # convert input to integer
    grade = int(grade_input)
    # determine if input is valid
    if 0 <= grade <= 100:
        print("Valid grade.")
    else:
        print("Invalid grade. Grade must be between 0 and 100. ")

except ValueError:
    # runs if not a whole number
    print("Invalid input. Please enter a whole number.")