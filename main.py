#!/usr/bin/env python

# Testing backbone application

# import utility functions
import ssh_manager
import utils
import asyncio


utils.clear_terminal()

print('''
▗▖  ▗▗▄▄▄▗▄▄▄▗▖ ▗▖▗▄▗▄▄▄▗▖ ▗▖     ▗▄▖▗▖ ▗▗▄▄▄▗▄▖▗▖  ▗▖▗▄▗▄▄▄▗▄▄▄▖▗▄▖▗▖  ▗▖
▐▛▚▖▐▐▌    █ ▐▌ ▐▐▌ ▐▌█ ▐▌▗▞▘    ▐▌ ▐▐▌ ▐▌ █▐▌ ▐▐▛▚▞▜▐▌ ▐▌█   █ ▐▌ ▐▐▛▚▖▐▌
▐▌ ▝▜▐▛▀▀▘ █ ▐▌ ▐▐▌ ▐▌█ ▐▛▚▖     ▐▛▀▜▐▌ ▐▌ █▐▌ ▐▐▌  ▐▐▛▀▜▌█   █ ▐▌ ▐▐▌ ▝▜▌
▐▌  ▐▐▙▄▄▖ █ ▐▙█▟▝▚▄▞▘█ ▐▌ ▐▌    ▐▌ ▐▝▚▄▞▘ █▝▚▄▞▐▌  ▐▐▌ ▐▌█ ▗▄█▄▝▚▄▞▐▌  ▐▌

                                           - Made by Angel Jacobo Madrigal''')

def first_menu():
    # Define options
    options = ["Execute Commands", "Add a playbook", "Add a device", "Exit"]
    # Print main menu
    utils.print_menu("How would u like to proceed?", options)
    # Get user's choice for method
    option = utils.get_user_input('Please select an option: ')

    if option == '4':
        # print separator
        utils.print_separator()
        # Handle exit (utils.py)
        utils.handle_exit()

    elif option not in ['1', '2', '3']:
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        # Recursive function in case of multiple invalid options
        return first_menu()

    return option


def dependent_or_independent():
    # Define options
    options = ["Dependent commands", "Independent commands", "Back"]
    # Print main menu
    utils.print_menu("How would u like to proceed?", options)
    # Get user's choice for method
    option = utils.get_user_input('Please select an option: ')

    if option not in ['1', '2', '3']:
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        # Recursive function in case of multiple invalid options
        return dependent_or_independent()
        
    return option


# Main menu to select between methods
def main_menu():
    #print separator
    utils.print_separator()
    # Invoke first menu ('Execute, add a playbook, or add a device')
    user_choice = first_menu()
    
    # Option 1 (Execute commands)
    if user_choice == '1':
        #print separator
        utils.print_separator()
        print('You have selected "Execute commands" method')
        # Invoke dependent or independent menu and store the user's choice
        user_choice = dependent_or_independent()

        # Option 1 (Dependent)
        if user_choice == '1':
            #print separator
            utils.print_separator()
            print('You have selected "Dependent Commands" method')
            # Handle exit
            utils.handle_exit()
        
        # Option 2 (Independent)       
        elif user_choice == '2':
            #print separator
            utils.print_separator()
            print('You have selected "Independent Commands" method')
            # Invoke second menu and store the user's choice
            # Handle exit
            utils.handle_exit()

        elif user_choice == '3':
            #print separator
            utils.print_separator()
            print('You have selected "Back" method')
            # Invoke second menu and store the user's choice
            main_menu()
            
    # Option 2 (Add a playbook)   
    elif user_choice == '2':
        # print separator
        utils.print_separator()
        print('You have selected "Add a playbook" method')
        # Invoke dependent or independent menu and store the user's choice
        user_choice = dependent_or_independent()

        # Option 1 (Dependent)
        if user_choice == '1':
            #print separator
            utils.print_separator()
            print('You have selected "Dependent Commands" method')
            # Invoke add new playbook 
            utils.add_new_playbook('dependent')
            # print separator
            utils.print_separator()
            main_menu
        
        # Option 2 (Independent)       
        elif user_choice == '2':
            #print separator
            utils.print_separator()
            print('You have selected "Independent Commands" method')
            # Invoke add new playbook menu 
            utils.add_new_playbook('independent')
            # print separator
            utils.print_separator()
            main_menu

        elif user_choice == '3':
            #print separator
            utils.print_separator()
            print('You have selected "Back" method')
            # back to main
            main_menu()

    # Option 3 (Add a device)
    if user_choice == '3':
        # print separator
        utils.print_separator()
        print('You have selected "Add a device" method')
        # Invoke add a new device menu 
        utils.add_new_device()
        # print separator
        utils.print_separator()
        main_menu

if __name__ == '__main__':
    main_menu()