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

        # Editamos el campo de nuestro objeto json para almacenar el id del Frame para asi poder
        # movernos con el boton desde el menu principal
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


        '''
        values = ['one','two', 'three']
        print(values)
        for i in values:
            self.model.appendRow(QStandardItem(i))
        '''
        
        #self.lvListDatabases.clicked[QModelIndex].connect(self.on_clicked1)

        self.get_data()
    

    '''
    def on_clicked1(self, index):
        item = self.model.itemFromIndex(index)
        print (item.text())
    '''

    '''
    def on_clicked(self, index):
        data = self.lvListDatabases.currentIndex().data()
        index = self.lvLis
        tDatabases.currentIndex().row()
        print(index, data)
    '''

    def get_data(self):

        with open('src/list_databases.json', 'r') as f:
            data = json.load(f)
            print(data)
        
        #for i in data:
        #    self.model.appendRow(QStandardItem(data[i]))
        
        for i in data:
            self.model.appendRow(QStandardItem(i))
        
        # Seleccionamos el primer elemento del ListView
        ix = self.model.index(0, 0)
        sm = self.lvListDatabases.selectionModel()
        sm.select(ix, QtCore.QItemSelectionModel.Select)




    # Obtenemos la base de datos seleccionada en el ListView y la insertamos en
    # la ruta para abrir la base de datos
    def on_clicked(self):
        
        # Obtenemos el elemento seleccionado en el ListView
        route_database = self.lvListDatabases.currentIndex().data()
        
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["route_open_database"] = route_database
            f.seek(0)        
            json.dump(data, f, indent=4)
            f.truncate() 
    


    # Eliminamos la base de datos seleccionada en el ListView
    def delete_recent_database(self):
        route_database = self.lvListDatabases.currentIndex().data()

        # Eliminamos la base de datos seleccionada en el objeto json
        with open('src/list_databases.json', 'r+') as f:
            data = json.load(f)
            del data[route_database]
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        # Realizamos una limpieza del ListView insertando un arreglo vacio
        self.model = QStandardItemModel()
        self.lvListDatabases.setModel(self.model)
            
        values = []

        for i in values:
            self.model.appendRow(QStandardItem(i))

        self.get_data()
    


    '''
    def delete_recent_databases(self):
        with open('src/list_databases.json', 'r+') as f:
            data = json.load(f)
            del data['route_3']
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        self.model = QStandardItemModel()
        self.lvListDatabases.setModel(self.model)
            
        values = []

        for i in values:
            self.model.appendRow(QStandardItem(i))

        self.get_data()
    '''


    


        


        

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

