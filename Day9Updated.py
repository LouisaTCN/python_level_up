# order_counter = 0
# def create_order():
#     global order_counter():
#     order_counter +=1
#     return f"Order #order"

order_number = 0
order_number +=1

drink_menu = {
    "Tea" : 1.00,
    "Americano" : 1.70,
    "Latte" : 1.90,
    "Cappuccino" : 1.90,
    "Mocha":2.00,
}

food_menu = {
  "Croissant": 1.50,
  "Muffin": 2.10, 
  "Toast": 1.00,
  "Panini": 2.90,
  "Buttered Roll": .70,
  "Stroopwafel": .50
}

drink_order = []
food_order = []

total_cost = 0

drink_answer = input("Would you like to order a drink?  ").capitalize()
 
while drink_answer == "Yes":
    print(drink_menu)
    drink_item = input("Drink choice: ")
    if drink_item in drink_menu:
       drink_quantity = int(input("How many do you want? "))
       drink_order.append((drink_item, drink_quantity))
       drink_value = drink_menu.get(drink_item)
       cost = drink_value * drink_quantity
       total_cost += cost
       print(f"You have ordered {drink_quantity} x {drink_item}. The total cost is £{total_cost}")
       drink_answer = input("Would you like to order another drink? ").capitalize()
    else:
        print("Sorry we don't have that item. Try again")

food_answer = input("Would you like to order food? ").capitalize()
 
while food_answer == "Yes":
    print(food_menu)
    food_item = input("Food choice: ")
    if food_item in food_menu:
       food_quantity = int(input("How many do you want? "))
       food_order.append((food_item, food_quantity))
       food_value = food_menu.get(food_item)
       cost = food_value * food_quantity
       total_cost += cost
       print(f"You have ordered {food_quantity} x {food_item}. The total cost so far is £{total_cost}")
       food_answer = input("Would you like to order some more food? ").capitalize()
    else:
        print("Sorry we don't have that item. Try again")

print("Checkout")


