import menu

# TODO 0: import menu and resource
espresso = menu.MENU['espresso']
latte = menu.MENU['latte']
cappuccino = menu.MENU['cappuccino']
resources = menu.resources
income = 0
order = ""
enough = True

def get_money():
    print('Please insert your coins:')
    quarters = int(input('How many quarters? '))
    half = int(input("How many half dollar? "))
    one = int(input("How many loonies? "))
    payment = (0.25 * quarters) + (0.5 * half) + one
    return payment

def increase_income(cost):
    global income
    income += cost
    print(f"The total cash is ${income} 🤑🤑🤑.")

def check_resouces(coffee_ingredient):
    global resources
    global enough
    enough = True
    coffee_ingredients_list = list(coffee_ingredient.keys())
    for key, value in resources.items():
        if not key in coffee_ingredients_list:
            coffee_ingredient[key] = 0
        if resources[key] < coffee_ingredient[key]:
            enough = False
            print(f"Sorry 😔😔😔, we are missing {-resources[key] + coffee_ingredient[key]} {key}, please try another drink")
            return enough
        return enough

def align_ingredients(coffee_ingredient):
    global resources
    coffee_ingrediets_list = list(coffee_ingredient.keys())
    for key, value in resources.items():
        if not key in coffee_ingrediets_list:
            coffee_ingredient[key] = 0

def change_resources(coffee_ingredient):
    global resources
    coffee_ingrediets_list = list(coffee_ingredient.keys())
    for key, value in resources.items():
        if not key in coffee_ingrediets_list:
            coffee_ingredient[key] = 0
        resources[key] -= coffee_ingredient[key]
    print("Updated resources: ", resources)

def understand_order(order):
    if order == "latte":
        order = latte
    elif order == "cappuccino":
        order = cappuccino
    elif order == "espresso":
        order = espresso
    return order

def read_ingredients(ingredients):
    align_ingredients(ingredients)
    print(f"The ingredients are {ingredients['water']}ml Water 💧, {ingredients['milk']}ml Milk 🥛 and {ingredients['coffee']}mg Coffee 🧆 ")

# TODO 0.1: function of giving the ingredients
def coffee_ingredients(coffee):
    ingredients = coffee['ingredients']
    return ingredients

# TODO 0.2: function of giving the cost
def coffee_cost(coffee):
    cost = coffee['cost']
    return cost
# TODO 1: Take the order as an input

print(menu.logo)

while order != 'exit':
    order = input("What would you like to have? ☕☕☕(espresso/latte/cappuccino/exit)☕☕☕: ")
    if order != 'exit':
        order = understand_order(order)

        ingredients = coffee_ingredients(order)
        cost = coffee_cost(order)
        read_ingredients(ingredients)
        print(f"The cost will be ${cost}")

        if check_resouces(ingredients):
            payment = get_money()
            print(f"You have paid: ${payment}")
            change = payment - cost
            if change >= 0:
                print(f"Your change is ${change} 😊😊😊")
                change_resources(coffee_ingredients(order))
                increase_income(coffee_cost(order))
            else:
                print(f"You are missing ${change} 😥😥😥")

    else:
        print('Thank you, have and good day! 🌞🌞🌞')
