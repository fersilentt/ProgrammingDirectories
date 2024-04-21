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

from view.ui_py.project_tutorial_list_ui import Ui_Frame
import config

root_dir = config.ROOT_DIR
data_json = config.DATA_JSON
list_databases_json = config.LIST_DATABASES_JSON
version_json = config.VERSION_JSON



class FrameProjectTutorial(QtWidgets.QFrame):

    def __init__(self):
        super(FrameProjectTutorial,self).__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)
        
        self.ui.tableWidget.setHorizontalHeaderLabels([
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
            "Nº",
            "Type Application",
            "id_type_application"])
        self.ui.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.setColumnHidden(0,True)
        self.ui.tableWidget.setColumnHidden(2,True)
        self.ui.tableWidget.setColumnHidden(3,True)
        self.ui.tableWidget.setColumnHidden(4,True)
        self.ui.tableWidget.setColumnHidden(6,True)
        self.ui.tableWidget.setColumnHidden(7,True)
        self.ui.tableWidget.setColumnHidden(8,True)
        self.ui.tableWidget.setColumnHidden(10,True)
        #self.tableWidget.setColumnHidden(11,True)
        self.ui.tableWidget.setColumnHidden(13,True)

        icon_add  = config.ICON_ADD
        icon_update  = config.ICON_UPDATE
        icon_delete  = config.ICON_DELETE
        icon_view = config.ICON_VIEW
        
        self.ui.pbAdd.setIcon(QtGui.QIcon(icon_add))
        self.ui.pbEdit.setIcon(QtGui.QIcon(icon_update))
        self.ui.pbDelete.setIcon(QtGui.QIcon(icon_delete))
        self.ui.pbView.setIcon(QtGui.QIcon(icon_view))

        self.ui.pbAdd.clicked.connect(lambda: self.add_update_window_modal(0))
        self.ui.pbEdit.clicked.connect(lambda: self.add_update_window_modal(1))
        self.ui.pbDelete.clicked.connect(self.delete_window)
        self.ui.pbView.clicked.connect(self.view_window_modal)
        self.ui.leSearch.textChanged.connect(self.scan_q_line_edit)






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
                uic.loadUi(root_dir+"/view/ui/project_tutorial/form.ui", self.window)
                self.window.show()

                id = self.ui.tableWidget.item(r,0).text()
                name = self.ui.tableWidget.item(r,1).text()
                programming_language_version = self.ui.tableWidget.item(r,2).text()
                framework = self.ui.tableWidget.item(r,3).text()
                graphical_interface = self.ui.tableWidget.item(r,4).text()
                data_base = self.ui.tableWidget.item(r,5).text()
                data_base_version = self.ui.tableWidget.item(r,6).text()
                orm = self.ui.tableWidget.item(r,7).text()
                virtual_environment = self.ui.tableWidget.item(r,8).text()
                architecture = self.ui.tableWidget.item(r,9).text()
                cloud_server = self.ui.tableWidget.item(r,10).text()
                number_project_tutorial = self.ui.tableWidget.item(r,11).text()

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

            self.window = QtWidgets.QFrame()
            uic.loadUi(root_dir+"/view/ui/project_tutorial/form.ui", self.window)
            self.window.show()
            
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

        r = self.ui.tableWidget.currentRow()

        if r == -1:
            self.ui.lMessageList.setText('<font color="red">Please select a record</font>')
            return False
        else:
            id = self.ui.tableWidget.item(r,0).text()

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







    def view_window_modal(self):

        r = self.ui.tableWidget.currentRow()

        if r == -1:
            self.ui.lMessageList.setText('<font color="red">Please select a record</font>')
        else:
            self.window = QtWidgets.QFrame()
            uic.loadUi(root_dir+"/view/ui/project_tutorial/view.ui", self.window)
            self.window.show()

            self.window.pbClose.clicked.connect(self.window.hide)

            self.window.lTextName.setStyleSheet("font-weight: bold")
            self.window.lTextProgrammingLanguageVersion.setStyleSheet("font-weight: bold")
            self.window.lTextFramework.setStyleSheet("font-weight: bold")
            self.window.lTextGraphicalInterface.setStyleSheet("font-weight: bold")
            self.window.lTextDatabase.setStyleSheet("font-weight: bold")
            self.window.lTextDataBaseVersion.setStyleSheet("font-weight: bold")
            self.window.lTextOrm.setStyleSheet("font-weight: bold")
            self.window.lTextVirtualEnvironment.setStyleSheet("font-weight: bold")
            self.window.lTextArchitecture.setStyleSheet("font-weight: bold")
            self.window.lTextCloudServer.setStyleSheet("font-weight: bold")
            self.window.lTextNumberProjectTutorial.setStyleSheet("font-weight: bold")

            name = self.ui.tableWidget.item(r,1).text()
            programming_language_version = self.ui.tableWidget.item(r,2).text()
            framework = self.ui.tableWidget.item(r,3).text()
            graphical_interface = self.ui.tableWidget.item(r,4).text()
            data_base = self.ui.tableWidget.item(r,5).text()
            data_base_version = self.ui.tableWidget.item(r,6).text()
            orm = self.ui.tableWidget.item(r,7).text()
            virtual_environment = self.ui.tableWidget.item(r,8).text()
            architecture = self.ui.tableWidget.item(r,9).text()
            cloud_server = self.ui.tableWidget.item(r,10).text()
            number_project_tutorial = self.ui.tableWidget.item(r,11).text()

            self.window.lName.setText(name)
            self.window.lProgrammingLanguageVersion.setText(programming_language_version)
            self.window.lFramework.setText(framework)
            self.window.lGraphicalInterface.setText(graphical_interface)
            self.window.lDatabase.setText(data_base)
            self.window.lDataBaseVersion.setText(data_base_version)
            self.window.lOrm.setText(orm)
            self.window.lVirtualEnvironment.setText(virtual_environment)
            self.window.lArchitecture.setText(architecture)
            self.window.lCloudServer.setText(cloud_server)
            self.window.lNumberProjectTutorial.setText(number_project_tutorial)




    def insert_frame_id(self):
        with open(data_json, 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 4
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
                data["window_project_tutorial_id"] = id
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate() 
            return True
    


    def back_window(self):
        
        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window_type_creation = str_id_window['window_type_creation_id']

        with open(data_json, 'r+') as f:
            data = json.load(f)
            data["window_table_id"] = id_window_type_creation
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

            
            

        
        

    


    def get_data(self):
    
        from controller.project_tutorial.list import List
        from controller.project_tutorial.count import Count
        
        lista = List.list_data()
        count_rows = Count.count_rows()

        tablerow=0

        self.ui.tableWidget.setRowCount(count_rows)
        
        for id, name, programming_language_version, framework, graphical_interface, data_base, data_base_version, orm, virtual_environment, architecture,cloud_server, number_project_tutorial, name_type_application, id_type_application in zip(*lista): 

            item_id = QtWidgets.QTableWidgetItem()
            item_number_project_tutorial = QtWidgets.QTableWidgetItem()
            item_id_type_application = QtWidgets.QTableWidgetItem()
                   
            item_id.setData(Qt.EditRole, id)
            item_number_project_tutorial.setData(Qt.EditRole, number_project_tutorial)
            item_id_type_application.setData(Qt.EditRole, id_type_application)

            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item_id))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(programming_language_version))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(framework))
            self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(graphical_interface))
            self.ui.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(data_base))
            self.ui.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(data_base_version))
            self.ui.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(orm))
            self.ui.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(virtual_environment))
            self.ui.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(architecture))
            self.ui.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(cloud_server))
            self.ui.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(item_number_project_tutorial))
            self.ui.tableWidget.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(name_type_application))
            self.ui.tableWidget.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(item_id_type_application))

            tablerow+=1
        




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

            from controller.project_tutorial.insert import Insert
            
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
            self.ui.lMessageList.setText('<font color="green">Data added successfully</font>')
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

            from controller.project_tutorial.update import Update
            
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
            self.ui.lMessageList.setText('<font color="green">Data updated successfully</font>')
            self.get_data()




    def delete_data(self, id):

        from controller.project_tutorial.delete import Delete
        Delete.delete_data(id)
        self.ui.lMessageList.setText('<font color="green">Data deleted successfully</font>')
        self.get_data()

    
    
    def search_data(self, data):

        from controller.project_tutorial.search import Search
        from controller.project_tutorial.count_search import CountSearch
        
        list_search = Search.search_data(data)
        count_rows_search = CountSearch.count_rows_search(data)
        
        tablerow=0
        self.ui.tableWidget.setRowCount(count_rows_search)
        
        for id, name, programming_language_version, framework, graphical_interface, data_base, data_base_version, orm, virtual_environment, architecture,cloud_server, number_project_tutorial, name_type_application, id_type_application in zip(*list_search): 

            item_id = QtWidgets.QTableWidgetItem()
            item_number_project_tutorial = QtWidgets.QTableWidgetItem()
            item_id_type_application = QtWidgets.QTableWidgetItem()
                   
            item_id.setData(Qt.EditRole, id)
            item_number_project_tutorial.setData(Qt.EditRole, number_project_tutorial)
            item_id_type_application.setData(Qt.EditRole, id_type_application)

            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item_id))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(programming_language_version))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(framework))
            self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(graphical_interface))
            self.ui.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(data_base))
            self.ui.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(data_base_version))
            self.ui.tableWidget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(orm))
            self.ui.tableWidget.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(virtual_environment))
            self.ui.tableWidget.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(architecture))
            self.ui.tableWidget.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(cloud_server))
            self.ui.tableWidget.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(item_number_project_tutorial))
            self.ui.tableWidget.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(name_type_application))
            self.ui.tableWidget.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(item_id_type_application))

            tablerow+=1
        
    



    def scan_q_line_edit(self, event):

        if event:
            self.search_data(event)
        else:
            self.get_data()






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


