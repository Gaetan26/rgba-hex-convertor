# 
from json import load
from os.path import exists


if exists('convertions/exchanges_values.json'):
    with open('convertions/exchanges_values.json', 'rb+') as f:
        dt = load(f); f.close(); exchanges_values = dt['switch_to_rgb']
else: raise FileNotFoundError()


def switch_to_rgba(HEX:str):

    HEX = (HEX.replace("#","")).lower()
    hex_len = HEX.__len__()

    if hex_len < 8:
        if hex_len == 3:
            HEX *= 2
            HEX += 'ff'
        elif hex_len == 6:
            HEX += 'ff'
        else: 
            return None
    elif hex_len > 8 : 
        return None

    R = (exchanges_values[HEX[0]]*16) + (exchanges_values[HEX[1]]*1)
    G = (exchanges_values[HEX[2]]*16) + (exchanges_values[HEX[3]]*1)
    B = (exchanges_values[HEX[4]]*16) + (exchanges_values[HEX[5]]*1)
    A = (exchanges_values[HEX[6]]*16) + (exchanges_values[HEX[7]]*1)

    return (R,G,B,A)