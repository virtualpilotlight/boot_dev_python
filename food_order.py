italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
def find_meal(name, menu):
  if name in menu:
    return name
  else:
    return None

def select_meal(name):
  return find_meal(name, italian_food)

def display_available_meals():
  print("Available Italian meals:")
  for food in italian_food:
    print(food)

def create_summary(name, amount):
  order = select_meal(name)
  if order == None:
    return "Meal not found"
  else:
    return f"food: {order} quantity: {amount}"

print("Welcome to the Food Order System!")

display_available_meals()

name_input = input("choose meal: ")
amount_input = input("choose amount: ")

result = create_summary(name_input, amount_input)

print(result)


