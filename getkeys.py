# getkeys.py
# Citation: Box Of Hats (https://github.com/Box-Of-Hats )
import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
    [A,W,D] boolean values.
    '''
    output = [0, 0, 0, 0, 0]
    if 'W' in keys:
        output[1] = 1
    elif 'D' in keys:
        output[2] = 1
    elif 'S' in keys:
        output[3] = 1
    elif 'A' in keys:
        output[4] = 1
    else:
        output[0] = 1
    return output
