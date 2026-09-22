# pin validation
pin = input("Enter a 6-digit pin: ")

# check formatting + content
if len(pin) == 6 and pin.isdigit():
    print("Valid Pin.")
else:
    print("Invalid Pin. Must be 6 DIGITS BRO")
