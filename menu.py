from clear import *

#This is our menu function, which displays the main menu to the user. 
def menu():
    print("*" * 43)
    print("|", "Welcome to your Riwi inventory manager!", "|")
    print("*" * 43)
    print("""
    Menu: 
    1. Add a product
    2. Show invetory 
    3. Calculate stadistics 
    4. Exit   
    """
    )
    to_continue = True 
    
    #This loop help us validating that the option is entered as is expected by the program
    while to_continue:
        try: #Managing errors, so if a invalid value is entered the program won't crash 
            #Telling the user to enter an option
            option_selected = int(input("\nPlease select the action you want to do: "))
            if option_selected > 4 or option_selected < 1: #Validating that the option selected is within the range expected 
                print("The value entered must be within 1 to 4")
            else:
                to_continue = False
            
        except ValueError: 
            print("Please enter a valid option.")
    return option_selected


