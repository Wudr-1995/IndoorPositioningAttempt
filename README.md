# A Simple Attempt for Indoor Positioning Based on WIFI Signal

# Environment
## System

```zsh
# Mac os
sudo visudo
# add the line below into the visudo with replacing the username of your own, 'whoami'
# username ALL=(ALL) NOPASSWD: /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport
```

## Some python package

1. subprocess
2. pandas
3. re

# How to use

## Set some position IDs

## Get the list of WIFI BSSIDs

Run the program with

```zsh
python getWifiList.py
```

and take your mac go around.

## Collect the received signal strength interval (RSSI) of different IDs

```zsh
mkdir samples
python getSamples.py
```

Hold your mac in the position, then input the position ID as the program ask.

## Location

Run the program with

```zsh
python locate.py
```

Input the true position ID as the program ask. The program will print the true position ID and the predicted position ID for your informantion

