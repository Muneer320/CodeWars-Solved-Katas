def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

if validate_pin(1355):
    print("It's true")
else:
    print("It's false")
