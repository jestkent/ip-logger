from flask import Flask, request
import logging
import requests

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='ip_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# IPinfo API token (replace with your actual token)
IPINFO_TOKEN = 'a80f59fde431ea'

def get_location(ip):
    """Fetch location details using the IPinfo API."""
    try:
        print(f"Fetching location for IP: {ip}")  # Debug print
        response = requests.get(f'https://ipinfo.io/{ip}?token={IPINFO_TOKEN}')
        data = response.json()
        print(f"Location data: {data}")  # Debug print
        return data
    except Exception as e:
        print(f"Error fetching location: {e}")  # Debug print
        return {"error": str(e)}

@app.route('/')
def index():
    # Get the user's IP address
    user_ip = request.remote_addr
    print(f"User IP: {user_ip}")  # Debug print
    # Get location details
    location = get_location(user_ip)
    # Log the IP address and location
    logging.info(f"IP: {user_ip}, Location: {location}")
    print(f"Logged IP: {user_ip}, Location: {location}")  # Debug print
    return f"Hello! Your IP has been logged. Location: {location}"

if __name__ == '__main__':
    print("Starting the IP logger...")  # Debug print
    app.run(host='0.0.0.0', port=5000, debug=True)  # Enable debug mode