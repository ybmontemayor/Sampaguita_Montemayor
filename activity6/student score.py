# student score entry
score_input = input("Enter exam score: ")

try:
    # conversion to integer
    score = float(score_input)

    # range validation
    if 0 <= score <= 100:
        print("Valid score.")
    else
        print("Invalid score. Score must be between 0 and 100.")

except ValueError:
    # syntax check
    print("Invalid input. Please enter a number.")
