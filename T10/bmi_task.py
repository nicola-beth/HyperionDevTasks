weight = float(input("How much do you weigh? (in kg): ")) #float user input for weight
height = float(input("How tall are you? (in m): ")) #float user input for height
bmi = round(weight / (height*2), 3) #bmi calc
bmi_outcome = "" #empty string for bmi outcome

if bmi >= 30:
    bmi_outcome = "obese"
elif bmi >= 25:
    bmi_outcome = "overweight"
elif bmi >= 18.5:
    bmi_outcome = "normal"
else:
    bmi_outcome = "underweight"

print(f'Your BMI is {bmi}, this classifies you as {bmi_outcome}.')