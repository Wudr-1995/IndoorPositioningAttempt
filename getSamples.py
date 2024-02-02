from scanRSS import list_wifi_networks
import pandas as pd
import os

def obtainSample(pid):
	bssid_list_path = './bssid_list.csv'
	wifi_list = list_wifi_networks()

	if os.path.exists(bssid_list_path):
		bssid_list = pd.read_csv(bssid_list_path, header=None)
		bssid_list.columns = ['BSSID']
	else:
		print(f"{bssid_list_path} doesn't exists")
		return False

	sample = bssid_list.copy()
	sample['RSSI'] = 0

	for index, row in wifi_list.iterrows():
		if row['BSSID'] in sample['BSSID'].values:
			sample.loc[sample['BSSID'] == row['BSSID'], 'RSSI'] = int(row['RSSI'])
		else:
			pass

	sample['RSSI_normalized'] = (sample['RSSI'] - sample['RSSI'].min()) / (sample['RSSI'].max() - sample['RSSI'].min())
	output_path = f'./samples/sample_{pid}.csv'
	sample.to_csv(output_path)

for i in range(0, 13):
	pid = int(input('Enter the position id: '))
	obtainSample(pid)

