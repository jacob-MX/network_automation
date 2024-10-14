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

    if option == '1':
        command_type = 'dependent'

    elif option == '2':
        command_type = 'independent'

    elif option =='3':
        main_menu()

    else:
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        # Recursive function in case of multiple invalid options
        return dependent_or_independent()
        
    return option, command_type


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
        user_choice, command_type = dependent_or_independent()
 
        #print separator
        utils.print_separator()
        
        print(f'You have selected "{command_type}" commands execution.')
        
        # Select devices
        devices, file = utils.get_json_devices_by_os()

        #print separator
        utils.print_separator()
        
        # print playbooks menu
        playbook = utils.playbooks_menu(command_type, file)
        
        # Select playbook
        commands = utils.get_playbook_by_name(playbook)
            
        # print commands
        print(commands)
        # Handle exit
        utils.handle_exit()
        
            
    # Option 2 (Add a playbook)   
    elif user_choice == '2':
        
        # print separator
        utils.print_separator()
        
        print('You have selected "Add a playbook" method')
        
        # Invoke dependent or independent menu and store the user's choice
        user_choice, command_type = dependent_or_independent()

        #print separator
        utils.print_separator()
        
        print(f'You have selected "{command_type}" method')
        
        # Invoke add new playbook 
        utils.add_new_playbook(command_type)
        
        # print separator
        utils.print_separator()
        main_menu

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