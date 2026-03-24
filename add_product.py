def add_product(inventory): #This is a funtion to add a new product to the inventory
    print("Please enter your product's data.")
    name = input("\nProduct's name: ")
    while True: #This loop help to manage errors
        try:
            price = float(input("Product's price: "))
            if price < 0:
                print("The price cannot be negative")
            else:
                break
        except ValueError:
            print("Please enter a valid number for price.")

    while True: #This loop help to manage errors
        try:
            quantity = int(input("Quantity: "))
            if quantity < 0:
                print("The quantity cannot be negative")
            else: 
                break                
        except ValueError:
            print("Please enter a valid integer for quantity.")

    product = {
        "product": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    print(inventory)