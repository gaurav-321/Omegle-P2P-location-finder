import os
import subprocess
import re
import geoip2.database

input_exec_loc = input("Enter Tshark file path:- ")
t_shark = input_exec_loc if input_exec_loc else r"C:\Program Files\Wireshark\tshark.exe"

os.system(f'"{t_shark}" -D')
input_device = input("Select Device:- ")

proc = subprocess.Popen([t_shark, f"-i {input_device}", '-f udp'], stdout=subprocess.PIPE)

reader = geoip2.database.Reader('GeoLite2-City.mmdb')
for line in iter(proc.stdout.readline, ''):
    try:
        line = str(line).strip()
        ips = re.findall(r"(?<= )\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?= )", line)
        response = reader.city(ips[1])
        print(response.country.name, response.city.name)
    except:
        pass
proc.kill()
