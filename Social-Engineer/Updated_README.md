# Social Engineer
Social Engineer is a python program that automated the process of a phishing campaign from cloning a webpage, scrapping the web for emails, sending a phishing email, to harvesting the credentials from the web server. The sections and subsections of this documents will explain each tool and its fuctionalities.

You can run the program using cmd or teminal: 
```bash
python socialengineer.py
```


## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.x
- PIP
- Libraries: `jinja2`, `openpyxl`, `flask`, `pandas`, `beautifulsoup4`

You can install the libraries using pip by running the requirements.sh for Debian( run chmod +x requirements.sh first) 
and requirements.ps1 for Windows.(REMEMBER TO RUN AS ROOT AND ADMINISTRATOR)

You can also manually instaal them using the libraries.
```bash
pip install jinja2 openpyxl beautifulsoup4 flask pandas
```

# Mailer

This Python script facilitates sending emails that can be dynamically generated from a Jinja2 HTML template with personalized placeholders and support for multiple file attachments. It uses the SMTP protocol for email transmission.

# Author

Ahmad Tijjani Saidu

# Date

17/04/2024

## Features

- Send plain and HTML emails
- Dynamic email body generation using Jinja2 templates
- Supports attachments (PDF, image, Word, Excel)
- Environment variables for secure SMTP configuration

## Setup

1. Clone this repository or download the script to your local machine.
2. Ensure you have a `.env` file in your script directory containing your SMTP server details:

```
SMTP_SERVER=your.smtp.server.com
SMTP_PORT=587
USERNAME=your_username
PASSWORD=your_password
```

3. Modify the script to include your specific email template or use the default path to a template.

## Usage

Run the script directly from the command line:

```bash
python mailer.py
python mass_mailer.py
```

You will be prompted to enter:
- Sender email address
- Email subject
- Decision to generate email from a template
- Path to the HTML template (if applicable)
- Email message or 'END' to finish message input
- Recipient's name and email address for single mailer
- Path to excel document for mass mailer
- Decision to attach files
- Path and type of the file to attach (if applicable)

## Email Template

The email template should be an HTML file with placeholders that can be rendered using Jinja2. For example:

```html
<html>
<body>
    <h1>Hello {{ name }}!</h1>
    <p>This is a test email for {{ email }}.</p>
</body>
</html>
```

## File Attachments

The script supports attaching files of types PDF, image, Word, and Excel. Ensure the file path is accessible and correct.

## Error Handling

The script includes basic error handling for SMTP errors and file-related issues.

## Security

Do not expose your SMTP credentials or `.env` file in public repositories or share them unsecured.

# Email Harvester

Email Harvester is a Python application designed to extract email addresses from given URLs or local files. It supports output in both JSON and CSV formats, making it versatile for various data handling and storage scenarios.

### Author

Ahmad El-rufai Bello

### Date

17/04/2024

### Features

- Harvest email addresses from URLs or local text files.
- Output harvested emails in JSON and CSV formats.
- Interactive command line and web interface options.
- Flask-powered web interface for easy operation via a browser.

### Installation

#### Prerequisites

Ensure you have Python installed on your system. Python 3.6 or higher is recommended. You will also need the following Python packages:

- pandas
- Flask
- requests
- regex

#### Installing Python Packages

Run the following command to install all required libraries:

```bash
pip install pandas flask beautifulsoup4
```

### Usage

#### Web Interface

1. Run the script:
   ```bash
   python name_of_file.py
   ```
2. Navigate to `http://localhost:5000` in your web browser.
3. Use the form to input a URL or upload a file from which you want to harvest emails.

#### Command Line Interface

1. Run the script:
   ```bash
   python name_of_file.py
   ```
2. Follow the on-screen prompts to choose between harvesting emails from a URL or a local file.
3. Enter the URL or file path as prompted.
4. The emails will be harvested and saved in the specified formats in a designated directory.

### Output

- The script saves harvested emails in JSON and CSV formats to a folder named `emailHarvester\Emails` within the script's running directory.
- Users can specify other formats and output directories via the command line interface.

### Notes

Some parts of this code were developed with the assistance of an AI Chatbot, providing robust and efficient pattern matching for email extraction.
