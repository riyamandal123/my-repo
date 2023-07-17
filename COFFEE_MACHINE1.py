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
}

total_water=resources["water"]#initial value for total_water
total_milk=resources["milk"]#initial value for total_milk
total_coffee=resources["coffee"]#initial value for total_coffee

# Function to get the total amount of coins inserted by the user.
def insert_coins():
    total_amount = 0
    print("Please insert coins.")
    quaters=int(input("how many quaters? : "))
    dimes=int(input("how many dimes? : "))
    nickels=int(input("how many nickels? : "))
    pennies=int(input("how many pennies? : "))
    total_amount += 0.25*quaters + 0.10*dimes + 0.05*nickels + 0.01*pennies

    return total_amount

profit = 0
def espresso():
    total_amount = insert_coins()
    # Amount of water required for an espresso.
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    # Amount of coffee required for an espresso.
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    #cost of the espresso.
    cost_of_espresso = MENU["espresso"]["cost"]
    
    #Declare the global variables that need to be modified.
    global total_water,total_coffee
    
    # Check if there is enough water and coffee to make an espresso.
    if total_water >= 50 and total_coffee >= 18:
        # Deduct the used amount of water.
        total_water = total_water - espresso_water
        # Deduct the used amount of coffee.
        total_coffee = total_coffee - espresso_coffee

        if total_amount ==  cost_of_espresso:
            print("Here is your espresso ☕.Enjoy!")
        elif total_amount > cost_of_espresso:
            # Calculate the change to be given.
            change = round(total_amount - cost_of_espresso,2)
            # Add the cost of the espresso to the profit.
            global profit
            profit += cost_of_espresso
            print(f"Here is ${change} change.")
            print("Here is your espresso ☕.Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
            
    elif total_water < 50:
        print("Sorry there is not enough water.")
        
    elif  total_coffee < 18:
         print("Sorry there is not enough coffee.")
    

def latte():
    total_amount = insert_coins()
    # Amount of water required for an latte.
    latte_water = MENU["latte"]["ingredients"]["water"]
    # Amount of coffee required for an latte.
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    # Amount of milk required for an latte.
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    #ost of the latte.
    cost_of_latte = MENU["latte"]["cost"]
    #Declare the global variables that need to be modified.
    global total_water,total_coffee,total_milk

    # Check if there is enough water,milk and coffee to make an latte.
    if total_water >= 200 and total_coffee >= 24 and total_milk >= 150:
        # Deduct the used amount of water.
        total_water = total_water - latte_water
        # Deduct the used amount of coffee.
        total_coffee = total_coffee - latte_coffee
        # Deduct the used amount of milk.
        total_milk = total_milk - latte_milk
        
        if total_amount ==  cost_of_latte:
            print("Here is your latte ☕.Enjoy!")
        elif total_amount > cost_of_latte:
            # Calculate the change to be given.
            change = round(total_amount - cost_of_latte,2)
            # Add the cost of the espresso to the profit.
            global profit
            profit += cost_of_latte
            print(f"Here is ${change} change.")
            print("Here is your latte ☕.Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
            
    elif total_water < 200:
         print("Sorry there is not enough water.")
         
    elif  total_coffee < 24:
         print("Sorry there is not enough coffee.")
         
    elif  total_milk < 150:
         print("Sorry there is not enough milk.")
         

def cappuccino():
    total_amount = insert_coins()
    # Amount of water required for an cappuccino.
    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    # Amount of coffee required for an cappuccino.
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    # Amount of milk required for an cappuccino.
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    #cost of cappuccino.
    cost_of_cappuccino = MENU["cappuccino"]["cost"]
    #Declare the global variables that need to be modified.
    global total_water,total_coffee,total_milk

    # Check if there is enough water,milk and coffee to make an latte.
    if total_water >= 300 and total_coffee >= 100 and total_milk >= 200:
        # Deduct the used amount of water.
        total_water = total_water - cappuccino_water
        # Deduct the used amount of coffee.
        total_coffee = total_coffee - cappuccino_coffee
        # Deduct the used amount of milk.
        total_milk = total_milk - cappuccino_milk

        if total_amount ==  cost_of_cappuccino:
            print("Here is your cappuccino ☕.Enjoy!")
        elif total_amount > cost_of_cappuccino:
            # Calculate the change to be given.
            change = round(total_amount - cost_of_cappuccino,2)
            # Add the cost of the espresso to the profit.
            global profit
            profit += cost_of_cappuccino
            print(f"Here is ${change} change.")
            print("Here is your cappuccino ☕.Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
            
    elif total_water < 300:
         print("Sorry there is not enough water.")
         
    elif  total_coffee < 100:
         print("Sorry there is not enough coffee.")
         
    elif  total_milk < 200:
         print("Sorry there is not enough milk.")
         

coffee_machine_on = True
while coffee_machine_on:
    user_choice=input("What would you like? (espresso/latte/cappuccino): ")
    
    if user_choice == "espresso":
        espresso()
        
    elif user_choice == "latte":
        latte()
        
    elif user_choice == "cappuccino":
        cappuccino()
        
    elif user_choice == "report":
        print(f"Water: {total_water}ml")
        print(f"Milk: {total_milk}ml")
        print(f"coffee: {total_coffee}g")
        print(f"Money: ${profit}")
        
    elif user_choice == "off":
        coffee_machine_on = False
        
    else:
        print("Invalid input!")

    


    
