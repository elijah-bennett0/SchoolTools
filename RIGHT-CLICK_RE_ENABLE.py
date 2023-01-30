# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:05:43 2019

@author: Elijah Bennett (Ginsu)

Program notes: 
    
Program instructions: 
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:02:01 2018

@author: Elijah Bennett (Ginsu)

Program notes: Right click disabled by reg key
Key location: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
Key name: NoViewContextMenu
    
Program instructions: If NoViewContextMenu's value isn't 0, then change it to that.
"""

from winreg import *

def main():
    # Get the key, get the tuple, calculate a buffer to make value string
    # try to edit the reg key

    # open the key; key location: HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System; key name: DisableCMD
    key = OpenKey(HKEY_CURRENT_USER, 'Software\Microsoft\Windows\CurrentVersion\Policies\Explorer', 0, KEY_ALL_ACCESS)
    TUPLE = QueryValueEx(key, 'NoViewContextMenu') # Returns a tuple, (x, y) ; x is the keys value while y is the registry type
    
    # This is the value of the key; the original value is: 0x00000001
    VALUE = TUPLE[0]
    
    # The value size
    SIZE_1 = 8
    
    # How many digits the value is
    SIZE_2 = len(str(VALUE))
    
    # How many 0's to put in the value
    BUFFER = abs(SIZE_1 - SIZE_2)
    
    # If the value isnt 0, right-click is most likely disabled
    if int(VALUE) != 0:
        print('[!] Key value not equal to 0x00000000... lets fix that')
        print('[*] Attempting to change original value: {} to: 0x00000000'.format('0x' + '0' * BUFFER + str(VALUE)))
        try:
            # Edit the registry and replace the value 0x00000002 with 0x00000000
            editRegistry(key, TUPLE)
            print('[+] Right-click re-enabling success!')
            print('[*] Original key value: {}'.format('0x' + '0' * BUFFER + str(VALUE)))
            print('[*] New key value: 0x00000000')
            print('[*] If right click still doesn\'t work, restart your computer.')
        except:
            print('[-] Right-click re-enabling failed!')
    else:
        print('[+] Right-click is enabled in the registry.\n[*] Try restarting your computer if it doesn\'t work.')
        
def editRegistry(key, TUPLE):
    # if its not 0x00000000 then change it to that
    
    # key, key name, reserved, registry key type (from the tuple), the value we want
    SetValueEx(key, 'NoViewContextMenu', 0, TUPLE[1], 0)
    CloseKey(key)
    
if __name__ == '__main__':
    main()



