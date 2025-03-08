from flask import Flask, request
import logging
import requests

app = Flask(__name__)

# Set up logging to both console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('ip_log.txt'),  # Log to file
        logging.StreamHandler()             # Log to console
    ]
)

# IPinfo API token (replace with your actual token)
IPINFO_TOKEN = 'a80f59fde431ea'

def get_location(ip):
    """Fetch location details using the IPinfo API."""
    try:
        logging.info(f"Fetching location for IP: {ip}")  # Log to console and file
        response = requests.get(f'https://ipinfo.io/{ip}?token={IPINFO_TOKEN}')
        data = response.json()
        logging.info(f"Location data: {data}")  # Log to console and file
        return data
    except Exception as e:
        logging.error(f"Error fetching location: {e}")  # Log to console and file
        return {"error": str(e)}

@app.route('/')
def index():
    # Get the user's IP address
    user_ip = request.remote_addr
    logging.info(f"User IP: {user_ip}")  # Log to console and file
    # Get location details
    location = get_location(user_ip)
    # Log the IP address and location
    logging.info(f"Logged IP: {user_ip}, Location: {location}")  # Log to console and file
    return f"Hello! Your IP has been logged. Location: {location}"

if __name__ == '__main__':
    logging.info("Starting the IP logger...")  # Log to console and file
    app.run(host='0.0.0.0', port=5000, debug=False)  # Disable debug mode for production
