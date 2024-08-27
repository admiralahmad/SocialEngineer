"""
Program Name: Email Harvester
Description: This script extracts emails from given URLs or files and saves them in JSON and CSV formats.
Author: Ahmad El-rufai Bello
Date: 17/04/2024
Input: URL or filepath
Output: JSON and CSV files containing harvested emails
Note: Some parts of this code were developed with the assistance of an AI Chatbot.

How to run - command line
python name_of_file.py
"""
import pandas as pd 
import csv
import json
import os
import re
import requests
from flask import Flask, request, render_template_string
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
MAX_CONTENT_LENGTH = 1000000  # Maximum file size in bytes

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH  # Maximum file size in bytes


def extract_emails_from_text(text):
    """
    Extract emails from provided text using a regular expression.

    Parameters:
        text (str): Text from which to extract email addresses.

    Returns:
        list: A list of extracted email addresses.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)


def process_file(filepath):
    """
    Process a file to extract emails.

    Parameters:
        filepath (str): The path to the file to be processed.

    Returns:
        list: A list of extracted email addresses or an error message.
    """
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return extract_emails_from_text(content)
    except IOError as e:
        return [f'Error: {e}']


def scrape_emails_from_url(url):
    """
    Scrape emails from a specified URL.

    Parameters:
        url (str): The URL from which to scrape emails.

    Returns:
        list: A list of extracted email addresses or an error message.
    """
    try:
        response = requests.get(url)
        return extract_emails_from_text(response.text)
    except requests.RequestException as e:
        return [f'Error: {e}']


def save_emails_to_file(emails, filename, file_format='json', folder_name='emailHarvester/Emails'):
    folder_path = os.path.join(os.getcwd(),folder_name)

    # Check if the folder exists; if not, create it
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created at {folder_path}")

    # Construct the full file path
    file_path = os.path.join(folder_path, filename)

    # Save emails in JSON or CSV format based on file_format
    if file_format == 'json':
        with open(file_path, 'w') as json_file:
            json.dump(emails, json_file)
    elif file_format == 'csv':
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for email in emails:
                writer.writerow([email])
    elif file_format == 'excel':
        file_path = os.path.join(folder_path, filename + '.csv')
        # First save as CSV
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for email in emails:
                writer.writerow([email])
        # Then convert CSV to Excel
        df = pd.read_csv(file_path)
        excel_path = os.path.join(folder_path, filename + '.xlsx')
        df.to_excel(excel_path, index=False)
        file_path = excel_path            
    print(f"Emails saved to '{file_path}'.")


@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if request.method == 'POST':
        url = request.form.get('url')
        file = request.files.get('file')
        if url:
            emails = scrape_emails_from_url(url)
            save_emails_to_file(emails, 'emails_from_url.json', 'json')
            save_emails_to_file(emails, 'emails_from_url.csv', 'csv')
            message = f'Emails harvested from {url} and saved.'
        elif file and file.filename:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(file_path)
            emails = process_file(file_path)
            save_emails_to_file(emails, 'emails_from_file.json', 'json')
            save_emails_to_file(emails, 'emails_from_file.csv', 'csv')
            message = f'Emails harvested from {filename} and saved.'
        else:
            message = 'No URL or file provided'

    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body { padding: 20px; }
                .overflow-ellipsis { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; width: 100%; display: block; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Email Harvester</h1>
                <form method="post" enctype="multipart/form-data" class="mb-3">
                    <div class="form-group">
                        <label for="url">Enter URL:</label>
                        <input type="text" id="url" name="url" class="form-control" placeholder="https://example.com">
                    </div>
                    <div class="form-group">
                        <label for="file">Or Upload a File:</label>
                        <input type="file" id="file" name="file" class="form-control-file">
                    </div>
                    <button type="submit" class="btn btn-primary">Scrape Emails</button>
                </form>
                {{ message|safe }}
            </div>
        </body>
        </html>
    """, message=message)


def main_menu():
    while True:
        print("Please choose an option:")
        print("1 - Launch the Flask Web Application")
        print("2 - Use Command-line Email Harvesting")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            app.run(debug=True, use_reloader=False)
            break
        elif choice == '2':
            command_line_interface()
            break
        else:
            print("Invalid choice, please enter 1 or 2.")


def command_line_interface():
    # Secondary menu for command-line options
    while True:
        print("Choose the source for email harvesting:")
        print("1 - From a URL")
        print("2 - From a File")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            url_input = input("Enter URL to scrape emails from: ")
            if url_input:
                emails = scrape_emails_from_url(url_input)
                save_emails_to_file(emails, 'emails_from_url_cli.json', 'json')
                save_emails_to_file(emails, 'emails_from_url_cli.csv', 'csv')
                save_emails_to_file(emails, 'emails_from_url_cli.csv', 'excel')
            break
        elif choice == '2':
            file_path = input("Enter file path to extract emails from: ")
            if file_path:
                emails = process_file(file_path)
                if emails:
                    save_emails_to_file(emails, 'emails_from_file_cli.json', 'json')
                    save_emails_to_file(emails, 'emails_from_file_cli.csv', 'csv')
                    save_emails_to_file(emails, 'emails_from_url_cli.csv', 'excel')
            break
        else:
            print("Invalid choice, please enter 1 or 2.")


if __name__ == '__main__':
    main_menu()
