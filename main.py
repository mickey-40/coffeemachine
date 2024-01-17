from data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def cost (order):
  if order == 'espresso':
    cost = MENU['espresso']['cost']
    print(f"The price is {MENU['espresso']['cost']}")
  elif order == 'latte':
    cost = MENU['latte']['cost']
    print(f"The price is {MENU['latte']['cost']}")
  elif order == 'cappuccino':
    cost = MENU['cappuccino']['cost']
    print(f"The price is {MENU['cappuccino']['cost']}")
  else:
    print("It can only be (espresso/latte/cappuccino). Try again.")

order = input("​What would you like? (espresso/latte/cappuccino) : ").lower()

cost(order)

