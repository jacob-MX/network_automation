#!/usr/bin/env python

# Utilitiy functions, helpers, etc...
import os
import sys
import json

# Prints a menu with a title and list of options
def print_menu(title, options):
    
    print('\n')
    print(f'{title}\n')
    for idx, option in enumerate(options, start=1):
        print(f'{idx}) {option}')
    print('\n')

# Gets and returns user input
def get_user_input(prompt):
    
    return input(prompt)


 # Clear terminal
def clear_terminal(): 
    
    os.system('clear')       


#Print a separator based on the terminal width.
def print_separator(char='-'):
    
    # Get the terminal size
    terminal_size = os.get_terminal_size()
    
    # Create a separator with the given character and terminal width
    separator = char * terminal_size.columns
    
    # Print the separator
    print(separator)


# Exit the program
def handle_exit(): 
    print("\nThanks for using NETWORK AUTOMATION, bye!")
    sys.exit()   


# One router request info (Paramiko)
def get_router_info():
    router = {
        'hostname': input("Enter the router's hostname or IP address: "),
        'port': input("Enter the port number (default is 22): ") or '22',  # Default to port 22 if no input
        'username': input("Enter the username: "),
        'password': input("Enter the password: ")
    }
    return router


# Two options Menu
def yes_or_no(title):
    # Ask user if they want to add another device
    add_more = input(title).strip().lower()
    if add_more == 'yes' or add_more == 'no' :
        return add_more
    else:
        print('Please select a correct answer: "yes" or "no"')
        return yes_or_no(title)


# Function to store routers in JSON format
def store_routers_in_json(filename="devices.json"):
    routers = []

    while True:
        # Get router info from user
        router = get_router_info()
        routers.append(router)

        # "yes or no" user's choice 
        title = "Do you want to store another device? (yes/no): "
        user_choice = yes_or_no(title)
        if user_choice == 'yes':
            pass
        if user_choice == 'no':
            break
            
    # Save the routers list to a JSON file
    with open(filename, 'w') as file:
        json.dump(routers, file, indent=4)

    print(f"\nAll router information has been saved to {filename}")
