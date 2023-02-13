#=====Import Libraries+++++++
import math
#========The beginning of the class==========
class Shoe:
    #contructor with shoe parameters
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass
    #method to return cost of shoe
    def get_cost(self):
        return self.cost
        pass
    #method to return quantity of shoe
    def get_quantity(self):
        return self.quantity
        pass
    #return new shoe data in a string
    def new_shoe_data(self):
        return f'''{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}'''

    #return attributes of shoes in easy to read format
    def __str__(self):
        output = f'''Country: {self.country}
Code: {self.code}
Product: {self.product}
Cost: {self.cost}
Quantity: {self.quantity}
======================================
        '''
        return output
        pass

#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============

#Function to read shoe data from txt file
def read_shoes_data():
    read_inventory = open("inventory.txt", "r")
    next(read_inventory)
    inventory_data = read_inventory.readlines()
    for line in inventory_data:
        #Try/Except for error handling of txt file not existing or in wrong format
        try:
            split_data_inventory = line.strip("\n").split(",")
            country = split_data_inventory[0]
            code = split_data_inventory[1]
            product = split_data_inventory[2]
            cost = int(split_data_inventory[3])     #cast to int for later calculations
            quantity = int(split_data_inventory[4])     #cast to int for later calculations
            shoe_list.append(Shoe(country, code, product, cost, quantity))
        except:
            print("Error when getting data from .txt file")
        finally:
            read_inventory.close()
    pass

#Function to add new shoes via user inputs
def capture_shoes():
    new_country = input("Enter country where the shoe is stocked: ")
    new_code = input("Enter shoe code: ")
    new_product = input("Enter shoe product name: ")
    new_cost = input("Enter cost of the shoes: ")
    new_quantity = input("Enter quantity of shoes we have stocked: ")
    shoe_list.append(Shoe(new_country, new_code, new_product, new_cost, new_quantity))      #Append to shoe list
    update_file()
    pass

#Return every shoe in the file & their attributes
def view_all():
    for item in shoe_list:
        print(item)
    pass

#Function to update file once new Shoe is added
def update_file():
    write_inventory = open("inventory.txt", "w")
    write_inventory.write("Country,Code,Product,Cost,Quantity")
    for item in shoe_list:
        write_inventory.write(f"\n{item.new_shoe_data()}")
    write_inventory.close()
    read_shoes_data()
    pass

#Function to return shoe with loewest quantity and ask user if theuld like to add more stock, replacing new quantity in file
def re_stock():
    quantity_dict = {}
    for index, item in enumerate(shoe_list):
        quantity_dict[index] = item.quantity
    lowest_quantity = min(quantity_dict.values())       #math function to return min number in a list
    for index, quantity in quantity_dict.items():
        if quantity == lowest_quantity:
            print(shoe_list[index])
            user_restock = input("Would you like to restock this item? Y/N: ").lower()
            if user_restock == "y":
                user_quantity_restock = int(input("How many would you like to add?: "))
                shoe_list[index].quantity = lowest_quantity + user_quantity_restock     #Add new quantity to existing quantity
                update_file()
            elif user_restock == "n":
                print("Not restocking this item.")
            else:
                print("Unrecognised input.")

#Function to return shoe details when user enters shoe code
def seach_shoe():
    user_shoe_code = input("Enter shoe code: ")
    for item in shoe_list:
        if item.code == user_shoe_code:
            print(item)
    pass

#Function to print out the total value held of each shoe (total value = quantity * cost)
def value_per_item():
    read_shoes_data()             #Ensure new data is read before calculating value (i.e. addition of new shoe)
    print("Total value of each shoe held:\n")
    for item in shoe_list:
        total_value = item.quantity * item.cost
        print(f"{item.product}: £{total_value}")
    pass

#Function to return shoe with the highest quantity & print it as "for sale"
def highest_qty():
    quantity_dict = {}
    for index, item in enumerate(shoe_list):
        quantity_dict[index] = item.quantity
    highest_quantity = max(quantity_dict.values())      #math function to return min number in a list
    for index, quantity in quantity_dict.items():
        if quantity == highest_quantity:
            print("----FOR SALE----")
            print(shoe_list[index])
    pass

#==========Main Menu=============
#While statement to ask for User input for required action/output - explaining to User they need to load data first
while True:
    try:
        choice = input('''Welcome to Shoe database, before you can access the data from the file please enter "r" to read shoe data from file.
        If you have actioned this already, please select from one of the following:
        va - view all shoes
        as - add shoe
        ss - search shoe
        v - return value held of each shoe
        rs - return shoe with lowest quantity (restock)
        hq - return shoe with highest quantity
        ''')
        if choice == "r":
            read_shoes_data()
        elif choice == "va":
            view_all()
        elif choice == "as":
            capture_shoes()
        elif choice == "ss":
            seach_shoe()
        elif choice == "v":
            value_per_item()
        elif choice == "rs":
            re_stock()
        elif choice == "hq":
            highest_qty()
        else:
            print("Unrecognised input, please try again")
    except:
        print("There has been an error! Did you read the data in before requesting an action? Remember you need to type \"r\" after you run the program to do this.")


