import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QAbstractItemView
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtCore import Qt

import json

import sys
import os
file = os.path.abspath("src")
sys.path.insert(0, file)




class FrameOptionDatabase(QtWidgets.QFrame):

    def __init__(self):
        super(FrameOptionDatabase,self).__init__()
        loadUi(file+"/view/ui/option_database/option_database.ui",self)

        # Editamos el campo de nuestro objeto json para almacenar el id del Frame para asi poder
        # movernos con el boton desde el menu principal
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 0
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        
        self.pbCreateDatabase.clicked.connect(self.open_directory)
        self.pbOpenDatabase.clicked.connect(self.open_file_database)
    

    def open_file_database(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","SQLite Files (*.db)", options=options)
        if file_name:
            print(file_name)

            with open('src/data.json', 'r+') as f:
                data = json.load(f)
                data["route_open_database"] = file_name
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
                



    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","SQLite Files (*.db)", options=options)
        if fileName:
            print(fileName)

    
    def open_directory(self):
        directory = str(QtWidgets.QFileDialog.getExistingDirectory())
        print(directory)


        

'''
app=QApplication(sys.argv)
mainwindow=FrameOptionDatabase()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
#widget.setFixedWidth(400)
#widget.setFixedHeight(300)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")
'''

