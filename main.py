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


    if option == '1':
                
                #print separator
                utils.print_separator()
                print('You have selected "JSON" method')

    elif option == '2':
                
                #print separator
                utils.print_separator()
                print('You have selected "Manual insertion" method')
        

    elif option == '3':
                
                # print separator
                utils.print_separator()
                # Handle exit (utils.py)
                utils.handle_exit()
                # print separator
                utils.print_separator()

    else:
        
                # print separator
                utils.print_separator()
                print("\nInvalid option. Please select either 1, 2, or 3.")
                second_menu()

    

        



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
    
    if option == '1':

        #print separator
        utils.print_separator()
        print('You have selected "Asynchronous" method')
        # Invoke second menu and store the user's choice
        second_menu()

        
        
    elif option == '2':

        # print separator
        utils.print_separator()
        print('You have selected "Multithreading" method')
        # Invoke second menu and store the user's choice
        second_menu()
        
        
        
    elif option == '3':
        
        # print separator
        utils.print_separator()
        # Handle exit (utils.py)
        utils.handle_exit()
        # print separator
        utils.print_separator()

    
    else:
        
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        main_menu()


if __name__ == '__main__':
    main_menu()