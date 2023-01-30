# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:02:01 2018

@author: Elijah Bennett (Ginsu)

Program notes: cmd is disabled via a registry key. 
Key location: HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System
Key name: DisableCMD The value should be: 0x00000000
    
Program instructions: Read the disablecmd key and if its not 0x00000000 then change it to that
"""

from winreg import *

def main():
    # Get the key, get the tuple, calculate a buffer to make value string
    # try to edit the reg key

    # open the key; key location: HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System; key name: DisableCMD
    key = OpenKey(HKEY_CURRENT_USER, 'Software\Policies\Microsoft\Windows\System', 0, KEY_ALL_ACCESS)
    TUPLE = QueryValueEx(key, 'DisableCMD') # Returns a tuple, (x, y) ; x is the keys value while y is the registry type
    
    # This is the value of the key; the original value is: 0x00000002
    VALUE = TUPLE[0]
    
    # The value size
    SIZE_1 = 8
    
    # How many digits the value is
    SIZE_2 = len(str(VALUE))
    
    # How many 0's to put in the value
    BUFFER = abs(SIZE_1 - SIZE_2)
    
    # If the value isnt 0, cmd is most likely disabled
    if int(VALUE) != 0:
        print('[!] Key value not equal to 0x00000000... lets fix that')
        print('[*] Attempting to change original value: {} to: 0x00000000'.format('0x' + '0' * BUFFER + str(VALUE)))
        try:
            # Edit the registry and replace the value 0x00000002 with 0x00000000
            editRegistry(key, TUPLE)
            print('[+] CMD re-enabling success!')
            print('[*] Original key value: {}'.format('0x' + '0' * BUFFER + str(VALUE)))
            print('[*] New key value: 0x00000000')
        except:
            print('[-] CMD re-enabling failed!')
    else:
        print('[+] Cmd is enabled in the registry.. maybe its a policy problem')
        
def editRegistry(key, TUPLE):
    # if its not 0x00000000 then change it to that
    
    # key, key name, reserved, registry key type (from the tuple), the value we want
    SetValueEx(key, 'DisableCMD', 0, TUPLE[1], 0)
    CloseKey(key)
    
if __name__ == '__main__':
    main()



