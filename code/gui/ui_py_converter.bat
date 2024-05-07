@echo off
echo Script to assist transform a .ui file to a .py with PyQt5. File must be in this .bat folder.
set /p input= Type name of .ui file (without .ui extension):
echo File name is: %input%.ui
python -m PyQt5.uic.pyuic -x %input%.ui -o %input%.py
pause