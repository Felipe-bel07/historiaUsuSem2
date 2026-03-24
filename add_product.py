def add_product(inventory): #This function add a new product to the invenytary 
            print("Please enter the your product's data.")
            name  = input("\nProduct's name: ")
            price = float(input("Product's price: "))
            quantity = int(input("Quantity: "))
            product = {
                "product": name,
                "price": price,
                "quantity": quantity
            }  
            inventory.append(product)
            print(inventory)