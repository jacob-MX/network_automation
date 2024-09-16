#!/usr/bin/env python

# Utilitiy functions, helpers, etc...
import os
import sys

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
