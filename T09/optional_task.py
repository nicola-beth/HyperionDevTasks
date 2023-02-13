final_wage = 0 #set final wage as empty variable
salesperson_monthly_fixed_salary = 2000 #set monlthy salary of salesperson as fixed variable
manager_hourly_salary = 40 #set hourly salary of manager as fixed variable

role = input("What is your job title? (Salespeson or Manager): ").lower() #user input for job title
if role == "salesperson":
    salesperson_monthly_gross_sales = int(input("What was the total of your gross sales this month?")) #user input for salesperson gross sales
    salesperson_monthly_commission = 0.08 * salesperson_monthly_gross_sales #calc for commission
    salesperson_monthly_total_salary = salesperson_monthly_fixed_salary + salesperson_monthly_commission #calc for total salespersons total salary
    final_wage = salesperson_monthly_total_salary
else:
    manager_hours = int(input("How many hours did you work this month?"))
    manager_monthly_total_salary = manager_hours * manager_hourly_salary
    final_wage = manager_monthly_total_salary

print(f"Your monthly wage this month is {final_wage}")