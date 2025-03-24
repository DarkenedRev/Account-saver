@ECHO OFF
TITLE HWID Checker
Color 0A

:: Stylish Header
ECHO ***************************************
ECHO          HWID CHECKER
ECHO ***************************************
ECHO.

:: Main loop
:start
cls  :: Clears the screen

:: Display hardware information
ECHO ***************************************
ECHO [1] Disk Drive Serial Number:
ECHO ***************************************
wmic diskdrive get serialnumber
ECHO.

ECHO ***************************************
ECHO [2] CPU Serial Number:
ECHO ***************************************
wmic cpu get serialnumber
ECHO.

ECHO ***************************************
ECHO [3] BIOS Serial Number:
ECHO ***************************************
wmic bios get serialnumber
ECHO.

ECHO ***************************************
ECHO [4] Motherboard Serial Number:
ECHO ***************************************
wmic baseboard get serialnumber
ECHO.

ECHO ***************************************
ECHO [5] smBIOS UUID:
ECHO ***************************************
wmic path win32_computersystemproduct get uuid
ECHO.

ECHO ***************************************
ECHO [6] MAC Address:
ECHO ***************************************
getmac
ECHO.

:: Footer
ECHO ***************************************
ECHO Press R to refresh or Q to exit.
ECHO ***************************************

:: Wait for user input
set /p userInput="Press R to refresh or Q to exit: "

:: Check for Refresh (R) or Exit (Q)
IF /I "%userInput%"=="R" (
    goto start  :: Refresh info by going back to the start label
)

IF /I "%userInput%"=="Q" exit  :: Exit the script if Q is typed
