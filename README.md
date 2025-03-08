IP Logger with Geolocation
This is a simple IP logger that records the IP address, approximate location, and privacy details (VPN, proxy, or Tor usage) of visitors using the ipinfo.io API.

Features
Logs the visitor's IP address.

Fetches geolocation data (city, region, country, etc.) using the ipinfo.io API.

Detects if the visitor is using a VPN, proxy, or Tor.

Logs all details to both the console and a file (ip_log.txt).

How to Use
Local Setup
Clone the repository:

bash
Copy
git clone https://github.com/your-username/ip-logger.git
cd ip-logger
Install dependencies:

bash
Copy
pip install -r requirements.txt
Replace the IPINFO_TOKEN in app.py with your actual API token from ipinfo.io.

Run the script:

bash
Copy
python app.py
Access the server at http://localhost:5000.

Deploy to Render
Sign up for a free account at Render.

Create a new Web Service and connect your GitHub repository.

Configure the service:

Build Command: pip install -r requirements.txt

Start Command: python app.py

Deploy the app and access it using the public URL provided by Render.

Example Output
Logs
Copy
2023-10-15 12:34:56,789 - User IP: 123.45.67.89
2023-10-15 12:34:56,789 - Fetching location for IP: 123.45.67.89
2023-10-15 12:34:56,789 - Location data: {'ip': '123.45.67.89', 'city': 'New York', 'region': 'New York', 'country': 'US', 'vpn': False, 'proxy': False, 'tor': False}
2023-10-15 12:34:56,789 - Logged IP: 123.45.67.89, Location: {'ip': '123.45.67.89', 'city': 'New York', 'region': 'New York', 'country': 'US', 'vpn': False, 'proxy': False, 'tor': False}
Response Message
Copy
Hello! Your IP has been logged. Location: {'ip': '123.45.67.89', 'city': 'New York', 'region': 'New York', 'country': 'US', 'vpn': False, 'proxy': False, 'tor': False}
Notes
Replace your_ipinfo_token_here in app.py with your actual API token from ipinfo.io.

Ensure compliance with privacy laws (e.g., GDPR, CCPA) when collecting IP addresses and location data.

The ip_log.txt file will not persist on Render’s free tier. Use a database (e.g., SQLite, PostgreSQL) for permanent log storage.

Privacy Detection
The app detects if a visitor is using a VPN, proxy, or Tor using the privacy field from the ipinfo.io API. If detected, the response message will include:

"You are using a VPN."

"You are using a proxy."

"You are using Tor."

License
This project is licensed under the MIT License. See the LICENSE file for details.
