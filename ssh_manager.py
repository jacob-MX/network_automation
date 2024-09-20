import paramiko
import asyncio
import asyncssh



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
