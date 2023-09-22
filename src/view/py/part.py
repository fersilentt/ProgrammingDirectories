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



class FramePart(QtWidgets.QFrame):

    def __init__(self):
        super(FramePart,self).__init__()
        loadUi(file+"/view/ui/part/list.ui",self)

        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 4
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 

        self.tableWidget.setHorizontalHeaderLabels([
            "id",
            "Name", 
            "repository", 
            "youtube_video", 
            "id_part", 
            "Project Tutorial", 
            "id_project_tutorial"])
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)


        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setColumnHidden(0,True)
        self.tableWidget.setColumnHidden(6,True)


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
        uic.loadUi(file+"/view/ui/part/form.ui", self.window)
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
                repository = self.tableWidget.item(r,2).text()
                youtube_video = self.tableWidget.item(r,3).text()
                id_part = self.tableWidget.item(r,4).text()
            

            except IndexError as e:
                self.lMessageList.setText('<font color="red">Please select a data</font>')
                return
            
            self.window.leName.setText(name)
            self.window.leRepository.setText(repository)
            self.window.leYoutubeVideo.setText(youtube_video)
            self.window.lePartId.setText(id_part)
            self.window.pbAddUpdate.setText("Update")
            self.window.pbAddUpdate.clicked.connect(lambda: self.update_data(
                id,
                self.window.leName.text(),
                self.window.leRepository.text(), 
                self.window.leYoutubeVideo.text(),
                self.window.lePartId.text()))


        else:
            self.window.pbAddUpdate.setText("Add")
            self.window.pbAddUpdate.clicked.connect(lambda: self.add_data(
                self.window.leName.text(),
                self.window.leRepository.text(), 
                self.window.leYoutubeVideo.text(),
                self.window.lePartId.text(),
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
        



    '''
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
    '''    
    


    def back_window(self):

        # Abrimos el id de la ventana anterior
        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window_project_tutorial = str_id_window['window_project_tutorial_id']

        # Guardamos el id de la ventana especifica en el id de la ventana principal
        # para despues obtener los datos de ese id especifico
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["window_table_id"] = id_window_project_tutorial
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            

   

    








    # FUNCIONES PARA REALIZAR EL CRUD 

    def get_data(self):
    
        from controller.part.list import List
        from controller.part.count import Count
        
        lista = List.list_data()
        count_rows = Count.count_rows()

        tablerow=0

        self.tableWidget.setRowCount(count_rows)
        
        for id, name, repository, youtube_video, id_part, name_project_tutorial, id_project_tutorial  in zip(*lista): 

            item_id = QtWidgets.QTableWidgetItem()
            item_id_part = QtWidgets.QTableWidgetItem()
            item_id_project_tutorial = QtWidgets.QTableWidgetItem()
            
            item_id.setData(Qt.EditRole, id)
            item_id_part.setData(Qt.EditRole, id_part)
            item_id_project_tutorial.setData(Qt.EditRole, id_project_tutorial)

            
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item_id))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(repository))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(youtube_video))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(item_id_part))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(name_project_tutorial))
            self.tableWidget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(item_id_project_tutorial))

            tablerow+=1




    def add_data(self, 
        name,
        repository,
        youtube_video,
        id_part,
        id_project_tutorial):  

        from controller.part.insert import Insert

        if self.validation_add_update_window_modal(
            name, 
            repository, 
            youtube_video, 
            id_part):

            Insert.add_data(
                name, 
                repository, 
                youtube_video, 
                id_part, 
                id_project_tutorial)

            self.window.hide()
            self.lMessageList.setText('<font color="green">Data added successfully</font>')
            self.get_data()




    def update_data(self, 
        id, 
        name,
        repository, 
        youtube_video, 
        id_part):

        from controller.part.update import Update

        if self.validation_add_update_window_modal(
            name,
            repository, 
            youtube_video, 
            id_part):

            Update.update_data(
                id, 
                name, 
                repository, 
                youtube_video, 
                id_part)

            self.window.hide()
            self.lMessageList.setText('<font color="green">Data updated successfully</font>')
            self.get_data()



    def delete_data(self, id):

        from controller.part.delete import Delete
        Delete.delete_data(id)
        self.lMessageList.setText('<font color="green">Data deleted successfully</font>')
        self.get_data()














    # FUNCIONES QUE VAN A VALIDAR LAS CAJAS DE TEXTO
    def validation_add_update_window_modal(self, 
        name,
        repository,
        youtube_video,
        id_part):

        if(len(name) == 0):
            self.window.lMessageForm.setText('<font color="red">Name is required</font>')
        
        elif(len(repository) == 0):
            self.window.lMessageForm.setText('<font color="red">Repository is required</font>')
        
        elif(len(youtube_video) == 0):
            self.window.lMessageForm.setText('<font color="red">Youtube video is required</font>')
        
        elif(len(id_part) == 0):
            self.window.lMessageForm.setText('<font color="red">Part is required</font>')

        else:
            return name



'''
app=QApplication(sys.argv)
mainwindow=FramePart()
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

