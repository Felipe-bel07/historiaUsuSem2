import os

def  clear():
    name = os.name 
    if name != "nt":
        os.system("clear")
    else:
        os.system("cls")
    
