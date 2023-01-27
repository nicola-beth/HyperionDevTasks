item_price = float(input("What is the price of the item? (in R): ")) #user input for item cost
distance = float(input("How far away is the delivery address? (in km): ")) #user input for delivery distance

vehicle_cost = 0
vehicle = input("How would you like your parcel to be sent? Air/Freight").lower() #user input for how want parcel to be sent
if vehicle == "air":
    vehicle_cost = 0.36
else:
    vehicle_cost = 0.25

insurance_cost = 0
insurance = input("What insurance would you like? Full/Limited").lower() #user input for preferred insurance
if insurance == "full":
    insurance_cost = 50.00 * distance
else:
    insurance_cost = 25.00 * distance

gift_cost = 0
gift = input("Is this a gift? Y/N").lower() #user input to detirmine if its a gift
if gift == "y":
    gift_cost == 15.00
else:
    gift_cost = 0

type_cost = 0
type = input("How would you like your parcel to be sent? Priority/Standard").lower() #user input to find out if want priority post
if type == "priority":
    type_cost = 100
else:
    type_cost = 20

delivery_cost = vehicle_cost + insurance_cost + gift_cost + type_cost #add all delivery costs together
final_cost = item_price + delivery_cost

print(f"Total cost of your parcel is {final_cost}")