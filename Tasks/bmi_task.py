weight = float(input("How much do you weigh? (in kg): "))
height = float(input("How tall are you? (in m): "))
bmi = round(weight / (height*2), 3)
bmi_outcome = ""

if bmi >= 30:
    bmi_outcome = "obese"
elif bmi >= 25:
    bmi_outcome = "overweight"
elif bmi >= 18.5:
    bmi_outcome = "normal"
else:
    bmi_outcome = "underweight"

print(f'Your BMI is {bmi}, this classifies you as {bmi_outcome}.')