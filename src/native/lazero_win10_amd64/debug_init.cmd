@echo off
set AWK=E:\android-ndk-r10e\prebuilt\windows-x86_64\bin\awk.exe
set THISPATH=%CD%
powershell.exe -File find_process.ps1 "node.exe" | grep node | grep chrome_console | %AWK% "{print $1}" | xargs -iabc cmd /C "taskkill /F /PID abc"
powershell.exe -File find_process.ps1 "node.exe" | grep node | grep chrome_receive | %AWK% "{print $1}" | xargs -iabc cmd /C "taskkill /F /PID abc"
start /B cmd /C "cd eventService && node chrome_receive.js"
start /B cmd /C "cd replService && node chrome_console.js"

powershell.exe -File find_process.ps1 "python36.exe" | grep node | grep ptyproc_cmd.py | %AWK% "{print $1}" | xargs -iabc cmd /C "taskkill /F /PID abc"
cd shellService && python36 ptyproc_cmd.py
cd %THISPATH%
