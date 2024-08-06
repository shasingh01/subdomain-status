# subdomain-status
1. A Python script to check the status of subdomains and display it in a tabular format

## Requirements

- Python 3.x
- `requests` library
- `tabulate` library

## Installation

 Clone the repository:
 git clone https://github.com/shasingh01/subdomain-status.git

2. Navigate to the project directory:
3. cd subdomain-status
4. vim status_subdomains.py
5. Run the script from the command line.
6. When user run the script, it should clear the screen and print a table with the status of each subdomain.
The table will update every minute, showing the current status of each subdomain.

7. Check Known Subdomains:

Ensure that known subdomains like http://example.com and http://google.com show as 'Up'.
Ensure that a non-existent subdomain like http://nonexistent.example.com shows as 'Down'.

8. Check Local Subdomains:

If user have a local web server running, check if http://localhost and http://127.0.0.1 are correctly reported as 'Up' or 'Down'

9. Additional Testing
Stop and Start Local Server:

If user have a local server, stop it and observe the change in the script's output.
Restart the server and ensure the script updates the status correctly.
Simulate Network Issues:

Disconnect your internet and observe the change in the script's output.
Reconnect and ensure the script updates the status correctly.

Note: Script file status_subdomains.py
This README file contains all the necessary steps and instructions to set up the project, install dependencies, run the script, and push the code to a GitHub repository.


