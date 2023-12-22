import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QAbstractItemView
from PyQt5.uic import loadUi
from PyQt5 import uic

# We added this library to be able to display integers in our table using Roles table using Roles
from PyQt5.QtCore import Qt

# We import this module to work with json objects
import json



# We import this module to be able to inert the path, where the CRUD files are located, in this way 
# we can import our files independently of any folder where they are located
import sys

# We import this module to get an absolute path to our project, in order to import the images for 
# our buttons
import os

# os.path.abspath("src") = we get the absolute path of the project and then we import the files
file = os.path.abspath("src")

# We add the absolute path of our project, so that it recognizes the path of importing of the files 
# that make the CRUD
sys.path.insert(0, file)


import importlib









class FrameProgrammingLanguage(QtWidgets.QFrame):

    def __init__(self):
        super(FrameProgrammingLanguage,self).__init__()
        # We import the .ui file by calling the absolute path we have previously created
        loadUi(file+"/view/ui/programming_language/list.ui",self)
        
        r = self.tableWidget.currentRow()
        id = self.tableWidget.item(r,0)

        if id is not None and id.text() != '':
            print("Si hay dato")
            with open('src/data.json', 'r+') as f:
                data = json.load(f)
                data["status_table_widget"] = 1
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        else:
            print("No hay dato")
            with open('src/data.json', 'r+') as f:
                data = json.load(f)
                data["status_table_widget"] = 0
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

        # Here we set the size that each column is going to have according to its position, but in 
        # this case we comment it so that it remains in its original form
        #self.tableWidget.setColumnWidth(0, 250)
        #self.tableWidget.setColumnWidth(1, 100)
        #self.tableWidget.setColumnWidth(2, 350)
        
        #  We send the names of the headers that our table will have, replacing the headers in case it 
        # already has them
        self.tableWidget.setHorizontalHeaderLabels(["Id","Name"])

        # We add this to be able to select the whole row instead of selecting cell by cell
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        #self.tableWidget.verticalHeader().setVisible(False)
        # Sort in ascending and descending order with one click all the columns of the table
        self.tableWidget.setSortingEnabled(True)

        # We hide column 0 of the table
        self.tableWidget.setColumnHidden(0,True)



        # We create the icons for the buttons

        # We obtain the path to the image and then add it to the button
        icon_add  = QtGui.QPixmap(os.path.abspath("src/static/add.svg"))
        icon_update  = QtGui.QPixmap(os.path.abspath("src/static/update.svg"))
        icon_delete  = QtGui.QPixmap(os.path.abspath("src/static/delete.svg"))
        
        # Add the image to the button
        self.pbAdd.setIcon(QtGui.QIcon(icon_add))
        self.pbEdit.setIcon(QtGui.QIcon(icon_update))
        self.pbDelete.setIcon(QtGui.QIcon(icon_delete))
        #self.pbAdd.setIconSize(QtCore.QSize(200,200))


        # We execute the CRUD functions
        self.pbAdd.clicked.connect(lambda: self.add_update_window_modal(0))
        self.pbEdit.clicked.connect(lambda: self.add_update_window_modal(1))
        self.pbDelete.clicked.connect(self.delete_window)
        self.leSearch.textChanged.connect(self.scan_q_line_edit)

        # We perform a cleaning of the label that acts as a message
        self.lMessageList.setText("")

 


        







    # We create the window to add and update the data
    def add_update_window_modal(self, id_window_modal):

        # Validate if the form id is 0 will be to insert, 1 will be to update
        if id_window_modal != 0:

            # We obtain the data of the selected row
            r = self.tableWidget.currentRow()

            if r == -1:
                self.lMessageList.setText('<font color="red">Please select a record</font>')
            else:
                # We run the modal window and open it
                self.window = QtWidgets.QMainWindow()
                uic.loadUi(file+"/view/ui/programming_language/form.ui", self.window)
                self.window.show()

                # Let's get the row data according to their position
                id = self.tableWidget.item(r,0).text()
                name = self.tableWidget.item(r,1).text()

                # We send the data to the text boxes
                self.window.leName.setText(name)

                # We change the name of the button
                self.window.pbAddUpdate.setText("Update")
                
                # We send the data to update
                self.window.pbAddUpdate.clicked.connect(lambda: self.update_data(id, self.window.leName.text()))


        else:
            self.window = QtWidgets.QMainWindow()
            uic.loadUi(file+"/view/ui/programming_language/form.ui", self.window)
            self.window.show()

            self.window.pbAddUpdate.setText("Add")
            self.window.pbAddUpdate.clicked.connect(lambda: self.add_data(self.window.leName.text()))




    # We create a window to delete the data
    def delete_window(self): 

        r = self.tableWidget.currentRow()
        id = self.tableWidget.item(r,0).text()

        # We display an information message to indicate whether or not you want to delete the data
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
    # Seleccionamos la fila que le pasemos, para que se preseleccione al cargar la lista de datos
    def select_rows(self, selection: list):
        for i in selection:
            self.tableWidget.selectRow(i)
    '''



    # Insert the id of the Frame, so that it can be identified
    def insert_frame_id(self):
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        



    # We obtain the id of the table so that the following window will load
    def go_window(self):
        
        r = self.tableWidget.currentRow()

        if r == -1:
            self.lMessageList.setText('<font color="red">Please select a record</font>')
            return False
        else: 
            id = self.tableWidget.item(r,0).text()

            # We edit the fields of our json object to store the id of the table to be retrieved
            with open('src/data.json', 'r+') as f:
                data = json.load(f)
                # Here we edit the value of the "window_table_id" field and replace it with the id of the table
                data["window_table_id"] = id
                data["window_programming_language_id"] = id
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate() 
            return True
    

    
    
        


   






    # FUNCTIONS TO PERFORM THE CRUD

    # We obtain the list of data
    def get_data(self):
        import controller.programming_language.list
        import controller.programming_language.count

        #importlib.reload(controller.programming_language.list)
        #importlib.reload(controller.programming_language.count)
        #self.reload_modules()
    
        lista = controller.programming_language.list.List.list_data()
        count_rows = controller.programming_language.count.Count.count_rows()

        # We set to 0 the value that increments each row in our table
        tablerow=0

        # We set the number of records we are going to obtain from our query
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(count_rows)
        

        # We fill the data obtained from the query into the table
        for id,name in zip(*lista): 

            # Creamos este codigo para mostrar enteros en nuestra tabla usando Roles si no usamos 
            # este codigo no podremos ver los numeros en nuestra tabla
            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, id)
            
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))

            # We increase the row of our table by 1
            tablerow+=1

        '''
        # We send the position of the row that we want to be preset
        list_selection = [0]
        self.select_rows(list_selection)
        '''
    


    # We obtain the list of filtered data
    def get_data_general_search(self):
        import controller.programming_language.list
        import controller.programming_language.count

        lista = controller.programming_language.list.List.list_data()
        count_rows = controller.programming_language.count.Count.count_rows()

        tablerow=0

        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(count_rows)
        
        for id,name in zip(*lista): 

            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, id)
            
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))

            tablerow+=1





    # We insert data
    def add_data(self, name):  

        import controller.programming_language.insert
        #self.reload_modules()

        # We call the validation function to check that the text boxes are not empty
        if self.validation_add_update_window(name):

            # we insert data
            controller.programming_language.insert.Insert.add_data(name)
            # We hide the window
            self.window.hide()
            # We display a message with a color
            self.lMessageList.setText('<font color="green">Data added successfully</font>')
            # We update the data list
            self.get_data()



    # We update data
    def update_data(self, id, name):

        import controller.programming_language.update

        if self.validation_add_update_window(name):

            controller.programming_language.update.Update.update_data(id, name)
            self.window.hide()
            self.lMessageList.setText('<font color="green">Data updated successfully</font>')
            self.get_data()





    # We delete data
    def delete_data(self, id):

        import controller.programming_language.delete

        controller.programming_language.delete.Delete.delete_data(id)
        self.lMessageList.setText('<font color="green">Data deleted successfully</font>')
        self.get_data()
    



    # We search data
    def search_data(self, data):

        import controller.programming_language.search
        import controller.programming_language.count_search
        
        list_search = controller.programming_language.search.Search.search_data(data)
        count_rows_search = controller.programming_language.count_search.CountSearch.count_rows_search(data)

        tablerow=0
        self.tableWidget.setRowCount(count_rows_search)
        
        for id,name in zip(*list_search): 

            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, id)
            
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))

            tablerow+=1

    




    # We obtain the value we enter in the text box in a fast way

    # event = contains the text of the line edit, we could also test
    def scan_q_line_edit(self, event):
        
        # We validate that the data entered in the text box is searched in the database
        if event:
            self.search_data(event)
        # Otherwise, the entire list of data will be displayed
        else:
            self.get_data_general_search()
            



    
    









    # FUNCTIONS THAT WILL VALIDATE TEXT BOXES


    # We validate that the text boxes are not empty
    def validation_add_update_window(self, name):

        # len = method for obtaining the length of an element
        # == 0 = here we indicate that the length of the entered value is equal to 0
        if(len(name) == 0):
            self.window.lMessageForm.setText('<font color="red">Name is required</font>')

        # Otherwise we return the values of the data
        else:
            return name


'''
app=QApplication(sys.argv)
mainwindow=FrameProgrammingLanguage()
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
