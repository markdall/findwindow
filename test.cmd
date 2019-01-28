@echo off
cls

rem Start a window named blah for the python script to find and close
start "blah" cmd /k

python findwindow.py