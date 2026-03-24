def add_product(inventory): #This is a funtion to add a new product to the inventory
    price_continue = True
    quantity_continue = True
    print("Please enter your product's data.")
    name = input("\nProduct's name: ")
    while price_continue: #This loop helps managing errors
        try:
            price = float(input("Product's price: "))
            if price < 0:
                print("The price cannot be negative")
            else:
                price_continue = False 
        except ValueError:
            print("Please enter a valid number for price.")

    while quantity_continue: #This loop help to manage errors
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("The quantity cannot be negative")
            else: 
                quantity_continue = False         
        except ValueError:
            print("Please enter a valid integer for quantity.")

    product = {
        "product": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    print(inventory)