drink_menu = {
    "Tea" : 1.00,
    "Americano" : 1.70,
    "Latte" : 1.90,
    "Cappuccino" : 1.90,
    "Mocha":2.00,
}
drink_order = []
total_cost = 0

print(drink_menu)
drink_item = input("Drink choice: ")
if drink_item in drink_menu:
    quantity = int(input("How many do you want?"))
    drink_order.append((drink_item, quantity))
    drink_value = drink_menu.get(drink_item)
    cost = drink_value * quantity
    total_cost += cost
    print(f"You have ordered {drink_item} x {quantity}. The total cost is £{total_cost}")