#function to calc cost of hotel based on user input for total number of nights
def hotel_cost(nights):
    hotel_total = nights * 150.75            #hotel costs £150.75/night
    print(f'Cost of the hotel will be £{hotel_total}.')     #print hotel cost - need print statement in function as variable does not exist outside
    return hotel_total          #return variable value to be used outside of function

#function to calc cost of plane flights based on user input for destination
def plane_cost(city):
    if city == "Madrid":
        flight_cost = 120
    elif city == "Tokyo":
        flight_cost = 550
    elif city == "Marrakesh":
        flight_cost = 333
    print(f"Cost of the flights will be £{flight_cost}.")           #print flights cost
    return flight_cost          #return variable value to be used outside of function

#function to calc cost of car rental based on user input for total number of days needed for
def car_rental(car_days):
    car_total = car_days * 50          #car costs £50/day
    print(f"Cost of the car rental will be £{car_total}.")      #print car cost
    return car_total            #return variable value to be used outside of function

#function to call other functions to calc total cost of holiday
def holiday_cost(nights, city, car_days):
    holiday_total = hotel_cost(nights) + plane_cost(city) + car_rental(car_days)        #use return values of other functions to sum
    print(f"Overall, the total cost of your holiday will be £{holiday_total}")      #print total cost of holiday


user_nights = int(input("How many nights would you like to go away for?: "))

user_destination = input("What city would you like to fly to? Madrid/Tokyo/Marrakesh: ")

user_car_days = int(input("How many days would you like to rent a car for?: "))

holiday_cost(user_nights, user_destination, user_car_days)