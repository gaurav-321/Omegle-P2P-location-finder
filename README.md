# Omegle-P2P-Location-Finder 🌍💻

## Description

Omegle-P2P-Location-Finder is a Python program designed to monitor network traffic using `tshark`, identify remote IP addresses, and determine their geographical locations using the GeoIP2 database. This tool helps in tracking the physical location of individuals based on their network activity.

## Features
- Monitors UDP traffic for specific IPs.
- Captures network traffic using `tshark`.
- Resolves IP addresses to geographic locations using the GeoIP2 library.
- Prints country and city names associated with remote IP addresses.

## Installation

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage

Here's a basic example of how to use the program:

```python
# main.py
import os
import subprocess
import re
from geoip2.database import Reader

def capture_traffic():
    # Capture network traffic using tshark
    result = subprocess.run(['tshark', '-i', 'eth0', '-Y', 'udp'], capture_output=True, text=True)
    return result.stdout

def extract_ips(traffic):
    # Extract IP addresses from the captured traffic
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ips = re.findall(ip_pattern, traffic)
    return ips

def get_location_info(ip_address):
    # Initialize GeoIP2 client and fetch location information
    reader = Reader('GeoLite2-City.mmdb')
    location = reader.city(ip_address)
    reader.close()
    return {
        'country_name': location.country.name,
        'city': location.city.name,
        'latitude': location.location.latitude,
        'longitude': location.location.longitude
    }

def main():
    traffic = capture_traffic()
    ips = extract_ips(traffic)
    for ip in ips:
        print(f"IP: {ip}")
        location_info = get_location_info(ip)
        print(location_info)

if __name__ == "__main__":
    main()
```

## Configuration

- **tshark**: Ensure `tshark` is installed and accessible from your system.
- **GeoLite2-City.mmdb**: Download the MaxMind GeoLite2 City database and place it in the same directory as your script.

## Tests

To run tests, ensure you have all dependencies installed and execute:
```bash
pytest test_main.py
```

## Project Structure

```
Omegle-P2P-Location-Finder/
├── README.md
├── main.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Developed by gag3301v 🌐