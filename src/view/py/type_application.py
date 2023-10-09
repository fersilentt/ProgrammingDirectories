import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtCore import Qt

import json

import sys
import os
file = os.path.abspath("src")
sys.path.insert(0, file)



class FrameTypeApplication(QtWidgets.QFrame):

    def __init__(self):
        super(FrameTypeApplication,self).__init__()
        loadUi(file+"/view/ui/type_application/list.ui",self)

        self.tableWidget.setHorizontalHeaderLabels(["Id","Name", "Type Creation", "Id Type Creation"])
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)


        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setColumnHidden(0,True)
        self.tableWidget.setColumnHidden(3,True)


        icon_add  = QtGui.QPixmap(os.path.abspath("src/static/add.svg"))
        icon_update  = QtGui.QPixmap(os.path.abspath("src/static/update.svg"))
        icon_delete  = QtGui.QPixmap(os.path.abspath("src/static/delete.svg"))
        
        self.pbAdd.setIcon(QtGui.QIcon(icon_add))
        self.pbEdit.setIcon(QtGui.QIcon(icon_update))
        self.pbDelete.setIcon(QtGui.QIcon(icon_delete))
        

        self.pbAdd.clicked.connect(lambda: self.add_update_window_modal(0))
        self.pbEdit.clicked.connect(lambda: self.add_update_window_modal(1))
        self.pbDelete.clicked.connect(self.delete_window)

        self.get_data() 








    # FUNCIONES DE LAS VENTANAS

    def add_update_window_modal(self, id_window_modal):

        self.window = QtWidgets.QMainWindow()
        uic.loadUi(file+"/view/ui/type_application/form.ui", self.window)
        self.window.show()

        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window = str_id_window['window_table_id']

        
        if id_window_modal != 0:

            r = self.tableWidget.currentRow()

            try:
                id = self.tableWidget.item(r,0).text()
                name = self.tableWidget.item(r,1).text()
            except IndexError as e:
                self.lMessageList.setText('<font color="red">Please select a data</font>')
                return
            
            self.window.leName.setText(name)
            self.window.pbAddUpdate.setText("Update")
            self.window.pbAddUpdate.clicked.connect(lambda: self.update_data(id,self.window.leName.text()))


        else:
            self.window.pbAddUpdate.setText("Add")
            self.window.pbAddUpdate.clicked.connect(lambda: self.add_data(self.window.leName.text(), id_window))
        




    def delete_window(self): 

        r = self.tableWidget.currentRow()
        id = self.tableWidget.item(r,0).text()

        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("Do you want to delete this data?")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes!")
            self.delete_data(id)
        else:
            print("No!")
    


    def select_rows(self, selection: list):
        for i in selection:
            self.tableWidget.selectRow(i)



    def insert_frame_id(self):
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 2
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 


    
    def go_window(self): 

        r = self.tableWidget.currentRow()
        id = self.tableWidget.item(r,0).text()

        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["window_table_id"] = id
            data["window_type_application_id"] = id
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        


            
        
    def back_window(self):

        # Abrimos el id de la ventana anterior
        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window_programming_language = str_id_window['window_programming_language_id']

        # Guardamos el id de la ventana especifica en el id de la ventana principal
        # para despues obtener los datos de ese id especifico
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["window_table_id"] = id_window_programming_language
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        

    








    # FUNCIONES PARA REALIZAR EL CRUD 

    def get_data(self):
    
        from controller.type_application.list import List
        from controller.type_application.count import Count
        
        lista = List.list_data()
        count_rows = Count.count_rows()

        tablerow=0

        self.tableWidget.setRowCount(count_rows)
        
        for id, name, name_type_creation, id_type_creation in zip(*lista): 

            item_id = QtWidgets.QTableWidgetItem()
            item_id_type_creation = QtWidgets.QTableWidgetItem()
            
            item_id.setData(Qt.EditRole, id)
            item_id_type_creation.setData(Qt.EditRole, id_type_creation)

            
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item_id))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(name_type_creation))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(item_id_type_creation))

            tablerow+=1

        list_selection = [0]
        self.select_rows(list_selection)




    def add_data(self, name, id_type_creation):  

        from controller.type_application.insert import Insert

        if self.validation_add_update_window_modal(name):
            Insert.add_data(name, id_type_creation)
            self.window.hide()
            self.lMessageList.setText('<font color="green">Data added successfully</font>')
            self.get_data()



    def update_data(self, id, name):

        from controller.type_application.update import Update

        if self.validation_add_update_window_modal(name):
            Update.update_data(id, name)
            self.window.hide()
            self.lMessageList.setText('<font color="green">Data updated successfully</font>')
            self.get_data()



    def delete_data(self, id):

        from controller.type_application.delete import Delete
        Delete.delete_data(id)
        self.lMessageList.setText('<font color="green">Data deleted successfully</font>')
        self.get_data()














    # FUNCIONES QUE VAN A VALIDAR LAS CAJAS DE TEXTO
    def validation_add_update_window_modal(self, name):
        if(len(name) == 0):
            self.window.lMessageForm.setText('<font color="red">Name is required</font>')
        else:
            return name



'''
app=QApplication(sys.argv)
mainwindow=FrameTypeApplication()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(400)
widget.setFixedHeight(300)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")
'''


