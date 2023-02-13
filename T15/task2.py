#programe to check if year user inputs and years after within defined check count are a leap year or not
start_year = int(input("What year do you want to start with?: "))
years_check = int(input("How many years do you want to check?: "))

#checks conditions starting with user start year up until start year plus number of years requested to check
for year in range(start_year, start_year + years_check):
    if year % 4 == 0:           #calculation to detirmine if a leap year
        print(f'{year} is a leap year')
    else:
        print(f'{year} isn\'t a leap year')