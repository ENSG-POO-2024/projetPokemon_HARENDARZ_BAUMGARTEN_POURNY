@echo off
echo Script to assist transform a .qrc file to a .py with pyrcc4. File must be in this .bat folder.
set /p input= Type name of .qrc file (without .qrc extension):
echo File name is: %input%.qrc
python -m PyQt5.pyrcc_main %input%.qrc -o %input%.py
pause