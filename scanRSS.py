import subprocess
import pandas as pd
import re

# Function to execute the airport command and parse its output
def list_wifi_networks():
    command = "sudo /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode != 0:
        raise Exception(f"Error: {error.decode('utf-8')}")

    output = output.decode('utf-8')

    # Regex pattern to match the lines in the airport command output
    pattern = re.compile(r"^(?P<ssid>[\S ]+)\s+(?P<bssid>(?:[0-9a-f]{2}:){5}[0-9a-f]{2})\s+(?P<rssi>-?\d+)\s+.*$", re.MULTILINE)
    networks = []

    for match in pattern.finditer(output):
        networks.append({
            "SSID": match.group('ssid').strip(),
            "BSSID": match.group('bssid'),
            "RSSI": match.group('rssi')
        })

    networks_df = pd.DataFrame(networks)

    return networks_df

# Call the function and print the results
# wifi_networks = list_wifi_networks()
# print(wifi_networks[wifi_networks.SSID == 'IHEP'])
# print(len(wifi_networks))
# for network in wifi_networks:
#     # if network['SSID'] == 'IHEP':
#     print(f"SSID: {network['SSID']}, BSSID: {network['BSSID']}, RSSI: {network['RSSI']}mdB")

