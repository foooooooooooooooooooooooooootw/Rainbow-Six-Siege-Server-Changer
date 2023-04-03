import os
import configparser

home = os.path.expanduser('~')
location = os.path.join(home, 'Documents','My Games', 'Rainbow Six - Siege')


filepath = ""
filename = "GameSettings.ini"

print("""
Australia (AUS)
Brazil (BRZ)
Central US (CUS)
East Asia (EAS)
East US (EUS)
Japan (JPN)
North Europe (NEU)
South Africa (SAF)
South US (SUS)
South East Asia (SEA)
United Arab Emirates (UAE)
West Europe (WEU)
West US (WUS)
""")
serverchange = input("Which server to change to?")


if serverchange.upper() not in ["AUS", "BRZ", "CUS", "EAS", "EUS", "JPN", "NEU", "SAF", "SUS", "SEA", "UAE", "WEU", "WUS"]:
    print("input not recognized")
    serverchange = input("Which server to change to?")

for root, dirs, files in os.walk(location):
    for name in files:

        if name == filename:      
            filepath = os.path.join (root, name)

        elif not filepath:
            print ("File not found")

config = configparser.ConfigParser()
config.read(filepath)

if serverchange == "AUS":
    config['ONLINE']['DataCenterHint'] = 'playfab/australiaeast'
elif serverchange == "BRZ":
    config['ONLINE']['DataCenterHint'] = 'playfab/brazilsouth'
elif serverchange == "CUS":
    config['ONLINE']['DataCenterHint'] = 'playfab/centralus'
elif serverchange == "EAS":
    config['ONLINE']['DataCenterHint'] = 'playfab/eastasia'
elif serverchange == "JPN":
    config['ONLINE']['DataCenterHint'] = 'playfab/japaneast'
elif serverchange == "EUS":
    config['ONLINE']['DataCenterHint'] = 'playfab/eastus'
elif serverchange == "NEU":
    config['ONLINE']['DataCenterHint'] = 'playfab/northeurope'
elif serverchange == "SAF":
    config['ONLINE']['DataCenterHint'] = 'playfab/southafricanorth'
elif serverchange == "SUS":
    config['ONLINE']['DataCenterHint'] = 'playfab/southcentralus'
    print("amongus")
elif serverchange == "SEA":
    config['ONLINE']['DataCenterHint'] = 'playfab/southeastasia'
elif serverchange == "UAE":
    config['ONLINE']['DataCenterHint'] = 'playfab/uaenorth'
elif serverchange == "WEU":
    config['ONLINE']['DataCenterHint'] = 'playfab/westeurope'
elif serverchange == "WUS":
    config['ONLINE']['DataCenterHint'] = 'playfab/westus'


with open(filepath, 'w') as configfile:  
    config.write(configfile)
