swimming_time = float(input("What was your time for swimming? (in mins): ")) #user input for swimming time
cycling_time = float(input("What was your time for cycling? (in mins): ")) #user input for cycling time
running_time = float(input("What was your time for running? (in mins): ")) #user input for running time
total_time = swimming_time + cycling_time + running_time #calc to add all triathlon times

award_type = "" #empty varaible for triathlon award

if total_time <= 100:
    award_type = "Provincial Colours"
elif total_time > 100 and total_time <= 105:
    award_type = "Provincial Half Colours"
elif total_time > 105 and total_time <= 110:
    award_type = "Provincial Scroll"
else:
    award_type = "nothing"

print(f"It took you {total_time} minutes to complete the triathlon. You therefore were awarded {award_type}.")