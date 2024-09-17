#!/usr/bin/env python

# Testing backbone application

# import utility functions
import utils
import ssh_manager

utils.clear_terminal()

print('''
▗▖  ▗▗▄▄▄▗▄▄▄▗▖ ▗▖▗▄▗▄▄▄▗▖ ▗▖     ▗▄▖▗▖ ▗▗▄▄▄▗▄▖▗▖  ▗▖▗▄▗▄▄▄▗▄▄▄▖▗▄▖▗▖  ▗▖
▐▛▚▖▐▐▌    █ ▐▌ ▐▐▌ ▐▌█ ▐▌▗▞▘    ▐▌ ▐▐▌ ▐▌ █▐▌ ▐▐▛▚▞▜▐▌ ▐▌█   █ ▐▌ ▐▐▛▚▖▐▌
▐▌ ▝▜▐▛▀▀▘ █ ▐▌ ▐▐▌ ▐▌█ ▐▛▚▖     ▐▛▀▜▐▌ ▐▌ █▐▌ ▐▐▌  ▐▐▛▀▜▌█   █ ▐▌ ▐▐▌ ▝▜▌
▐▌  ▐▐▙▄▄▖ █ ▐▙█▟▝▚▄▞▘█ ▐▌ ▐▌    ▐▌ ▐▝▚▄▞▘ █▝▚▄▞▐▌  ▐▐▌ ▐▌█ ▗▄█▄▝▚▄▞▐▌  ▐▌
                                                                          
                                                                          
                                                                          
           
                                                          
                                                        -Made by Angel Jacobo Madrigal''')
def second_menu():
    # Define methods
    options = ["JSON file", "Manual insertion", "EXIT"]
    # Print second menu
    utils.print_menu("how would u like to enter your devices?", options)
    # Get user's choice for method
    option = utils.get_user_input('Please select an option: ')

    if option == '1' or option == '2' or option == '3': 
        pass

    else:        
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        return second_menu()
        
    return option
    

        



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
    print()


    # Main menu "ASYNCHRONOUS" 
    if option == '1':

        #print separator
        utils.print_separator()
        print('You have selected "Asynchronous" method')
        # Invoke second menu and store the user's choice
        user_choice = second_menu()
        
        if user_choice == '1':
            #print separator
            utils.print_separator()
            print('You have selected "JSON" format')
            input('Please enter file name: ')

        if user_choice == '2':
            #print separator
            utils.print_separator()
            print('You have selected "Manual Insertion"')
            utils.store_routers_in_json()
        

        
    # Main menu "Multithreading"    
    elif option == '2':

        # print separator
        utils.print_separator()
        print('You have selected "Multithreading" method')
        # Invoke second menu and store the user's choice
        user_choice = second_menu()
        
        if user_choice == '1':
            #print separator
            utils.print_separator()
            print('You have selected "JSON" format')
            input('Please enter file name: ')

        if user_choice == '2':
            #print separator
            utils.print_separator()
            print('You have selected "Manual Insertion"')
            utils.store_routers_in_json()

    
    # Main menu "EXIT"
    elif option == '3':
        
        # print separator
        utils.print_separator()
        # Handle exit (utils.py)
        utils.handle_exit()
        # print separator
        utils.print_separator()


    # Main menu invalid option
    else:
        
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        main_menu()


if __name__ == '__main__':
    main_menu()