import os
import subprocess

# Function to list all server scripts in the 'servers' directory
def list_servers():
    servers_dir = 'websitecloner/servers'
    # List comprehension to find files ending with '.py' in the specified directory
    return [f for f in os.listdir(servers_dir) if f.endswith('.py')]

# Function to run a selected server script
def run_server(server):
    # Starts the server script as a subprocess
    process = subprocess.Popen(["python", f"websitecloner/servers/{server}"])
    return process

def main():
    # Retrieve the list of server scripts
    servers = list_servers()
    print("Available Servers:")
    # Enumerate and print each server script with an index for user selection
    for i, server in enumerate(servers, 1):
        print(f"{i}. {server}")
    # Provide an option to exit
    print(f"{len(servers) + 1}. Exit")

    # User input for selecting a server to run or to exit
    choice = input("Enter the number of the server you want to run: ")
    try:
        # Convert choice to integer and adjust for 0-based index
        choice_idx = int(choice) - 1
        # Check if the user chose to exit
        if choice_idx == len(servers):
            print("Exiting...")
            return  # Exit the function, thus ending the script
        # If a valid server script is selected
        elif 0 <= choice_idx < len(servers):
            server_to_run = servers[choice_idx]  # Determine the selected server
            print(f"Running {server_to_run}... (Press Enter to stop)")
            # Start the selected server as a subprocess
            process = run_server(server_to_run)

            # Wait for user input to stop the server
            input("Press Enter to stop the server...")
            # Terminate the server after receiving input
            process.terminate()
            # Wait for the termination to complete
            process.communicate()
            print("Server stopped.")  # Confirm the server has been stopped
        else:
            print("Invalid selection.")
    except ValueError:
        # Error handling for wrong integer input
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
