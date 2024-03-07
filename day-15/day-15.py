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
money = 0
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25
cost_espresso = 1.5
cost_latte = 2.5
cost_cappuccino = 3.0


def report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${money}")

def is_resources(order):
        is_enough = True
        for item in order:
            if order[item] >= resources[item]:
                print(f"i'm sorry there no enough {item}.")
            is_enough = False        
        return True

loop = True
while loop == True:
    all_coins2 = 0
    # TODO - Ask the user about what he want
    ask = input("What Would you like: (espresso, latte, cappuccino) ")
    if ask == "report":
        report()
    
    # TODO - See if there is enough quantity for the order
    if ask == "latte":
        if resources["water"] - MENU["latte"]["ingredients"]["water"] < 0:
            print("we don't have water.")
            exit()
        elif resources["milk"] - MENU["latte"]["ingredients"]["milk"] < 0:
            print("we don't have milk.")
            exit()
        elif resources["coffee"] - MENU["latte"]["ingredients"]["coffee"] < 0:
            print("we don't have coffee.")
            exit()
    if ask == "espresso":
        if resources["water"] - MENU["espresso"]["ingredients"]["water"] < 0:
            print("we don't have water.")
            exit()
        elif resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"] < 0:
            print("we don't have coffee.")
            exit()
    if ask == "cappuccino":
        if resources["water"] - MENU["cappuccino"]["ingredients"]["water"] < 0:
            print("we don't have water.")
            exit()
        elif resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"] < 0:
            print("we don't have milk.")
            exit()
        elif resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"] < 0 :
            print("we don't have coffee.")
            exit()
    
    if ask == "cappuccino" or ask == "latte" or ask == "cappuccino":
        # TODO - Taking money from the user
        print("Please insert coins.")
        if resources["water"] > 0 and resources["coffee"] > 0 and resources["milk"] > 0:
            in_quarter = int(input("How many quarter "))
            c = quarter * in_quarter
            in_dime = int(input("How many dime "))
            o = dime * in_dime
            in_nickel = int(input("How many nickel "))
            i = nickel * in_nickel
            in_penny = int(input("How many penny "))
            n = penny * in_penny
            all_coins = c + o + i + n

        # TODO - Discount on available quantity after ordering
        if ask == "latte":
            if all_coins >= cost_espresso:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        if ask == "espresso":
            if all_coins >= cost_latte:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        if ask == "cappuccino":
            if all_coins >= cost_cappuccino:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]

        # TODO - Give the user the change
        if ask == "espresso":
            all_coins -= cost_espresso
            if all_coins > 0:
                money += cost_espresso
                print(f"Here is your change {all_coins:.2f}")
            else:
                print("sorry that's not enough money.")
                loop = False

        if ask == "latte":
            all_coins -= cost_latte
            if all_coins > 0:
                money += cost_latte
                print(f"Here is your change {all_coins:.2f}")
            else:
                print("sorry that's not enough money.")
                loop = False

        if ask == "cappuccino":
            all_coins -= cost_cappuccino
            if all_coins > 0:
                money += cost_cappuccino
                print(f"Here is your change {all_coins:.2f}")
            else:
                print("sorry that's not enough money.")
                loop = False

    if ask == "off":
        loop = False
