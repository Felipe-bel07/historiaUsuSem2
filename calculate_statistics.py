def calculate_statistics(inventory):
    total_bill = 0 
    total_products = len(inventory)
    print(f"The total amounht of products in your invetory is {total_products}")
    for data in inventory:
        sub_total = data['price'] * data['quantity']
        total_bill += sub_total
    print(f"Your total bill is ${total_bill}")