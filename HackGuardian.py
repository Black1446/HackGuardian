import requests
import time
from datetime import datetime
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Website-kaaga
website_url = 'https://example.com'

# BLACK1446
anonymous_mask = """
          ______
         /      \\
        |  O  O  |
        |    ^   |
        |   ---  |
         \______/
"""

# ASCII art for Developer CyberGuardian
developer_signature = """
        _______  __     _______  _______  __     _______ 
       /  ____|/  \\   |  ____|/  ____|/  \\   |  ____|  
      |  |__  / /\ \\  | |__   | |__   / /\ \\  | |__      
      |   __|/ ____ \\ |  __|  |  __|/ ____ \\ |  __|     
      |  |  / /    \\ \\| |____ | |___/ /    \\ \\| |____    
      |__| /_/      \\_\\______|______/_/      \\_\\______|   
"""

# Function to check website status
def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{Fore.WHITE}{anonymous_mask}")
            print(f"{Fore.BLUE}{developer_signature}")
            print(f"{Fore.GREEN}[{datetime.now()}] Website waa shaqaynayaa. Status code: 200")
        else:
            print(f"{Fore.WHITE}{anonymous_mask}")
            print(f"{Fore.BLUE}{developer_signature}")
            print(f"{Fore.YELLOW}[{datetime.now()}] Website wuxuu leeyahay status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.WHITE}{anonymous_mask}")
        print(f"{Fore.BLUE}{developer_signature}")
        print(f"{Fore.RED}[{datetime.now()}] Error: Website lama heli karo: {e}")

# Kormeerka website-ka
while True:
    check_website_status(website_url)
    time.sleep(3600)  # Waqti isku xigxiga ah 1 saac (3600 ilbiriqsi)
