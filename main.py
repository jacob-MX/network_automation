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
                                                                          
                                                                          
                                                                          
           
                                                          
                                           -Made by Angel Jacobo Madrigal''')




def third_menu():
    # Define methods
    options = ["Show playbooks", "Add new playbook", "EXIT"]
    # Print second menu
    utils.print_menu("how would u like to proceed?", options)
    # Get user's choice for method
    option = utils.get_user_input('Please select an option: ')

    # Making sure every option is a valid one
    if option == '1' or option == '2':
        return option
    
    elif option == '3':
        # print separator
        utils.print_separator()
        # Handle exit (utils.py)
        utils.handle_exit()
    
    else:        
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        # Recursive function in case of multiple invalid options
        return third_menu()


def independent_playbooks_menu():
    # Third menu to select how to proceed with playbooks
    user_choice = third_menu()

    if user_choice == '1':
        #print separator
        utils.print_separator()
        print('You have selected "Print Playbooks"')

        # Enter a filename and look for it as json file in the current directory
        playbook = utils.find_json_file()

        # Print menu based on the previous given filename and get commands
        commands = utils.async_playbooks_menu(playbook)

        return commands

    elif user_choice == '2':
        #print separator
        utils.print_separator()
        print('You have selected "Add new Playbook"')
        # add a new playbook (default)
        utils.store_async_playbooks("independent_commands.json")

        utils.print_separator()
        # Select a playbook (default)
        commands = utils.async_playbooks_menu("independent_commands.json")

    return commands


def dependent_playbooks_menu():
    # Third menu to select how to proceed with playbooks
    user_choice = third_menu()

    if user_choice == '1':
        #print separator
        utils.print_separator()
        print('You have selected "Print Playbooks"')

        # Enter a filename and look for it as json file in the current directory
        playbook = utils.find_json_file()

        # Print menu based on the previous given filename and get commands
        commands = utils.async_playbooks_menu(playbook)

        return commands

    elif user_choice == '2':
        #print separator
        utils.print_separator()
        print('You have selected "Add new Playbook"')
        # add a new playbook (default)
        utils.store_async_playbooks("dependent_commands.json")

        utils.print_separator()
        # Select a playbook (default)
        commands = utils.async_playbooks_menu("dependent_commands.json")

    return commands

def second_menu():
    # Define methods
    options = ["JSON file", "Manual insertion", "EXIT"]
    # Print second menu
    utils.print_menu("how would u like to enter your devices?", options)
    # Get user's choice for method
    option = utils.get_user_input('Please select an option: ')

    # Making sure every option is a valid one
    if option == '1' or option == '2': 
        return option

    elif option == '3':
        # print separator
        utils.print_separator()
        # Handle exit (utils.py)
        utils.handle_exit()

    else:        
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        # Recursive function in case of multiple invalid options
        return second_menu()

    
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
            # save filename given by the user and checks for its existence in the current directory
            filename = utils.find_json_file()
            # Store JSON file as Python objects
            devices = utils.read_json_file(filename)

            # Get commands from a Playbook
            commands = independent_playbooks_menu()

            # print separator
            utils.print_separator()
            
            # run multiple ssh clients and execute playbook as an asynchronous function 
            ssh_objects = asyncio.run(ssh_manager.run_multiple_clients(devices, commands))
            # print output per device
            utils.print_objects(ssh_objects, devices)
            # Handle exit (utils.py)
            utils.handle_exit()
                      
        if user_choice == '2':
            #print separator
            utils.print_separator()
            print('You have selected "Manual Insertion"')

            # Function to enter device from terminal one by one (Manually)
            utils.store_routers_in_json("devices.json")
            
            # Store JSON file as Python objects
            devices = utils.read_json_file("devices.json")
            
            #print separator
            utils.print_separator()

            # Get commands from a Playbook
            commands = independent_playbooks_menu()

            # print separator
            utils.print_separator()
            
            # run multiple ssh clients and execute playbook as an asynchronous function 
            ssh_objects = asyncio.run(ssh_manager.run_multiple_clients(devices, commands))
            
            # print output per device
            utils.print_objects(ssh_objects, devices)
            
            # Handle exit (utils.py)
            utils.handle_exit()
                
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

            # Look for a json file in the current directory
            filename = utils.find_json_file()
            
            # Store JSON file as Python objects
            devices = utils.read_json_file(filename)

            # Get commands from a Playbook
            commands = dependent_playbooks_menu()

            # print separator
            utils.print_separator()

            # Execute commands using multithreading (ssh_manager)
            outputs = ssh_manager.multithreading_execution(devices, commands)
            # Print outputs
            for output in outputs:
                print(output)

            # Handle exit (utils.py)
            utils.handle_exit()

        if user_choice == '2':
            #print separator
            utils.print_separator()
            print('You have selected "Manual Insertion"')
            
            # Function to enter device from terminal one by one (Manually)
            utils.store_routers_in_json("devices.json")
            
            # Store JSON file as Python objects
            devices = utils.read_json_file("devices.json")
            
            #print separator
            utils.print_separator()

            # Get commands from a Playbook
            commands = dependent_playbooks_menu()

            # print separator
            utils.print_separator()

            # Execute commands using multithreading (ssh_manager)
            outputs = ssh_manager.multithreading_execution(devices, commands)
            # Print outputs
            for output in outputs:
                print(output)
                
            # Handle exit (utils.py)
            utils.handle_exit()
            

    if option == '3':
        # print separator
        utils.print_separator()
        # Handle exit (utils.py)
        utils.handle_exit()
        
    # Main menu invalid option
    else:
        # print separator
        utils.print_separator()
        print("\nInvalid option. Please select either 1, 2, or 3.")
        # Recursive function in case of multiple invalid options
        main_menu()


if __name__ == '__main__':
    main_menu()