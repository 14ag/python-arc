@echo off
setlocal enabledelayedexpansion

REM Get the current value of "lines to scroll"
for /f "usebackq tokens=3" %%i in (`reg query "HKCU\Control Panel\Mouse" /v "WheelScrollLines" 2^>nul`) do (
    set "currentValue=%%i"
)

REM Toggle the value between 4 and 1
if "%currentValue%"=="4" (
    set "newValue=1"
) else (
    set "newValue=4"
)

REM Update the registry with the new value
reg add "HKCU\Control Panel\Mouse" /v "WheelScrollLines" /t REG_SZ /d "%newValue%" /f >nul

REM Notify the user about the change
echo "lines to scroll" option has been set to %newValue%.

endlocal
