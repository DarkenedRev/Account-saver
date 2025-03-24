@echo off
echo Downloading Python 3.10.5 installer...
curl -L -o python-installer.exe https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe

echo Installing Python 3.10.5...
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

echo Installing pip if it's not already installed...
python -m ensurepip --upgrade

echo Installing requests via pip...
python -m pip install requests

echo Deleting Python installer...
del python-installer.exe

echo Python 3.10.5 and requests have been installed successfully!
pause