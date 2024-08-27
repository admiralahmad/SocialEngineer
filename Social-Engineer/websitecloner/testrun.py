import os
import subprocess
import signal

# Function to list available server scripts in the 'servers' directory
def list_servers():
    servers_dir = 'websitecloner/servers'
    # Returns a list of Python files (end with .py) found in the specified directory
    return [f for f in os.listdir(servers_dir) if f.endswith('.py')]

# Function to start a server given its filename
def run_server(server):
    # Start the server script as a subprocess and return the subprocess object
    process = subprocess.Popen(["python", f"websitecloner/servers/{server}"])
    return process

# Main function that handles the menu and server execution
def main():
    while True:  # Continuous loop to allow repeated operations
        servers = list_servers()  # Get the list of server scripts
        print("Available Flask Servers:")
        for i, server in enumerate(servers, 1):  # Enumerate and display servers
            print(f"{i}. {server}")
        print(f"{len(servers) + 1}. Exit")  # Option to exit the program

        choice = input("Enter the number of the server you want to run: ")  # User input for selection
        try:
            choice_idx = int(choice) - 1  # Convert input into an index (zero-based)
            if choice_idx == len(servers):  # Check if the user chose to exit
                print("Exiting...")
                break  # Break the loop and exit
            elif 0 <= choice_idx < len(servers):  # Validate if the choice is within the range of available servers
                server_to_run = servers[choice_idx]  # Get the server to run based on user choice
                print(f"Running {server_to_run}... (Press Enter to stop)")
                process = run_server(server_to_run)  # Start the server

                input("Press Enter to stop the server...")  # Wait for the user to stop the server
                process.terminate()  # Terminate the server process
                process.wait()  # Ensure the server process has fully terminated
                print("Server stopped.")

                restart_choice = input("Do you want to go through the options again? (y/n): ")  # Ask if user wants to continue
                if restart_choice.lower() != 'y':  # Check if user wants to stop
                    break  # Break the loop if no
            else:
                print("Invalid selection. Please run the script again.")  # Handle invalid selections
        except ValueError:
            print("Please enter a valid number.")  # Handle non-integer inputs

if __name__ == "__main__":
    main()  # Execute main function when script is run directly
