import paramiko

def get_device_info(ssh_client, ip_address):
    # Linux command
    stdin, stdout, stderr = ssh_client.exec_command('uname -a')
    linux_output = stdout.read().decode().lower()
    
    # If it's a Linux machine
    if 'linux' in linux_output:
        print(f"{ip_address} is a Linux machine.")
        return

    # Windows check - try running a Windows-specific command
    stdin, stdout, stderr = ssh_client.exec_command('cmd.exe /c ver')
    windows_output = stdout.read().decode().lower()

    if 'microsoft' in windows_output or 'windows' in windows_output:
        print(f"{ip_address} is a Windows machine.")
        return

    # Cisco command to check for Cisco devices
    stdin, stdout, stderr = ssh_client.exec_command('show version')
    cisco_output = stdout.read().decode().lower()

    if 'cisco' in cisco_output:
        print(f"{ip_address} is a Cisco device.")
        return


    # If none of the above commands match
    print("Could not determine the device type.")



def connect_to_router(router):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Trust the server automatically

    print(f'Connecting to {router["hostname"]}...')
    
    try:
        ssh_client.connect(
            hostname=router['hostname'], 
            port=int(router['port']),  # Convert port to integer
            username=router['username'], 
            password=router['password'],
            look_for_keys=False, 
            allow_agent=False
        )
        print(f"\nSuccessfully connected to {router['hostname']}!")
        
        # After successful connection, get device information
        get_device_info(ssh_client, router['hostname'])
        
    except paramiko.AuthenticationException:
        print(f"\nAuthentication failed when connecting to {router['hostname']}.")
    except paramiko.SSHException as sshException:
        print(f"\nSSH error occurred while connecting to {router['hostname']}: {sshException}")
    except paramiko.BadHostKeyException as badHostKeyException:
        print(f"\nInvalid host key for {router['hostname']}: {badHostKeyException}")
    except Exception as e:
        print(f"\nFailed to connect to {router['hostname']}: {e}")
    finally:
        ssh_client.close()




def multiple_connection(json):
    for device in json:
        connect_to_router(device)

