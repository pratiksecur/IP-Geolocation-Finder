# IP Geolocation Finder

The **IP Geolocation Finder** is a Python-based tool that allows users to input IP addresses and retrieve detailed geolocation information, such as city, region, country, coordinates, and organization. You can enter multiple IPs separated by commas or a single IP for quick lookup.

## Features

- Get the geolocation details of IP addresses.
- Input multiple IP addresses separated by commas.
- Provides the city, region, country, coordinates, and the organization associated with the IP.

## Sample Output

```bash
IP-Geolocation-Finder
Enter the IP Address to find the details:
Enter IP addresses (comma-separated for multiple IPs) or 'exit' to quit: 157.240.192.0

Geolocation for IP: 157.240.192.0
  City: Chennai
  Region: Tamil Nadu
  Country: IN
  Coordinates: 13.0878, 80.2785
  Organization: AS32934 Facebook, Inc.
```

## How to Use

### Step 1: Clone the Repository

First, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/IP-Geolocation-Finder.git
```

### Step 2: Navigate to the Directory

Move into the project directory:

```bash
cd IP-Geolocation-Finder
```

### Step 3: Add Your Access Token

Before running the script, you need to add your IPinfo API access token. 

1. Sign up at [ipinfo.io](https://ipinfo.io/signup) to get your access token.
2. Open the `geofinder.py` file in a text editor.
3. Find the line that reads:

   ```python
   access_token = 'your_access_token'
   ```

4. Replace `'your_access_token'` with your actual API token from IPinfo.

### Step 4: Install the Required Dependencies

Make sure you have Python installed on your system. You can install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

### Step 5: Run the Script

You can run the script by executing:

```bash
python geofinder.py
```
