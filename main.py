#!/usr/bin/env python

# Testing backbone application

# import utility functions
import utils

utils.clear_terminal()

print('''
▗▖  ▗▗▄▄▄▗▄▄▄▗▖ ▗▖▗▄▗▄▄▄▗▖ ▗▖     ▗▄▖▗▖ ▗▗▄▄▄▗▄▖▗▖  ▗▖▗▄▗▄▄▄▗▄▄▄▖▗▄▖▗▖  ▗▖
▐▛▚▖▐▐▌    █ ▐▌ ▐▐▌ ▐▌█ ▐▌▗▞▘    ▐▌ ▐▐▌ ▐▌ █▐▌ ▐▐▛▚▞▜▐▌ ▐▌█   █ ▐▌ ▐▐▛▚▖▐▌
▐▌ ▝▜▐▛▀▀▘ █ ▐▌ ▐▐▌ ▐▌█ ▐▛▚▖     ▐▛▀▜▐▌ ▐▌ █▐▌ ▐▐▌  ▐▐▛▀▜▌█   █ ▐▌ ▐▐▌ ▝▜▌
▐▌  ▐▐▙▄▄▖ █ ▐▙█▟▝▚▄▞▘█ ▐▌ ▐▌    ▐▌ ▐▝▚▄▞▘ █▝▚▄▞▐▌  ▐▐▌ ▐▌█ ▗▄█▄▝▚▄▞▐▌  ▐▌
                                                                          
                                                                          
                                                                          
           
                                                          
                                                        -Made by Angel Jacobo Madrigal''')


# Proceed based on the user's input
# Proceed if 'Asynchronous' or 'Multithreading'
def automate_devices(method):
    #print separator
    utils.print_separator()
    # Shows selected options
    print(f'\nYou selected "{method}" method.')
    
    # Define options for device automation
    options = ["One device", "Multiple devices", "EXIT"]

    # Print the device automation menu
    utils.print_menu("How many devices would you like to automate?", options)

    # Get user's choice for device automation
    option = utils.get_user_input('Please select an option: ')



    if option == '1':
        #print separator
        utils.print_separator()
        print("\nYou selected to automate one device.")
        
        if method == 'Asynchronous':
            print(f'Executing {method} process for one device...')
            # Add logic for automating asynchronously one device here
        
        elif method == 'Multithreading':
            print(f'Executing {method} process for one device...')
            # Add logic for automating one device using Multithreading here
        


    
    elif option == '2':
        #print separator
        utils.print_separator()
        print("\nYou selected to automate multiple devices.")
        
        if method == 'Asynchronous':
            print(f'Executing {method} process for mutiple devices...')
        
        elif method == 'Multithreading':
            print(f'Executing {method} process for mutiple devices...')


    elif option == '3':
        utils.handle_exit()

    else:
        print("\nInvalid option. Please select either 1, 2, or 3.")
        automate_devices(method)


# Main menu to select between methods
def main_menu():
    
    #print separator
    utils.print_separator()
    # Define methods
    options = ["Asynchronous", "Multithreading", "EXIT"]
    # Print main menu
    utils.print_menu("Select the method you want to use:", options)
    # Get user's choice for method
    option = utils.get_user_input('Please select an option: ')

    
    if option == '1':

        automate_devices("Asynchronous")
        
    elif option == '2':

        automate_devices("Multithreading")
        
    elif option == '3':
        utils.handle_exit()
        
    else:
        print("\nInvalid option. Please select either 1, 2, or 3.")
        main_menu()


if __name__ == '__main__':
    main_menu()