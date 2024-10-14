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


def print_separator():
    # Get the terminal size
    terminal_size = os.get_terminal_size()

    # Define the pattern
    pattern = '>><<>><<'
    
    # Calculate how many times the pattern can fit into the terminal width
    repeat_count = terminal_size.columns // len(pattern)
    
    # Create the separator by repeating the pattern
    separator = pattern * repeat_count
    
    # If the pattern does not perfectly fit, slice the string to match the exact terminal width
    separator = separator[:terminal_size.columns]
    
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


# Two options Menu
def yes_or_no(title):
    # Ask user if they want to add another device
    add_more = input(title).strip().lower()
    if add_more == 'y' or add_more == 'n' :
        return add_more
    else:
        print('Please select a correct answer: "y" or "n"')
        return yes_or_no(title)
        

# One router request info (Paramiko)
def get_router_info():
    router = {
        'hostname': input("Enter the router's IP address: "),
        'port': input("Enter the port number (default is 22): ") or '22',  # Default to port 22 if no input
        'username': input("Enter the username: "),
        'password': input("Enter the password: ")
    }
    return router
    

# Function to store devices in JSON format
def append_device(filename):
    devices = []

    # Check if the file exists and load the existing playbooks if present
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                devices = json.load(file)
            # if not initialize empty list
            except json.JSONDecodeError:
                devices = []

    # Continue adding new devices
    while True:
        # invoke create_playbook function
        device = get_router_info()
        # append playbook to a list
        devices.append(device)

        # "yes or no" user's choice 
        title = "\nDo you want to store another device (y/n)?: "
        choice = yes_or_no(title)
        
        # If yes continue adding playbooks
        if choice == 'y':
            pass
        # If "n" stop iteration
        if choice == 'n':
            break
            
    # Save the updated playbooks list to the JSON file
    with open(filename, 'w') as file:
        json.dump(devices, file, indent=4)

    print(f"All devices have been saved to {filename}")


def add_new_device():
    """Fetch and display available OS devices."""
    
    path = f"devices/"
    
    # List all JSON files in the selected directory
    json_files = [f for f in os.listdir(path) if f.endswith('.json')]
    
    # Print the available OS options
    print("\nWhich OS is your device?")
    for i, file in enumerate(json_files, start=1):
        # Display the file names without the .json extension
        print(f"{i}. {file.replace('.json', '')}")
    
    # Get the user's selection
    try:
        user_choice = int(input("\nSelect an option by number: ")) - 1
        if user_choice < 0 or user_choice >= len(json_files):
            raise ValueError
    except ValueError:
        print("Invalid option. Please select a valid number.")
        return get_operating_system_files(command_type)  # Retry in case of invalid input

    # Read the selected JSON file
    selected_file = os.path.join(path, json_files[user_choice])
    
    append_device(selected_file)


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
        title = "\nDo you want to store another Playbook (y/n)?: "
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



def playbooks_os_menu(command_type):
    """Fetch and display available OS files for the selected command type."""
    # Set the path based on the command type (dependent or independent)
    path = f"playbooks/{command_type}_commands"
    
    # List all JSON files in the selected directory
    json_files = [f for f in os.listdir(path) if f.endswith('.json')]
    
    # Print the available OS options
    print("\nWhich operating system would you like to add the playbook to?")
    for i, file in enumerate(json_files, start=1):
        # Display the file names without the .json extension
        print(f"{i}. {file.replace('.json', '')}")
        
    return json_files, path


def add_new_playbook(command_type):

    # print os options for playbooks
    json_files, path = playbooks_os_menu(command_type)
    
    # Get the user's selection
    try:
        user_choice = int(input("\nSelect an option by number: ")) - 1
        if user_choice < 0 or user_choice >= len(json_files):
            raise ValueError
    except ValueError:
        print("Invalid option. Please select a valid number.")
        return get_operating_system_files(command_type)  # Retry in case of invalid input

    # Read the selected JSON file
    selected_file = os.path.join(path, json_files[user_choice])
    
    store_async_playbooks(selected_file)


def devices_os_menu():
    """Fetch and display available OS devices."""
    path = "devices"
    
    # List all JSON files in the selected directory
    json_files = [f for f in os.listdir(path) if f.endswith('.json')]
    
    # Print the available OS options
    print("\nWhich operating system would you like to execute?")
    for i, file in enumerate(json_files, start=1):
        # Display the file names without the .json extension
        print(f"{i}. {file.replace('.json', '')}")
    
    return json_files

def get_json_devices_by_os():
    """Get the devices from the selected OS JSON file."""
    json_files = devices_os_menu()
    
    # Get user input to select the OS
    choice = int(input("\nSelect the number corresponding to the OS: "))
    
    if 1 <= choice <= len(json_files):
        selected_file = json_files[choice - 1]
        
        # Load the selected JSON file
        with open(os.path.join("devices", selected_file), "r") as f:
            devices = json.load(f)
        
        # Return the list of devices
        return devices, selected_file
    else:
        print("Invalid choice. Please try again.")
        return get_json_devices_by_os()


def playbooks_menu(method, file):
    
    file_path = f"playbooks/{method}_commands/{file}"
    
    # Load the JSON file containing commands
    with open(file_path, 'r') as file:
        commands = json.load(file)
        
    # Display a menu of command options
    print("Please select a command to run:")
    for index, command in enumerate(commands, 1):
        print(f"{index}. {list(command.keys())[0]}")
        
    return commands


def get_playbook_by_name(commands):
    
    # Ask the user to select a command
    choice = int(input("\nEnter the number of the Playbook to run: ")) - 1
    if choice < 0 or choice >= len(commands):
        print("Invalid choice. Please try again.")
        return get_playbook_by_name(commands)
        
    return list(commands[choice].values())[0]  # Return the command list


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





