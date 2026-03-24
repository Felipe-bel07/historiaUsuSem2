from menu import *
from clear import *
from add_product import *
from show_inventory import *
from calculate_statistics import *

inventory = []
clear()


running = True 

#We created a while loop so that the program wouldn't stop until the user selected the exit option. 
while running: 
    option = menu() #We call the function menu here to get the user's selection. 

    #By using if/elif/else we process the user's election 
    if option == 1: 
        add_product(inventory)
    elif option == 2:
        show_inventary(inventory) #This function shows the inventary 
    elif option == 3: 
        calculate_statistics(inventory) #This funcitons calculates and displays statistics for all products. 
    else:
        running = False #We here get out the program 
    
    
#The objetive of this week was to learn how to use colections, loops and conditionals in python 