num1 = int(input("yo bruh gimme a number "))
num2 = int(input("yo bruh gimme another number "))
sum = num1 + num2 # global 1
diff = num1 - num2 # global 2
def calculate_sum():
    global sum
    print(f"sum is {sum}")
def calculate_difference():
    global diff
    print(f"difference is {diff}")
calculate_sum()
calculate_difference()
print("u welcom boss")