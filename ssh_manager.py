import paramiko


# Test connection to the router 
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
    except Exception as e:
        print(f"\nFailed to connect to {router['hostname']}: {e}")
    finally:
        ssh_client.close()
