from scanRSS import list_wifi_networks
import pandas as pd
import os

def obtainWifiList(times):
	for i in range(0, times):
		print(f'{i}th scan started')
		bssid_list_path = './bssid_list.csv'
		wifi_list = list_wifi_networks()
		if wifi_list.shape[0] == 0:
			continue;

		if os.path.exists(bssid_list_path):
			bssid_list_ext = pd.read_csv(bssid_list_path, header=None)
			bssid_list_ext.columns = ['BSSID']
		else:
			bssid_list_ext = pd.DataFrame(columns=['BSSID'])

		bssid_list_cur = wifi_list[['BSSID']]
		bssid_list_new = bssid_list_cur[~bssid_list_cur['BSSID'].isin(bssid_list_ext['BSSID'])]
		bssid_list_cut = pd.concat([bssid_list_ext, bssid_list_new], ignore_index=True)

		bssid_list_cut.to_csv(bssid_list_path, header=False, index=False)

obtainWifiList(20)
