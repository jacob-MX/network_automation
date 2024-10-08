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


# Gets and returns user input
def get_user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        handle_exit()
        

# One router request info (Paramiko)
def get_router_info():
    router = {
        'hostname': input("Enter the router's IP address: "),
        'port': input("Enter the port number (default is 22): ") or '22',  # Default to port 22 if no input
        'username': input("Enter the username: "),
        'password': input("Enter the password: ")
    }
    return router


# Two options Menu
def yes_or_no(title):
    # Ask user if they want to add another device
    add_more = input(title).strip().lower()
    if add_more == 'y' or add_more == 'n' :
        return add_more
    else:
        print('Please select a correct answer: "y" or "n"')
        return yes_or_no(title)


# Function to store routers in JSON format
def store_routers_in_json(filename):
    routers = []

    while True:
        # Get router info from user
        router = get_router_info()
        routers.append(router)

        # "yes or no" user's choice 
        title = "Do you want to store another device? (y/n): "
        user_choice = yes_or_no(title)
        if user_choice == 'y':
            pass
        if user_choice == 'n':
            break
            
    # Save the routers list to a JSON file
    with open(filename, 'w') as file:
        json.dump(routers, file, indent=4)

    print(f"All router information has been saved to {filename}")


# Find JSON file in current direcotry
def find_json_file():
    while True:
        try:
            # Get the filename from the user
            filename = get_user_input('Please enter the file name (with .json extension): ')

            # Check in the current directory
            current_dir = os.getcwd()
            filepath = os.path.join(current_dir, filename)

            if os.path.exists(filepath) and filepath.endswith('.json'):
                print(f"File found in the current directory: {filepath}")
                print_separator()
                return filename
            else:
                print("File not found in the current directory or it's not a JSON file.")
                print_separator()
        
        except KeyboardInterrupt:
            handle_exit()



# Read devices.json from the current directory
def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            devices = json.load(file)  # Parse the JSON file into a Python object
        return devices
    except FileNotFoundError:
        print("Error: The file 'devices.json' was not found.")
    except json.JSONDecodeError:
        print("Error: The file 'devices.json' contains invalid JSON.")
        
    return None


# get commands by the user and returns a list
def get_async_commands():
    commands = list()

    # Initializing loop
    while True: 
        # append command to the list
        commands.append(input("Please enter command: "))
        # invoke yes or no menu function
        choice = yes_or_no("Another command will be appended (y/n)?")
        # If choice yes, continues iteration
        if choice == 'y':
            pass
        # If choice no, stops iteration
        if choice == 'n':
            break
    return commands


# One router request info (Paramiko)
def create_async_playbook():
    name = input("Please enter playbook's name: ")
    # Invoke get_commands function
    commands = get_async_commands()
    # Building playbook based on the user input
    playbook = {name:commands}
    
    return playbook


# Function to store routers in JSON format
def store_async_playbooks(filename):
    playbooks = []

    # Check if the file exists and load the existing playbooks if present
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                playbooks = json.load(file)
            # if not initialize empty list
            except json.JSONDecodeError:
                playbooks = []

    # Continue adding new playbooks
    while True:
        # invoke create_playbook function
        playbook = create_async_playbook()
        # append playbook to a list
        playbooks.append(playbook)

        # "yes or no" user's choice 
        title = "Do you want to store another Playbook (y/n)?: "
        choice = yes_or_no(title)
        # If yes continue adding playbooks
        if choice == 'y':
            pass
        # If "n" stop iteration
        if choice == 'n':
            break
            
    # Save the updated playbooks list to the JSON file
    with open(filename, 'w') as file:
        json.dump(playbooks, file, indent=4)

    print(f"All playbooks have been saved to {filename}")



# Function to iterate and print each command as options
def print_playbook_names(playbooks):
    for index, playbook in enumerate(playbooks, start=1):
        for key, value in playbook.items():
            print(f"{index}. {key}")


# Function to search for a user input in the JSON keys
def search_playbook(playbooks):
    user_input = input("Enter playbook's name: ").strip()

    found = False
    for playbook in playbooks:
        for key, value in playbook.items():
            if user_input == key:  # Exact match with the key
                print("Playbook found!")
                return value  # Return the list of commands (value)
                found = True

    if not found:
        print("Invalid playbook name!")
        return search_playbook(playbooks)  # Recursively call to try again if not found


# Function to print playbooks an proceed to select one
# it return a list of commands
def async_playbooks_menu(file):

    print('Playbooks: ')
    # Look for the file in the current directory
    playbooks = read_json_file(file)

    # Print playbooks as a list of option
    print_playbook_names(playbooks)

    # Get user choice and look for the string in the playbooks file
    commands = search_playbook(playbooks)

    #print separator
    print_separator()
    # Make sure user want to execute the given name playbook
    user_choice = yes_or_no(f'Are you sure u want to proceed with: {commands}\n (y/n): ')

    if user_choice == 'y':
        return commands
        
    if user_choice == 'n':
        # return and ask again
        async_playbooks_menu()


# Pretty printing SSHCompletedProcess object
def print_objects(objects, hosts):

    # Process and print the results from each host
    i = 0
    for obj in objects:
        print(f"Results from host {hosts[i]['hostname']}:")
        for command in obj:
            print(f"Command executed: {command.command}")
            print(f"Exit status: {command.exit_status}")
            print(f"Standard Output:\n{command.stdout}")
            print(f"Standard Error (if any): {command.stderr}")
            print('#' * 50)
        i += 1




