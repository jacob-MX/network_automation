import paramiko
import asyncio
import asyncssh
import time
import threading
import logging



# Define the main coroutine to connect to the SSH server and run the commands
async def connect_and_run(host, username, password, commands):
    
    # Initialize a list to store the result objects (output of each command)
    objects = []

    # Asynchronously ensure that the SSH connection is opened, used,
    # and properly closed when the operation is complete.
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        
        # Loop through the commands and run each command on the same connection
        for command in commands:
            try:
                # Asynchronously send the command and retrieve the result object
                obj = await connection.run(command)
                # Append the result object to the list
                objects.append(obj)
            except Exception as e:
                # Handle the case where the command fails
                print(f"Command '{command}' failed with error: {e}")

    return objects


# Modify run_multiple_clients to accept both hosts and commands
async def run_multiple_clients(hosts, commands):
    
    # Initialize a list to store the tasks (one per host)
    tasks = list()
    
    # Iterate over each host in the hosts list
    for host in hosts:
        # Create a task for each host to run the SSH commands using connect_and_run()
        task = connect_and_run(host['hostname'], host['username'], host['password'], commands)
        # Append each task to the tasks list
        tasks.append(task)

    # Run all the tasks asynchronously in parallel and collect the results
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    return results


def connect(ip, port, user, passwd):
    ssh_client = paramiko.SSHClient()   # Create an SSH client instance
    
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Bypass the security 
                                                                     #policy and trust the server
    print(f'Connecting to {ip}...')
    # Connect to the client
    ssh_client.connect(hostname     = ip,
                       port         = port,
                       username     = user,
                       password     = passwd,
                       look_for_keys= False, 
                       allow_agent  = False)
    return ssh_client


def get_shell(ssh_client):
    shell = ssh_client.invoke_shell() # Start an interactive SSH session
    return shell
    

def send_command(shell, command, expected_output=None, timeout=1):
    shell.send(command + '\n')  # Send the command
    output = ""
    end_time = time.time() + timeout

    while time.time() < end_time:
        if shell.recv_ready():  # Check if the output is ready to be received
            output += shell.recv(10000).decode()  # Append received output to the variable
        time.sleep(0.1)  # Small delay to prevent overloading the CPU

    return output


def show(shell, n=10000):
    output = shell.recv(n) # Receive up to 10,000 bytes of data
    return output.decode() # return and change binary to strings


def close(ssh_client):
    try:
        # Check if there is an active connection
        if ssh_client.get_transport() and ssh_client.get_transport().is_active():
            ssh_client.close()
            print("Connection closed successfully.")
        else:
            print("Connection is closed already!")
    except AttributeError:
        # Handle the case where get_transport() returns None
        print("Connection is closed already!")


def paramiko_commands_exe(host, commands):
    output = []
    client = connect(host['hostname'], host['port'], host['username'], host['password'])  # Connect to host
    print('Connection completed!\n')
    
    shell = get_shell(client)  # Start interactive shell session

    for command in commands:
        print(f'Sending command: {command}\n')
        
        # Handle 'sudo' by sending password after sudo
        if command.startswith('sudo'):
            shell.send(f"{command} -S\n")  # Send 'sudo' command with standard input password
            time.sleep(1)  # Small delay to allow password prompt
            shell.send(f"{host['password']}\n")  # Send the password
            time.sleep(1)  # Allow time for sudo to authenticate

        # Send regular command
        output.append(send_command(shell, command))

    print('Commands executed!\n')
    close(client)

    return output


def store_output(device, cisco_commands, output_list):
    result = paramiko_commands_exe(device, cisco_commands)
    output_list.append(result)



def multithreading_execution(devices, commands):
    # Initialize an empty list to store the outputs
    all_outputs = []
    threads = []

    # Create and start the threads
    for device in devices:
        thread = threading.Thread(target=store_output, args=(device, commands, all_outputs))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return all_outputs
