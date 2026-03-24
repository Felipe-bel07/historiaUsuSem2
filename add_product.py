def add_product(inventary): #This function add a new product to the invenytary 
            print("Please enter the your product's data.")
            name  = input("\nProduct's name: ")
            price = float(input("Product's price: "))
            quantity = int(input("Quantity: "))
            product = {
                "name": name,
                "price": price,
                "quantity": quantity
            }  
            inventary.append(product)
            print(inventary)