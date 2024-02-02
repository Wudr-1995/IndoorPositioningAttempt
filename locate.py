from scanRSS import list_wifi_networks
import pandas as pd
import os

def obtainRSSI():
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
	return sample

def calMSE(sample, map_sample_path):
	mse = 0;
	map_sample = pd.read_csv(map_sample_path)
	for index, row in sample.iterrows():
		map_rssi = int(map_sample.loc[map_sample['BSSID'] == row['BSSID'], 'RSSI_normalized'].iloc[0])
		row_rssi = int(row['RSSI_normalized'])
		mse = mse + (map_rssi - row_rssi) ** 2
	mse = mse / sample.shape[0]
	return mse ** 0.5

def trailLocation():
	map_list = range(0, 16)
	for i in range(0, 10):
		truth = int(input('input the true position id: '))
		cur_rssi = obtainRSSI()
		pre = 0
		pre_mse = 1000
		for j in map_list:
			map_sample_path = f'./samples/sample_{j}.csv'
			mse = calMSE(cur_rssi, map_sample_path)
			if mse < pre_mse:
				pre_mse = mse
				pre = j
		print(f'Truth: {truth}, Prediction: {pre}')

trailLocation()
