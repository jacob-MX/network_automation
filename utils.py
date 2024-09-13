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


# Exit the program
def handle_exit(): 
    print("\nThanks for using NETWORK AUTOMATION, bye!")
    sys.exit()         


#Print a separator based on the terminal width.
def print_separator(char='-'):
    
    # Get the terminal size
    terminal_size = os.get_terminal_size()
    
    # Create a separator with the given character and terminal width
    separator = char * terminal_size.columns
    
    # Print the separator
    print(separator)

