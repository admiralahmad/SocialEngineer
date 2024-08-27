"""
Program Name: Email Harvester App
Description: This Flask web application allows users to extract emails
            from specified URLs or local files through a user interface.
            It saves the harvested emails in both JSON and CSV formats
            for further use, such as in mass mailing campaigns.
Author: Ahmad
Date: 16/04/2024
Input: User inputs through web form either a URL to scrape or a file path to upload.
Output: Generates JSON and CSV files containing the harvested emails.
"""

import os
import json
import csv
from flask import Flask, request, render_template_string, send_from_directory
from werkzeug.utils import secure_filename

from emailHarvester.email_harvester1 import scrape_emails_from_url, process_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_PATH'] = 1000000  # Maximum file size in bytes

# Ensure the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def save_emails_to_json(emails, filename):
    """
    Save a list of emails to a JSON file.

    Parameters:
        emails (list): List of email addresses to save.
        filename (str): Filename for the JSON output.
    """
    with open(filename, 'w') as file:
        json.dump(emails, file)


def convert_json_to_csv(json_file, csv_file):
    """
    Convert a JSON file with emails to a CSV file.

    Parameters:
        json_file (str): Filename of the source JSON.
        csv_file (str): Filename of the target CSV.
    """
    with open(json_file, 'r') as jf:
        data = json.load(jf)
    with open(csv_file, 'w', newline='') as cf:
        writer = csv.writer(cf)
        for email in data:
            writer.writerow([email])


@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if request.method == 'POST':
        if 'url' in request.form and request.form['url']:
            url = request.form['url']
            emails = scrape_emails_from_url(url)
            json_filename = 'emails_from_url.json'
            csv_filename = 'emails_from_url.csv'
            save_emails_to_json(emails, json_filename)
            convert_json_to_csv(json_filename, csv_filename)
            message = f'Emails harvested from {url} and saved.'
        elif 'file' in request.files:
            file = request.files['file']
            if file.filename:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                emails = process_file(file_path)
                json_filename = 'emails_from_file.json'
                csv_filename = 'emails_from_file.csv'
                save_emails_to_json(emails, json_filename)
                convert_json_to_csv(json_filename, csv_filename)
                message = f'Emails harvested from {filename} and saved.'
            else:
                message = 'No file selected'

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


if __name__ == '__main__':
    app.run(debug=True)
