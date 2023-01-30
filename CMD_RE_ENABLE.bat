@echo off

cls

REM Key location: HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System
REM Key name: DisableCMD
REM The keys value should be 0x00000002 if cmd is disabled
REM To enable cmd, the key needs to be set to 0x00000000

echo [!] Attempting to overwrite the registry key!
echo [!] Output below:

reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System" /v "DisableCMD" /d "0x00000002" /t REG_SZ /f

REM uh so this pretty much just removes the key and 
REM makes a new 'look-alike'