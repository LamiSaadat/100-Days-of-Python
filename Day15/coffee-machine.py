MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coins = {
  "quarters": 0.25,
  "dimes": 0.10,
  "nickles": 0.05, 
  "pennies": 0.01,
  }



#prompt for order
#take order and match with current resource
  #if any of the items is less than needed for the order
    #print what we don't have enough of
  #else
    #ask for coins
      #calculate the amount
        #if does not match with price
          #print sorry not enough coins. Money refunded
        #else if matches
          #add cost of drink to machine as profit
          #deduct amount used in order from resources
          #print drink
        #else if too much money
          #provide change with drink

#is_resource_sufficient

#process_coins
#is_transaction_successful
#make_coffee

order = input("What would you like? (espresso/latte/cappuccino)\n")

if order in MENU:
  #check for resource sufficiency
	for item in resources:
		if item in MENU[order]["ingredients"] and MENU[order]["ingredients"][item] > resources[item]:
			print(f"Sorry there is not enough {item} for your {order}.")
		else:
			#process the order
			#ask for money
			cost = MENU[order]["cost"]
			print(f"Please insert ${cost}.")
			quarters_inserted = float(input("How many quarters?: "))
			dimes_inserted = float(input("How many dimes?: "))
			nickles_inserted = float(input("How many nickles?: "))
			pennies_inserted = float(input("How many pennies?: "))

	total_money_inserted = round(quarters_inserted * coins["quarters"] + dimes_inserted * coins["dimes"] + nickles_inserted * coins["nickles"] + pennies_inserted * coins["pennies"], 2)

	if total_money_inserted < MENU[order]["cost"]:
		print(f"Not enough money. Amount returned {total_money_inserted}")
	else:
		#make coffee
		#subtract resource amount from resources 
		if item in MENU[order]["ingredients"]:
			resources[item] -= MENU[order]["ingredients"][item]
			resources["money"] += MENU[order]["cost"]
		#provide change
		change = round(float(total_money_inserted) - float(MENU[order]["cost"]), 2)
		if change > 0:
			print(f"Here is your change ${change}. Enjoy your coffee!")

		else:
			print("Enjoy your coffee!")

elif order == "report":
	print(resources)