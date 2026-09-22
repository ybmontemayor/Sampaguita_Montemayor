# id checker
import re

id_num = input("Enter your ID number: ")

# checks for patterns (eg XXXX-XXXX)
valid_num_pat = r"\d{4}-\d{4}"

# check if it is valid
if re.fullmatch(valid_num_pat, id_num):
    print("Valid Student ID.")
else:
    print("Invalid Student ID.")
