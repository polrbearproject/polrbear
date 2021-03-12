reg add "hklm\software\microsoft\windows nt\currentversion\image file execution options\whoami.exe" /v Debugger /t REG_SZ /d "none.exe" /f
reg add "hklm\software\microsoft\windows nt\currentversion\image file execution options\ipconfig.exe" /v Debugger /t REG_SZ /d "none.exe" /f
reg add "hklm\software\microsoft\windows nt\currentversion\image file execution options\hostname.exe" /v Debugger /t REG_SZ /d "none.exe" /f
reg add "hklm\software\microsoft\windows nt\currentversion\image file execution options\powershell.exe" /v Debugger /t REG_SZ /d "none.exe" /f
