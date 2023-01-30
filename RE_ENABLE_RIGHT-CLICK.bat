@echo off
cls

REM Key location: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
REM Key name: NoViewContextMenu
REM The keys value should be 0x00000001 if right-clicking is disabled
REM To enable right-clicking, the key needs to be set to 0x00000000

echo [!] Attempting to overwrite the registry key
echo [!] Output below:

reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoViewContextMenu" /d "0x00000001" /t REG_SZ /f

