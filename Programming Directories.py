# In this file we list all the libraries that our project needs to run
# we add in this file to be able to use py2app

# Modules of the  src/view files
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QLabel, QAbstractItemView
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtCore import Qt

import json
import importlib
import webbrowser
import validators

import sys
import os
file = os.path.abspath("src")
sys.path.insert(0, file)


# Modules of the src/controller files
from sqlalchemy.orm import sessionmaker


# Modules of src/model files
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref



# Main file that will start the application
from src.view.py.main import MainWindow





