import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QAbstractItemView
from PyQt5.uic import loadUi
from PyQt5.QtCore import QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# We import this module to validate the version of the installed application with the latest version of the 
# application uploaded to GitHub, using the GitHub api
import requests
import json
import sys
import os

from view.ui_py.option_database_main_ui import Ui_Frame
import config

data_json = config.DATA_JSON
list_databases_json = config.LIST_DATABASES_JSON
version_json = config.VERSION_JSON

class FrameOptionDatabase(QtWidgets.QFrame):

    def __init__(self):
        super(FrameOptionDatabase,self).__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        icon_delete  = config.ICON_DELETE
        self.ui.pbDeleteRecentDatabase.setIcon(QtGui.QIcon(icon_delete))

        # We edit the field of our json object to store the id of the Frame so that we can to move with the 
        # button from the main menu
        with open(data_json, 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 0
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        self.ui.pbDeleteRecentDatabase.clicked.connect(self.delete_recent_database)
        
        self.model = QStandardItemModel()
        self.ui.lvListDatabases.setModel(self.model)
        #self.lvListDatabases.setObjectName("listView-1")
        self.ui.lvListDatabases.setModelColumn(1)

        self.get_data()

        self.checking_application_updates()
    


    # We get the list of recently opened databases
    def get_data(self):

        with open(list_databases_json, 'r') as f:
            data = json.load(f)
            #print(data)
        
        #for i in data:
        #    self.model.appendRow(QStandardItem(data[i]))
        
        for i in data:
            self.model.appendRow(QStandardItem(i))
        
        # Select the first item of the ListView
        ix = self.model.index(0, 0)
        sm = self.ui.lvListDatabases.selectionModel()
        sm.select(ix, QtCore.QItemSelectionModel.Select)




    # We get the selected database in the ListView and insert it in the path to open the database
    def on_clicked(self):
        
        with open(list_databases_json, 'r') as f:
            data = json.load(f)

        # We convert the json object to string to perform validation
        data_str = str(data)
    
        if data_str == "{}":
            self.ui.lMessageOptionDatabase.setText('<font color="red">No recent database exists</font>')
            return False
        else: 
            # We obtain the selected item in the ListView
            route_database = self.ui.lvListDatabases.currentIndex().data()
        
            with open(data_json, 'r+') as f:
                data = json.load(f)
                data["route_open_database"] = route_database
                f.seek(0)        
                json.dump(data, f, indent=4)
                f.truncate() 
            
            return True
    



    # Delete the selected database in the ListView
    def delete_recent_database(self):

        with open(list_databases_json, 'r') as f:
            data = json.load(f)

        # We convert the json object to string to perform validation
        data_str = str(data)
    
        if data_str == "{}":
            self.ui.lMessageOptionDatabase.setText('<font color="red">No recent database exists</font>')
            return False
        else: 

            route_database = self.ui.lvListDatabases.currentIndex().data()

            # Delete the selected database in the json object
            with open(list_databases_json, 'r+') as f:
                data = json.load(f)
                del data[route_database]
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

            # Perform a ListView cleanup by inserting an empty array
            self.model = QStandardItemModel()
            self.ui.lvListDatabases.setModel(self.model)
                
            values = []

            for i in values:
                self.model.appendRow(QStandardItem(i))

            self.get_data()

        
    





    # Validate the version of the installed application with the latest version of the application uploaded to GitHub, 
    # using the GitHub api
    def checking_application_updates(self):

        # We check that the search for updates is enabled
        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_search_updates = json.loads(json_str)
        search_updates = str_search_updates['search_updates']

        if search_updates == "True":
            # The repository must be without the "pre-release" option, in order to be detected by GitHub api and get the latest 
            # version of the project
            response_version_github = requests.get("https://api.github.com/repos/fersilentt/ProgrammingDirectories/releases/latest")
            app_version_github = response_version_github.json()["name"]
        

            # We obtain the current version of the application
            with open(version_json, 'r') as f:
                data = json.load(f)

            json_str = json.dumps(data)
            str_app_version = json.loads(json_str)
            app_version = str_app_version['app_version']

            if app_version != app_version_github:
                self.ui.lMessageOptionDatabase.setOpenExternalLinks(True)
                message = "<font color='orange'>Is there a new version of the application, would you like to update it? </font>"
                urlLink = "<a href=\"https://github.com/fersilentt/ProgrammingDirectories/releases/latest\"> Yes</a>"
                update_message = message+urlLink
                self.ui.lMessageOptionDatabase.setText(update_message)



    def clear_update_message(self): 
        self.ui.lMessageOptionDatabase.setText('')

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

