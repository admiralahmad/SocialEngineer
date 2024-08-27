import requests
from bs4 import BeautifulSoup
import os

def clone_website():
    # Ask user for the URL of the website to clone
    url = input("Enter the URL of the website to clone: ").strip()

    # Check if the URL starts with 'http://' or 'https://', if not, add 'http://'
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    # Send a GET request to the URL
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Failed to clone website:", e)
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Ask user for the name to save the cloned file
    filename = input("Enter the name to save the cloned file (without extension): ").strip()

    # Save the original HTML content
    with open(f"{filename}.html", 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print("Website cloned successfully. Cloned file saved as:", f"{filename}.html")

if __name__ == "__main__":
    clone_website()