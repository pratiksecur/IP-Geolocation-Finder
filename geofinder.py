import ipinfo
import time

# Replace 'your_access_token' with your actual API token from ipinfo.io
access_token = 'your_access_token'
handler = ipinfo.getHandler(access_token)

# Function to get geolocation of an IP address
def get_geolocation(ip):
    details = handler.getDetails(ip)
    return {
        'IP Address': ip,
        'City': details.city,
        'Region': details.region,
        'Country': details.country,
        'Coordinates': f"{details.latitude}, {details.longitude}" if 'latitude' in details.all and 'longitude' in details.all else "N/A",
        'Organization': details.org
    }

# Function to process multiple IPs
def process_ip_addresses(ip_list):
    for ip in ip_list:
        geolocation = get_geolocation(ip.strip())  # Strip to remove any extra spaces
        print(f"Geolocation for IP: {geolocation['IP Address']}")
        print(f"  City: {geolocation['City']}")
        print(f"  Region: {geolocation['Region']}")
        print(f"  Country: {geolocation['Country']}")
        print(f"  Coordinates: {geolocation['Coordinates']}")
        print(f"  Organization: {geolocation['Organization']}")
        print("\n" + "-"*40 + "\n")

# Displaying the header (Metasploit-like style)
def display_header():
    header = r"""
  _____ _____     _____            ______ _           _           
 |_   _|  __ \   / ____|          |  ____(_)         | |          
   | | | |__) | | |  __  ___  ___ | |__   _ _ __   __| | ___ _ __ 
   | | |  ___/  | | |_ |/ _ \/ _ \|  __| | | '_ \ / _` |/ _ \ '__|
  _| |_| |      | |__| |  __/ (_) | |    | | | | | (_| |  __/ |   
 |_____|_|       \_____|\___|\___/|_|    |_|_| |_|\__,_|\___|_|   
                                                                  
                                                                  

IP Geolocation Finder Tool
--------------------------------------------------------------
Author: Pratik Gupta
Use this tool to find the geolocation of IP addresses.
--------------------------------------------------------------

"""
    print(header)

# Main interactive loop
def main():
    display_header()
    time.sleep(1)  # Adds a short delay for aesthetics
    print("Welcome to the IP Geolocation Finder!\n")

    while True:
        # Ask user to input IP address(es)
        ip_input = input("Enter IP addresses (comma-separated for multiple IPs) or 'exit' to quit: ")
        
        if ip_input.lower() == 'exit':
            print("\nExiting the IP Geolocation Finder. Goodbye!")
            break
        
        # Split input into a list of IP addresses
        ip_addresses = ip_input.split(',')
        
        # Call function to process each IP
        process_ip_addresses(ip_addresses)

if __name__ == "__main__":
    main()
