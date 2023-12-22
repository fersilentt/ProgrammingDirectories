import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QAbstractItemView
from PyQt5.uic import loadUi
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import json

import sys
import os
file = os.path.abspath("src")
sys.path.insert(0, file)


class FrameOptionDatabase(QtWidgets.QFrame):

    def __init__(self):
        super(FrameOptionDatabase,self).__init__()
        loadUi(file+"/view/ui/option_database/option_database.ui",self)

        # We edit the field of our json object to store the id of the Frame so that we can to move with the 
        # button from the main menu
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 0
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        self.pbDeleteRecentDatabase.clicked.connect(self.delete_recent_database)
        
        self.model = QStandardItemModel()
        self.lvListDatabases.setModel(self.model)
        #self.lvListDatabases.setObjectName("listView-1")
        self.lvListDatabases.setModelColumn(1)

        self.get_data()
    


    # We get the list of recently opened databases
    def get_data(self):

        with open('src/list_databases.json', 'r') as f:
            data = json.load(f)
            print(data)
        
        #for i in data:
        #    self.model.appendRow(QStandardItem(data[i]))
        
        for i in data:
            self.model.appendRow(QStandardItem(i))
        
        # Select the first item of the ListView
        ix = self.model.index(0, 0)
        sm = self.lvListDatabases.selectionModel()
        sm.select(ix, QtCore.QItemSelectionModel.Select)




    # We get the selected database in the ListView and insert it in the path to open the database
    def on_clicked(self):
        
        # Obtenemos el elemento seleccionado en el ListView
        route_database = self.lvListDatabases.currentIndex().data()
        
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["route_open_database"] = route_database
            f.seek(0)        
            json.dump(data, f, indent=4)
            f.truncate() 
    


    # Delete the selected database in the ListView
    def delete_recent_database(self):
        route_database = self.lvListDatabases.currentIndex().data()

        # Eliminamos la base de datos seleccionada en el objeto json
        with open('src/list_databases.json', 'r+') as f:
            data = json.load(f)
            del data[route_database]
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        # Perform a ListView cleanup by inserting an empty array
        self.model = QStandardItemModel()
        self.lvListDatabases.setModel(self.model)
            
        values = []

        for i in values:
            self.model.appendRow(QStandardItem(i))

        self.get_data()
    


    

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

