import requests
import sys
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def get_ip_info(ip):
    try:
        print(f"\n{Fore.CYAN}Looking up information for IP: {ip}...\n")
        response = requests.get(f"http://ip-api.com/json/{ip}")
        api = response.json()

        if api.get('status') != "success":
            print(f"{Fore.RED}Invalid IP or lookup failed.")
            return

        print(f"""{Fore.GREEN}IP Lookup Result:
{Fore.YELLOW}Status     : {Fore.WHITE}{api.get('status')}
{Fore.YELLOW}Country    : {Fore.WHITE}{api.get('country')} ({api.get('countryCode')})
{Fore.YELLOW}Region     : {Fore.WHITE}{api.get('regionName')} ({api.get('region')})
{Fore.YELLOW}City       : {Fore.WHITE}{api.get('city')}
{Fore.YELLOW}ZIP        : {Fore.WHITE}{api.get('zip')}
{Fore.YELLOW}Latitude   : {Fore.WHITE}{api.get('lat')}
{Fore.YELLOW}Longitude  : {Fore.WHITE}{api.get('lon')}
{Fore.YELLOW}Timezone   : {Fore.WHITE}{api.get('timezone')}
{Fore.YELLOW}ISP        : {Fore.WHITE}{api.get('isp')}
{Fore.YELLOW}Org        : {Fore.WHITE}{api.get('org')}
{Fore.YELLOW}AS         : {Fore.WHITE}{api.get('as')}
""")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")

if __name__ == "__main__":
    # Show both the instructions and input prompt on the same screen
    print(f"{Fore.MAGENTA}Type 'u' to return to the menu without lookup. ", end="")  # Keeps it on the same line
    ip = input(f"{Fore.BLUE}Enter IP address to lookup: {Fore.WHITE}")  # Input prompt on the same screen

    # If user types 'u', return to the menu
    if ip.strip().lower() == 'u':
        print(f"{Fore.GREEN}Returning to menu...\n")
        sys.exit(0)  # Exit to return to batch menu

    # Proceed with IP lookup if valid input
    get_ip_info(ip)
    input(f"\n{Fore.MAGENTA}Press Enter to return to the menu...")
 
