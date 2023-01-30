# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 11:28:31 2018

@author: Elijah Bennett (Ginsu)

Program notes: enable policy editor (gpedit) via adding a key in the registry. 
cmd create key command: REG add "HKCU\Software\Policies\Microsoft\MMC\{8FC0B734-A0E1-11D1-A7D3-0000F87571E3}" /v Restrict_Run /t REG_DWORD /d 0 /f
    
winreg create key docs:
winreg.CreateKey(key, sub_key)
Creates or opens the specified key, returning a handle object.

key is an already open key, or one of the predefined HKEY_* constants.

sub_key is a string that names the key this method opens or creates.

If key is one of the predefined keys, sub_key may be None. In that case, the handle returned is the same key handle passed in to the function.

If the key already exists, this function opens the existing key.

The return value is the handle of the opened key. If the function fails, an OSError exception is raised.


Program instructions: create the key above in the registry to enable gpedit
"""
from winreg import *

def main():
    # Just call the function here
    createRegKey()
    
    
def createRegKey():
    # Try to create the key, otherwise report the error
    try:
        CreateKeyEx(HKEY_CURRENT_USER, 'Software\Policies\Microsoft\MMC\{8FC0B734-A0E1-11D1-A7D3-0000F87571E3}\Restrict_Run', 0, KEY_ALL_ACCESS)
        print('[+] Key Created')
        print('[+] GPEDIT should now be accessible')
    except OSError as e:
        print('[-] Failed. Error: {}'.format(e))
    
    
if __name__ == '__main__':
    main()


