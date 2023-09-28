import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtCore import Qt

import PyQt5.QtCore

import json

import sys
import os
file = os.path.abspath("src")
sys.path.insert(0, file)



class FrameProjectTutorial(QtWidgets.QFrame):

    def __init__(self):
        super(FrameProjectTutorial,self).__init__()
        loadUi(file+"/view/ui/project_tutorial/list.ui",self)
        
        self.tableWidget.setHorizontalHeaderLabels([
            "id",
            "Name", 
            "programming_language_version", 
            "framework",
            "graphical_interface",
            "Database",
            "data_base_version",
            "orm",
            "virtual_environment",
            "Architecture",
            "cloud_server",
            "number_project_tutorial",
            "Type Application",
            "id_type_application"])
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setColumnHidden(0,True)
        self.tableWidget.setColumnHidden(2,True)
        self.tableWidget.setColumnHidden(3,True)
        self.tableWidget.setColumnHidden(4,True)
        self.tableWidget.setColumnHidden(6,True)
        self.tableWidget.setColumnHidden(7,True)
        self.tableWidget.setColumnHidden(8,True)
        self.tableWidget.setColumnHidden(10,True)
        self.tableWidget.setColumnHidden(11,True)
        self.tableWidget.setColumnHidden(13,True)


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
        uic.loadUi(file+"/view/ui/project_tutorial/form.ui", self.window)
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
                programming_language_version = self.tableWidget.item(r,2).text()
                framework = self.tableWidget.item(r,3).text()
                graphical_interface = self.tableWidget.item(r,4).text()
                data_base = self.tableWidget.item(r,5).text()
                data_base_version = self.tableWidget.item(r,6).text()
                orm = self.tableWidget.item(r,7).text()
                virtual_environment = self.tableWidget.item(r,8).text()
                architecture = self.tableWidget.item(r,9).text()
                cloud_server = self.tableWidget.item(r,10).text()
                number_project_tutorial = self.tableWidget.item(r,11).text()

            except IndexError as e:
                self.lMessageList.setText('<font color="red">Please select a data</font>')
                return
            
            self.window.leName.setText(name)
            self.window.leProgrammingLanguageVersion.setText(programming_language_version)
            self.window.leFramework.setText(framework)
            self.window.leGraphicalInterface.setText(graphical_interface)
            self.window.leDatabase.setText(data_base)
            self.window.leDataBaseVersion.setText(data_base_version)
            self.window.leOrm.setText(orm)
            self.window.leVirtualEnvironment.setText(virtual_environment)
            self.window.leArchitecture.setText(architecture)
            self.window.leCloudServer.setText(cloud_server)
            self.window.leNumberProjectTutorial.setText(number_project_tutorial)
            self.window.pbAddUpdate.setText("Update")

            self.window.pbAddUpdate.clicked.connect(lambda: self.update_data(
                id,
                self.window.leName.text(),
                self.window.leProgrammingLanguageVersion.text(),
                self.window.leFramework.text(),
                self.window.leGraphicalInterface.text(),
                self.window.leDatabase.text(),
                self.window.leDataBaseVersion.text(),
                self.window.leOrm.text(),
                self.window.leVirtualEnvironment.text(),
                self.window.leArchitecture.text(),
                self.window.leCloudServer.text(),
                self.window.leNumberProjectTutorial.text()))


        else:
            self.window.pbAddUpdate.setText("Add")
            self.window.pbAddUpdate.clicked.connect(lambda: self.add_data(
                self.window.leName.text(), 
                self.window.leProgrammingLanguageVersion.text(),
                self.window.leFramework.text(),
                self.window.leGraphicalInterface.text(),
                self.window.leDatabase.text(),
                self.window.leDataBaseVersion.text(),
                self.window.leOrm.text(),
                self.window.leVirtualEnvironment.text(),
                self.window.leArchitecture.text(),
                self.window.leCloudServer.text(),
                self.window.leNumberProjectTutorial.text(),
                id_window))
        




    def delete_window(self): 

        r = self.tableWidget.currentRow()

        try:
            id = self.tableWidget.item(r,0).text()

        except IndexError as e:
            self.lMessageList.setText('<font color="red">Please select a data</font>')
            return 

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
            data["frame_id"] = 3
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        

    
    def go_window(self): 

        self.get_data()

        r = self.tableWidget.currentRow()
        id = self.tableWidget.item(r,0).text()
        
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["window_table_id"] = id
            data["window_project_tutorial_id"] = id
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
    


    def back_window(self):
        
        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window_type_application = str_id_window['window_type_application_id']

        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["window_table_id"] = id_window_type_application
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            
            

        
        

    








    # FUNCIONES PARA REALIZAR EL CRUD 

    def get_data(self):
    
        from controller.project_tutorial.list import List
        from controller.project_tutorial.count import Count
        
        lista = List.list_data()
        count_rows = Count.count_rows()

        tablerow=0

        self.tableWidget.setRowCount(count_rows)
        
        for id, name, programming_language_version, framework, graphical_interface, data_base, data_base_version, orm, virtual_environment, architecture,cloud_server, number_project_tutorial, name_type_application, id_type_application in zip(*lista): 

            item_id = QtWidgets.QTableWidgetItem()
            item_number_project_tutorial = QtWidgets.QTableWidgetItem()
            item_id_type_application = QtWidgets.QTableWidgetItem()
                   
            item_id.setData(Qt.EditRole, id)
            item_number_project_tutorial.setData(Qt.EditRole, number_project_tutorial)
            item_id_type_application.setData(Qt.EditRole, id_type_application)

            
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item_id))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(programming_language_version))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(framework))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(graphical_interface))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(data_base))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(data_base_version))
            self.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(orm))
            self.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(virtual_environment))
            self.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(architecture))
            self.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(cloud_server))
            self.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(item_number_project_tutorial))
            self.tableWidget.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(name_type_application))
            self.tableWidget.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(item_id_type_application))

            tablerow+=1
        
        list_selection = [0]
        self.select_rows(list_selection)




    def add_data(self, 
            name,
            programming_language_version, 
            framework, 
            graphical_interface, 
            data_base,
            data_base_version, 
            orm, 
            virtual_environment, 
            architecture,
            cloud_server, 
            number_project_tutorial,
            id_type_application):  

        from controller.project_tutorial.insert import Insert

        if self.validation_add_update_window_modal(
            name,
            programming_language_version, 
            framework, 
            graphical_interface, 
            data_base,
            data_base_version, 
            orm, 
            virtual_environment, 
            architecture,
            cloud_server, 
            number_project_tutorial):
            
            Insert.add_data(
                name,
                programming_language_version, 
                framework, 
                graphical_interface, 
                data_base,
                data_base_version, 
                orm, 
                virtual_environment, 
                architecture,
                cloud_server, 
                number_project_tutorial,
                id_type_application)

            self.window.hide()
            self.lMessageList.setText('<font color="green">Data added successfully</font>')
            self.get_data()



    def update_data(self, 
            id,
            name,
            programming_language_version, 
            framework, 
            graphical_interface, 
            data_base,
            data_base_version, 
            orm, 
            virtual_environment, 
            architecture,
            cloud_server, 
            number_project_tutorial):

        from controller.project_tutorial.update import Update

        if self.validation_add_update_window_modal(
            name,
            programming_language_version, 
            framework, 
            graphical_interface, 
            data_base,
            data_base_version, 
            orm, 
            virtual_environment, 
            architecture,
            cloud_server, 
            number_project_tutorial):
            
            Update.update_data(
                id, 
                name,
                programming_language_version, 
                framework, 
                graphical_interface, 
                data_base,
                data_base_version, 
                orm, 
                virtual_environment, 
                architecture,
                cloud_server, 
                number_project_tutorial)

            self.window.hide()
            self.lMessageList.setText('<font color="green">Data updated successfully</font>')
            self.get_data()




    def delete_data(self, id):

        from controller.project_tutorial.delete import Delete
        Delete.delete_data(id)
        self.lMessageList.setText('<font color="green">Data deleted successfully</font>')
        self.get_data()














    # FUNCIONES QUE VAN A VALIDAR LAS CAJAS DE TEXTO
    def validation_add_update_window_modal(self,
            name,
            programming_language_version, 
            framework, 
            graphical_interface, 
            data_base,
            data_base_version, 
            orm, 
            virtual_environment, 
            architecture,
            cloud_server, 
            number_project_tutorial):

        if(len(name) == 0):
            self.window.lMessageForm.setText('<font color="red">Name is required</font>')
        
        elif(len(programming_language_version) == 0):
            self.window.lMessageForm.setText('<font color="red">Programming language version is required</font>')
        
        elif(len(framework) == 0):
            self.window.lMessageForm.setText('<font color="red">Framework is required</font>')
        
        elif(len(graphical_interface) == 0):
            self.window.lMessageForm.setText('<font color="red">Graphical interface is required</font>')
        
        elif(len(data_base) == 0):
            self.window.lMessageForm.setText('<font color="red">Database is required</font>')
        
        elif(len(data_base_version) == 0):
            self.window.lMessageForm.setText('<font color="red">Database version is required</font>')
        
        elif(len(orm) == 0):
            self.window.lMessageForm.setText('<font color="red">ORM is required</font>')

        elif(len(virtual_environment) == 0):
            self.window.lMessageForm.setText('<font color="red">Virtual environment is required</font>')
        
        elif(len(architecture) == 0):
            self.window.lMessageForm.setText('<font color="red">Architecture is required</font>')

        elif(len(cloud_server) == 0):
            self.window.lMessageForm.setText('<font color="red">Cloud server is required</font>')
        
        elif(len(number_project_tutorial) == 0):
            self.window.lMessageForm.setText('<font color="red">Number project tutorial is required</font>')

        else:
            return name



'''
app=QApplication(sys.argv)
mainwindow=FrameProjectTutorial()
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


