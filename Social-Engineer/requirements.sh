#!/bin/bash

# Function to check if command exists
command_exists() {
    type "$1" &> /dev/null
}

# List of libraries to install with pip
libraries_to_install="jinja2  pandas openpyxl beautifulsoup4 flask"

# Check if Python is installed
if command_exists python3; then
    echo "Python is already installed."
else
    echo "Python is not installed. Installing Python..."
    # Install Python 3 - adjust the installation command based on your OS or preferences
    # Here we assume Debian-based systems for example purposes
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
fi

# Check again to make sure installation was successful
if command_exists python3; then
    echo "Installing Python libraries: $libraries_to_install"
    # Using python3 -m pip to ensure we are calling the correct pip
    python3 -m pip install $libraries_to_install
else
    echo "Failed to install Python. Please install Python manually."
fi

