# Task automation with python of webpage title scraping by Avishkar Bhosale



import requests
import re
from colorama import init, Fore, Style

# Initialize color output
init(autoreset=True)

# Set your target URL here
URL = "https://www.example.com"   # Replace with any webpage URL
OUTPUT_FILE = "webpage_title.txt"

def scrape_title():
    print(Fore.CYAN + Style.BRIGHT + f"🌐 Scraping title from: {URL}")
    
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise error for bad responses
    except requests.RequestException as e:
        print(Fore.RED + f"❌ Request failed: {e}")
        return

    # Search for the <title> tag in HTML
    match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
    
    if match:
        title = match.group(1).strip()
        with open(OUTPUT_FILE, 'w') as f:
            f.write(f"Page Title: {title}\n")
        print(Fore.GREEN + f"✅ Title saved: '{title}' → {OUTPUT_FILE}")
    else:
        print(Fore.YELLOW + "⚠️ Title tag not found in HTML.")

if __name__ == "__main__":
    scrape_title()
