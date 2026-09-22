# payment method checker
user_meth = input("Enter payment method: ").strip().lower()

# valid values
valid_meth = ("cash", "card", "gcash")

# validation
if user_meth in valid_meth:
    print("Valid payment method.")
else:
    print("Invalid payment method.")