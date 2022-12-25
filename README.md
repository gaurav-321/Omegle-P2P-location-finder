# Omegle/P2P location finder

A simple python project which uses tshark to find packets going to remote ip and then find location using geoip2


---

## Requirements
- Tshark: You need to have tshark installed on your system and the file path should be provided as input to the program. If no file path is provided, the program will assume that tshark is installed in the default location (C:\Program Files\Wireshark\tshark.exe).
- GeoIP database: You need to have the GeoLite2-City database in the same directory as the program.
- Python packages: You need to have the geoip2 and subprocess packages installed.
## Usage
- Run the program.
- Select the device on which you want to monitor the traffic.
- The program will start monitoring the UDP traffic and will print the country and city names for the IP addresses involved in the traffic.
- To stop the program, press CTRL+C.

## To Run the project

```
python3 main.py
```

## Compiled Release

It has been compiled using pyinstaller and in order to run .exe make sure .mmdb file is in same location.
You can download release from below:-

https://github.com/gaurav-321/p2p_ip_finder/releases/tag/final


### This is a contributions for open source projects, if you are utilizing this project please give credit to my github Ordinary Pythoneer

