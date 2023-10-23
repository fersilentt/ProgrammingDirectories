import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtCore import Qt

import sys
import os
file = os.path.abspath("src")
sys.path.insert(0, file)

import json
import importlib



class FrameTypeCreation(QtWidgets.QFrame):

    def __init__(self):
        super(FrameTypeCreation,self).__init__()
        loadUi(file+"/view/ui/type_creation/list.ui",self)

        self.tableWidget.setHorizontalHeaderLabels(["Id","Name", "Programming Language", "Id Programming Language"])
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        self.tableWidget.setSortingEnabled(True)
        # Ocultamos los id de la tabla
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



        







    # FUNCIONES DE LAS VENTANAS
    def add_update_window_modal(self, id_window_modal):

        self.window = QtWidgets.QMainWindow()
        uic.loadUi(file+"/view/ui/type_creation/form.ui", self.window)
        self.window.show()

        # Obtenemos el id de la ventana anterior, que es el id de de realacion con
        # esta tabla
        # Load the data into an element
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
        



    def insert_frame_id(self):
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 2
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        

        
    def go_window(self): 
        r = self.tableWidget.currentRow()

        if r == -1:
            self.lMessageList.setText('<font color="red">Please select a record</font>')
            return False
        
        else:
            id = self.tableWidget.item(r,0).text()

            with open('src/data.json', 'r+') as f:
                    data = json.load(f)
                    data["window_table_id"] = id
                    data["window_type_creation_id"] = id
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
            return True
        


    # Obtenemos el id del Frame para que la anterior ventana cargue
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
        import controller.type_creation.list
        import controller.type_creation.count
        
        lista = controller.type_creation.list.List.list_data()
        count_rows = controller.type_creation.count.Count.count_rows()

        tablerow=0

        self.tableWidget.setRowCount(count_rows)
        
        for id, name, name_programming_language, id_programming_language in zip(*lista): 

            item_id = QtWidgets.QTableWidgetItem()
            item_id_programming_language = QtWidgets.QTableWidgetItem()
            
            item_id.setData(Qt.EditRole, id)
            item_id_programming_language.setData(Qt.EditRole, id_programming_language)

            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item_id))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(name_programming_language))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(item_id_programming_language))

            tablerow+=1
        




    def add_data(self, name, id_programming_language):
        
        import controller.type_creation.insert

        if self.validation_add_update_window_modal(name):
            controller.type_creation.insert.Insert.add_data(name, id_programming_language)
            self.window.hide()
            self.lMessageList.setText('<font color="green">Data added successfully</font>')
            self.get_data()



    def update_data(self, id, name):

        import controller.type_creation.update

        if self.validation_add_update_window_modal(name):
            controller.type_creation.update.Update.update_data(id, name)
            self.window.hide()
            self.lMessageList.setText('<font color="green">Data updated successfully</font>')
            self.get_data()



    def delete_data(self, id):

        import controller.type_creation.delete

        controller.type_creation.delete.Delete.delete_data(id)
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
mainwindow=FrameTypeCreation()
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

