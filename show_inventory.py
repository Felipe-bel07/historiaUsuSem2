def show_inventary(inventory):
    if inventory:
        print("This is you stockt at the moment: ")
        for data in inventory: 
            print(f"\nProduct: {data['product']} | Price: {data['price']} | Quantity: {data['quantity']}")
            
    else: 
        print("\nYour inventory is empty. Please add a product first.")  