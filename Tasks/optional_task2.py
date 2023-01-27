above_20degrees = False
weekend = False
sunny = False
temperature = input("What is the temperature?")
if temperature > 20:
    above_20degrees = True
    print("Wear a short-sleeved shirt.")
else:
    print("Wear a long-sleeved shirt.")
time_of_week = input("Is it the weekend? Y/N").lower()
if input == y:
    weekend = True
    print("Wear shorts, it's the weekend!")
else:
    print("Wear jeans today.")
sunny_outside = input("Is it sunny outside? Y/N").lower()
if sunny_outside == y:
    sunny = True
    print("Put a cap on.")
else:
    print("Put on your rain jacket.")
print(f'Please ensure you follow the below:\n{} ')
