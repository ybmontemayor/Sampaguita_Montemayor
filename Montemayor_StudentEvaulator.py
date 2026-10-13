# Montemayor, Yianni Jairo B.
# 8-Sampaguita

perf = ""
avg = 0

def display_header():
    print("Performance Evaluation")
    print("")
    print("==============================================================")
    print("")

display_header()

name = input("What is your name? (First, Last) ")
s1 = int(input("Enter score for assessment #1: "))
s2 = int(input("Enter score for assessment #2: "))
s3 = int(input("Enter score for assessment #3: "))
scores = [s1, s2, s3] # global
def evaluate_performance():
    avg = sum(scores) / 3
    if 90 <= avg <= 100:
        perf = ("Outstanding")
    elif 85 <= avg <= 89:
        perf = ("Very Satisfactory")
    elif 80 <= avg <= 84:
        perf = ("Satisfactory")
    elif 75 <= avg <= 79:
        perf = ("Fairly Satisfactory")
    elif avg < 75:
        perf = ("Needs Improvement")
    else:
        print("Please enter a value between 0 and 100")
evaluate_performance()
def display_report():
    print("=============================================")
    print(f"{name}")
    print(f"{s1} - {s2} - {s3}")
    print(f"{avg}")
    print(f"{perf}")
display_report()