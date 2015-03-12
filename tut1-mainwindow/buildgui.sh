#!/bin/bash
rm ui_*.py
rm ui_*.pyc
pyside-uic mainWindow.ui > ui_mainWindow.py
