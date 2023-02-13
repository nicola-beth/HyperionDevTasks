#programe to look for menu keys in dictionaries and calculate total value of all stock via 'menu' key
menu = ["tuna sandwich", "pain au chocolat", "cheese toastie", "snack bar"]
stock = {"tuna sandwich": 5, "pain au chocolat": 4, "cheese toastie": 7, "snack bar": 13}
price = {"tuna sandwich": 4.99, "pain au chocolat": 2.50, "cheese toastie": 3.99, "snack bar": 1.99}

total_price = 0     #define total variable to add to

#for menu list items, look for key in stock & price dictionary
for food in menu:
    total_price += stock[food] * price[food]        #total is sum of all qualtity multiplied by price for all items

print(f"Total value of stock in cafe is £{total_price}.")