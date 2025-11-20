from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtCore import Qt

import json

from view.ui_py.type_application_list_ui import Ui_Frame
import config

root_dir = config.ROOT_DIR
data_json = config.DATA_JSON
list_databases_json = config.LIST_DATABASES_JSON
version_json = config.VERSION_JSON
dark_mode = config.DARK_MODE

title_add = config.TITLE_ADD
title_update = config.TITLE_UPDATE
title_delete = config.TITLE_DELETE


class FrameTypeApplication(QtWidgets.QFrame):

    def __init__(self):
        super(FrameTypeApplication,self).__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.ui.tableWidget.setHorizontalHeaderLabels(["Id","Name", "Type Creation", "Id Type Creation"])
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.setColumnHidden(0,True)
        self.ui.tableWidget.setColumnHidden(3,True)
        self.ui.tableWidget.verticalHeader().setVisible(False)

        icon_add  = config.ICON_ADD
        icon_update  = config.ICON_UPDATE
        icon_delete  = config.ICON_DELETE
        
        self.ui.pbAdd.setIcon(QtGui.QIcon(icon_add))
        self.ui.pbEdit.setIcon(QtGui.QIcon(icon_update))
        self.ui.pbDelete.setIcon(QtGui.QIcon(icon_delete))
        
        self.ui.pbAdd.clicked.connect(lambda: self.add_update_window_modal(0))
        self.ui.pbEdit.clicked.connect(lambda: self.add_update_window_modal(1))
        self.ui.pbDelete.clicked.connect(self.delete_window)








    def add_update_window_modal(self, id_window_modal):

        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window = str_id_window['window_table_id']
        
        if id_window_modal != 0:

            r = self.ui.tableWidget.currentRow()

            if r == -1:
                self.ui.lMessageList.setText('<font color="red">Please select a record</font>')
            else:
                self.window = QtWidgets.QFrame()
                uic.loadUi(root_dir+"/view/ui/type_application/form.ui", self.window)
                self.window.show()

                self.window.setWindowTitle(title_update)

                self.load_stylesheet_frame(dark_mode)

                id = self.ui.tableWidget.item(r,0).text()
                name = self.ui.tableWidget.item(r,1).text()

                self.window.leName.setText(name)
                self.window.pbAddUpdate.setText("Update")
                self.window.pbAddUpdate.clicked.connect(lambda: self.update_data(id,self.window.leName.text()))

        else:
            self.window = QtWidgets.QFrame()
            uic.loadUi(root_dir+"/view/ui/type_application/form.ui", self.window)
            self.window.show()

            self.window.setWindowTitle(title_add)

            self.load_stylesheet_frame(dark_mode)

            self.window.pbAddUpdate.setText("Add")
            self.window.pbAddUpdate.clicked.connect(lambda: self.add_data(self.window.leName.text(), id_window))
        




    def delete_window(self): 

        r = self.ui.tableWidget.currentRow()

        if r == -1:
            self.ui.pbAddlMessageList.setText('<font color="red">Please select a record</font>')
            return False
        else:
            id = self.ui.tableWidget.item(r,0).text()

            dlg = QMessageBox(self)
            dlg.setWindowTitle(title_delete)
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
        with open(data_json, 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 3
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 


    
    def go_window(self): 

        r = self.ui.tableWidget.currentRow()

        if r == -1:
            self.ui.lMessageList.setText('<font color="red">Please select a record</font>')
            return False
        
        else:
            id = self.ui.tableWidget.item(r,0).text()

            with open(data_json, 'r+') as f:
                data = json.load(f)
                data["window_table_id"] = id
                data["window_type_application_id"] = id
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            return True
            
        


            
        
    def back_window(self):

        # Open the id of the previous window
        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window_programming_language = str_id_window['window_programming_language_id']

        # We store the id of the specific window in the id of the main window and then we get the data of that 
        # specific id
        with open(data_json, 'r+') as f:
            data = json.load(f)
            data["window_table_id"] = id_window_programming_language
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        

    



    def get_data(self):
    
        from controller.type_application.list import List
        from controller.type_application.count import Count
        
        lista = List.list_data()
        count_rows = Count.count_rows()

        tablerow=0

        self.ui.tableWidget.setRowCount(count_rows)
        
        for id, name, name_type_creation, id_type_creation in zip(*lista): 

            item_id = QtWidgets.QTableWidgetItem()
            item_id_type_creation = QtWidgets.QTableWidgetItem()
            
            item_id.setData(Qt.EditRole, id)
            item_id_type_creation.setData(Qt.EditRole, id_type_creation)

            
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item_id))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(name_type_creation))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(item_id_type_creation))

            tablerow+=1



    def add_data(self, name, id_type_creation):  

        if self.validation_add_update_window_modal(name):
            from controller.type_application.insert import Insert
            Insert.add_data(name, id_type_creation)
            self.window.hide()
            self.ui.lMessageList.setText('<font color="green">Data added successfully</font>')
            self.get_data()



    def update_data(self, id, name):

        if self.validation_add_update_window_modal(name):
            from controller.type_application.update import Update
            Update.update_data(id, name)
            self.window.hide()
            self.ui.lMessageList.setText('<font color="green">Data updated successfully</font>')
            self.get_data()



    def delete_data(self, id):

        from controller.type_application.delete import Delete
        Delete.delete_data(id)
        self.ui.lMessageList.setText('<font color="green">Data deleted successfully</font>')
        self.get_data()


    def validation_add_update_window_modal(self, name):
        if(len(name) == 0):
            self.window.lMessageForm.setText('<font color="red">Name is required</font>')
        else:
            return name
        

    def load_stylesheet_frame(self, path):
        try:
            print("Cargando CSS desde:", path)
            with open(path, "r") as file:
                stylesheet = file.read()
                self.window.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print("Archivo CSS no encontrado:", path)
        except Exception as e:
            print("Error al cargar el CSS:", str(e))






