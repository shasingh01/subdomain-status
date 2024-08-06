import requests
import time
from tabulate import tabulate

# List of subdomains to check
subdomains = [
    'http://example.com',
    'http://nonexistent.example.com',
    'http://google.com',
    'http://localhost',
    'http://127.0.0.1'
]

def check_status(url):
    """Check the status of a URL."""
    try:
        response = requests.get(url, timeout=5)
        return 'Up' if response.status_code == 200 else 'Down'
    except requests.exceptions.RequestException:
        return 'Down'

def print_statuses(statuses):
    """Print the statuses in a tabular format."""
    table = [[subdomain, status] for subdomain, status in statuses.items()]
    print(tabulate(table, headers=['Subdomain', 'Status'], tablefmt='grid'))

def main():
    while True:
        statuses = {}
        for subdomain in subdomains:
            status = check_status(subdomain)
            statuses[subdomain] = status
        
        # Clear the screen before printing the updated table
        print("\033[H\033[J")
        print_statuses(statuses)
        
        # Wait for 60 seconds before the next check
        time.sleep(60)

if __name__ == '__main__':
    main()

