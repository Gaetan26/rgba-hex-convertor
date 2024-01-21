# 
from json import load
from os.path import exists


if exists('convertions/exchanges_values.json'):
    with open('convertions/exchanges_values.json', 'rb+') as f:
        dt = load(f); f.close(); exchanges_values = dt['switch_to_hex']
else: raise FileNotFoundError()


def switch_to_hex(RGBA:tuple | list):
    
    RGBA = list(RGBA)
    rgba_len = RGBA.__len__()

    if rgba_len == 3:
        RGBA.append(255)
    elif rgba_len < 3 or rgba_len > 4:
        return None

    HEX = "#"
    for i in RGBA:
        division, modulo = int(int(i)/16), int(int(i)%16)
        division, modulo = str(division), str(modulo)
        i = exchanges_values[division]+exchanges_values[modulo]
        HEX += i
    
    return HEX