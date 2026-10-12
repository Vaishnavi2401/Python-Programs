#Calculate the cost of item in shopping cart

cart = [{"item":"Apple", "Cost": 10, "Quantity": 10},
        {"item":"Banana", "Cost": 15, "Quantity": 5},
        {"item":"Pineapple", "Cost": 40, "Quantity": 1},
        {"item":"Guvava", "Cost": 20, "Quantity": 5}]

def cart_total_cost(cart_items):
    Total_cost = 0
    for items in cart_items:
        Total_cost += items["Cost"] * items["Quantity"]
    print("Total cost of cart items are", Total_cost)

cart_total_cost(cart)