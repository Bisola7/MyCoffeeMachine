from coffee_data import MENU, resources
# TODO: prepare coffee type of user
def make_coffee():
    print("Please insert coins")
    quater = int(input("How many quaters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total = (0.25 * quater) + (0.1 * dime) + (0.05 * nickle) + (0.01 * penny)
    a = MENU[user_input]
    user_input_cost = a["cost"]
    # TODO: user change
    if total > user_input_cost:
        change = round(total - user_input_cost, 2)
        print(f"Here is {change} in change")
        if total >= total > user_input_cost:
            print(f"Here's your {user_input}☕")
            return True
    elif total < user_input_cost:
        print("Sorry, that's not enough money, money refunded")
money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
off = False
while off == False:
    # TODO: ask the user what they want to buy
    user_input = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if user_input == "report":
        # TODO: report
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    if user_input == "espresso":
        mui = MENU[user_input]
        uii = mui["ingredients"]
        uiw = uii["water"]
        uic = uii["coffee"]
        if water > uiw:
            if coffee > uic:
                if make_coffee() == True:
                    water -= uiw
                    coffee -= uic
                    print(water)
                    print(coffee)
                    money += mui["cost"]
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    elif user_input == "latte" or user_input == "cappuccino":
        mui = MENU[user_input]
        uii = mui["ingredients"]
        uiw = uii["water"]
        uim = uii["milk"]
        uic = uii["coffee"]
        if water > uiw:
            if coffee > uic:
                if milk > uim:
                    if make_coffee() == True:
                        water -= uiw
                        coffee -= uic
                        milk -= uim
                        print(water)
                        print(coffee)
                        print(milk)
                        money += mui["cost"]
                else:
                    print("sorry there is not enough milk")
            else:
                print("Sorry there is not enough coffee")
        else:
            print("Sorry there is not enough water")
    elif user_input == "off":
        off = True