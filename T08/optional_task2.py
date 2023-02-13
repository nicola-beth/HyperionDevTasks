above_20degrees = False
weekend = False
sunny = False
shirt_type = ""
bottoms = ""
additional_clothing = ""
temperature = float(input("What is the temperature in degrees?"))
if temperature > 20:
    above_20degrees = True
    shirt_type = "short-sleeved"
else:
    shirt_type = "long-sleeved"
time_of_week = input("Is it the weekend? Y/N").lower()
if time_of_week == "y":
    weekend = True
    bottoms = "shorts"
else:
    bottoms = "jeans"
sunny_outside = input("Is it sunny outside? Y/N").lower()
if sunny_outside == "y":
    sunny = True
    additional_clothing = "cap"
else:
    additional_clothing = "rain jacket"
print(f'Today, you should put on a {shirt_type} shirt and {bottoms}. Make sure you don\'t forget your {additional_clothing}!' )
