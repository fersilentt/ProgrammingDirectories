import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QLabel
from PyQt5.uic import loadUi
from PyQt5 import uic

import json
import sys
import os

file = os.path.abspath("src")
sys.path.insert(0, file)

# We import the classes of the Frames that will be displayed in this main class
from view.py.option_database_view import FrameOptionDatabase
from view.py.programming_language_view import FrameProgrammingLanguage
from view.py.type_creation_view import FrameTypeCreation
from view.py.type_application_view import FrameTypeApplication
from view.py.project_tutorial_view import FrameProjectTutorial
from view.py.part_view import FramePart

# We import the Pyqt .ui form converted to python file
from view.ui_py.main_main_ui import Ui_MainWindow


import config

root_dir = config.ROOT_DIR
data_json = config.DATA_JSON
list_databases_json = config.LIST_DATABASES_JSON
version_json = config.VERSION_JSON





class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


        # Add the title to the window
        self.setWindowTitle("Programming Directories")

        # We create the icons for the buttons

        # We obtain the path to the image and then add it to the button
        icon_main = config.ICON_MAIN
        icon_open_file_database  = config.ICON_OPEN_FILE_DATABASE
        icon_create_database  = config.ICON_CREATE_DATABASE
        icon_open_database  = config.ICON_OPEN_DATABASE
        icon_go  = config.ICON_GO
        icon_back  = config.ICON_BACK
        icon_frame  = config.ICON_FRAME
        icon_settings  = config.ICON_SETTINGS
        icon_info  = config.ICON_INFO
    
        self.ui.lMainIcon.setPixmap(QtGui.QPixmap(icon_main))
        self.ui.pbOpenFileDatabase.setIcon(QtGui.QIcon(icon_open_file_database))
        self.ui.pbCreateDatabase.setIcon(QtGui.QIcon(icon_create_database))
        self.ui.pbOpenDatabase.setIcon(QtGui.QIcon(icon_open_database))
        self.ui.pbGo.setIcon(QtGui.QIcon(icon_go))
        self.ui.pbBack.setIcon(QtGui.QIcon(icon_back))
        self.ui.pbFrameProgrammingLanguage.setIcon(QtGui.QIcon(icon_frame))
        self.ui.pbFrameTypeCreation.setIcon(QtGui.QIcon(icon_frame))
        self.ui.pbFrameTypeApplication.setIcon(QtGui.QIcon(icon_frame))
        self.ui.pbFrameProjectTutorial.setIcon(QtGui.QIcon(icon_frame))
        self.ui.pbSettings.setIcon(QtGui.QIcon(icon_settings))
        self.ui.pbInfo.setIcon(QtGui.QIcon(icon_info))
        
        

        # We load the Frames in variables
        self.frame_option_database= FrameOptionDatabase()
        self.frame_programming_language= FrameProgrammingLanguage()
        self.frame_type_creation= FrameTypeCreation()
        self.frame_type_application= FrameTypeApplication()
        self.frame_project_tutorial= FrameProjectTutorial()
        self.frame_part= FramePart()
        

        # We add the Frames to stackedWidget, so that it can be viewed
        self.ui.stackedWidget.addWidget(self.frame_option_database)
        self.ui.stackedWidget.addWidget(self.frame_programming_language)
        self.ui.stackedWidget.addWidget(self.frame_type_creation)
        self.ui.stackedWidget.addWidget(self.frame_type_application)
        self.ui.stackedWidget.addWidget(self.frame_project_tutorial)
        self.ui.stackedWidget.addWidget(self.frame_part)


        # Disable or enable menu buttons
        self.enable_disable_buttons()


        # We display a message when hovering the mouse over the button
        self.ui.pbOpenFileDatabase.setToolTip("Open file database")
        self.ui.pbCreateDatabase.setToolTip("Create database")
        self.ui.pbOpenDatabase.setToolTip("Open recent database")
        self.ui.pbGo.setToolTip("Next frame")
        self.ui.pbBack.setToolTip("Previous frame")
        self.ui.pbSettings.setToolTip("Settings")
        self.ui.pbInfo.setToolTip("About")
        self.ui.pbFrameProgrammingLanguage.setToolTip("Frame Programming Language")
        self.ui.pbFrameTypeCreation.setToolTip("Frame Type Creation")
        self.ui.pbFrameTypeApplication.setToolTip("Frame Type Application")
        self.ui.pbFrameProjectTutorial.setToolTip("Frame Project Tutorial")
      

        # Execute the functions in the main menu buttons
        self.ui.pbOpenFileDatabase.clicked.connect(self.open_file_database)
        self.ui.pbCreateDatabase.clicked.connect(self.create_file_database)
        self.ui.pbOpenDatabase.clicked.connect(self.open_database)
        self.ui.pbGo.clicked.connect(self.change_frame_go)
        self.ui.pbBack.clicked.connect(self.change_frame_back)
        self.ui.pbSettings.clicked.connect(self.settings)
        self.ui.pbInfo.clicked.connect(self.about)
        self.ui.pbFrameProgrammingLanguage.clicked.connect(lambda:self.change_frame_button(1))
        self.ui.pbFrameTypeCreation.clicked.connect(lambda:self.change_frame_button(2))
        self.ui.pbFrameTypeApplication.clicked.connect(lambda:self.change_frame_button(3))
        self.ui.pbFrameProjectTutorial.clicked.connect(lambda:self.change_frame_button(4))


        


        





    # We change the frame forwards
    def change_frame_go(self):

        # We obtain the id of the frame by opening the .json file
        with open(data_json , 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_frame_id = json.loads(json_str)
        frame_id = str_frame_id['frame_id']

        # We increment the frame id by 1 to move to the next frame according to its value according to its value
        frame_id_plus = frame_id+1

        # We perform a validation of the id of the augmented frame, so that the button will know which frame to 
        # execute
        if frame_id_plus == 2:
            # We execute the function of the first Frame which will obtain the id of the selected row in the 
            # table and in this way the next window will show the data according to the relation of that id
            if self.frame_programming_language.go_window():
                # We load the following Frame according to its position
                self.ui.stackedWidget.setCurrentIndex(2)
                # We execute this function of the Frame we loaded to insert the id of the Frame
                self.frame_type_creation.insert_frame_id()
                # We update the list of the Frame we loaded so that there is no conflict with the  information displayed 
                # when we move forward or backward with the button
                self.frame_type_creation.get_data() 
                self.enable_disable_buttons()
                self.location_information()

        elif frame_id_plus == 3:
            if self.frame_type_creation.go_window():       
                self.ui.stackedWidget.setCurrentIndex(3)
                self.frame_type_application.insert_frame_id()
                self.frame_type_application.get_data()
                self.enable_disable_buttons()
                self.location_information()
        
        elif frame_id_plus == 4:         
            if self.frame_type_application.go_window():
                self.ui.stackedWidget.setCurrentIndex(4)
                self.frame_project_tutorial.insert_frame_id()
                self.frame_project_tutorial.get_data() 
                self.enable_disable_buttons()
                self.location_information()       
        
        elif frame_id_plus == 5:
            if self.frame_project_tutorial.go_window():
                self.ui.stackedWidget.setCurrentIndex(5)
                self.frame_part.insert_frame_id()
                self.frame_part.get_data()
                self.enable_disable_buttons()
                self.location_information()









    # We change frame backward
    def change_frame_back(self):

        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_frame_id = json.loads(json_str)
        frame_id = str_frame_id['frame_id']

        # We decrease by 1 the id of the frame to move to the previous frame according to its value according to 
        # its value
        frame_id_less = frame_id-1

        if frame_id_less == 4:
            self.frame_part.back_window()
            self.ui.stackedWidget.setCurrentIndex(4)
            self.frame_project_tutorial.insert_frame_id()
            self.frame_project_tutorial.get_data() 
            self.enable_disable_buttons()
            self.location_information()
        
        elif frame_id_less == 3:
            self.frame_project_tutorial.back_window()
            self.ui.stackedWidget.setCurrentIndex(3)
            self.frame_type_application.insert_frame_id()
            self.frame_type_application.get_data()
            self.enable_disable_buttons()
            self.location_information()
 
        
        elif frame_id_less == 2:
            self.frame_type_application.back_window()
            self.ui.stackedWidget.setCurrentIndex(2)
            self.frame_type_creation.insert_frame_id()
            self.frame_type_creation.get_data()
            self.enable_disable_buttons()
            self.location_information()

        
        elif frame_id_less == 1:
            self.frame_type_creation.back_window()
            self.ui.stackedWidget.setCurrentIndex(1)
            self.frame_programming_language.insert_frame_id()
            self.frame_programming_language.get_data()
            self.enable_disable_buttons()
            self.location_information()





    # We show the information of where we are located
    def location_information(self):

        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_frame_id = json.loads(json_str)
        frame_id = str_frame_id['frame_id']    

        if frame_id == 1:
            self.ui.lInformation.setText("")

        elif frame_id == 2:
            from controller.type_creation.info import Info as class_type_creation_info
            info_name_programming_language = class_type_creation_info.list_info()
            self.ui.lInformation.setText(info_name_programming_language)
        
        elif frame_id == 3:
            from controller.type_creation.info import Info as class_type_creation_info
            from controller.type_application.info import Info as class_type_application_info
            info_name_programming_language = class_type_creation_info.list_info()
            info_name_type_creation = class_type_application_info.list_info()
            self.ui.lInformation.setText(info_name_programming_language+"/"+info_name_type_creation)
        
        elif frame_id == 4:
            from controller.type_creation.info import Info as class_type_creation_info
            from controller.type_application.info import Info as class_type_application_info
            from controller.project_tutorial.info import Info as class_project_tutorial_info
            info_name_programming_language = class_type_creation_info.list_info()
            info_name_type_creation = class_type_application_info.list_info()
            info_name_type_application = class_project_tutorial_info.list_info()
            self.ui.lInformation.setText(info_name_programming_language+"/"+info_name_type_creation+"/"+info_name_type_application)
        
        elif frame_id == 5:
            from controller.type_creation.info import Info as class_type_creation_info
            from controller.type_application.info import Info as class_type_application_info
            from controller.project_tutorial.info import Info as class_project_tutorial_info
            from controller.part.info import Info as class_part_info
            info_name_programming_language = class_type_creation_info.list_info()
            info_name_type_creation = class_type_application_info.list_info()
            info_name_type_application = class_project_tutorial_info.list_info()
            info_name_project_tutorial = class_part_info.list_info()
            self.ui.lInformation.setText(info_name_programming_language+"/"+info_name_type_creation+"/"+info_name_type_application+"/"+info_name_project_tutorial)

        
        



    # We execute the respective frame according to its id
    def change_frame_button(self, frame_id_button):

        if frame_id_button == 1:
            self.ui.stackedWidget.setCurrentIndex(1)
            self.frame_programming_language.insert_frame_id()
            self.enable_disable_buttons()
            self.location_information()
        
        elif frame_id_button == 2:
            self.ui.stackedWidget.setCurrentIndex(2)
            self.frame_type_creation.insert_frame_id()
            self.enable_disable_buttons()
            self.location_information()

        elif frame_id_button == 3:
            self.ui.stackedWidget.setCurrentIndex(3)
            self.frame_type_application.insert_frame_id()
            self.enable_disable_buttons()
            self.location_information()
        
        elif frame_id_button == 4:
            self.ui.stackedWidget.setCurrentIndex(4)
            self.frame_project_tutorial.insert_frame_id()
            self.enable_disable_buttons()
            self.location_information()








    # We enable or disable the buttons of the main window according to the frame id
    def enable_disable_buttons(self):

        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_frame_id = json.loads(json_str)
        frame_id = str_frame_id['frame_id']

        if frame_id == 0:
            self.ui.pbGo.setEnabled(False)
            self.ui.pbBack.setEnabled(False)
            self.ui.pbOpenDatabase.setEnabled(True)
            self.ui.pbInfo.setEnabled(True)
            self.ui.pbFrameProgrammingLanguage.setEnabled(False)
            self.ui.pbFrameTypeCreation.setEnabled(False)
            self.ui.pbFrameTypeApplication.setEnabled(False)
            self.ui.pbFrameProjectTutorial.setEnabled(False)
            self.ui.lMainIcon.setHidden(False)

        elif frame_id == 1:
            self.ui.pbGo.setEnabled(True)
            self.ui.pbBack.setEnabled(False)
            self.ui.pbOpenDatabase.setEnabled(False)
            self.ui.pbInfo.setEnabled(True)
            self.ui.pbFrameProgrammingLanguage.setEnabled(False)
            self.ui.pbFrameTypeCreation.setEnabled(False)
            self.ui.pbFrameTypeApplication.setEnabled(False)
            self.ui.pbFrameProjectTutorial.setEnabled(False)
            self.ui.lTitleMain.setText("Programming language")
            self.ui.lMainIcon.setHidden(True)

        elif frame_id == 2:
            self.ui.pbGo.setEnabled(True)
            self.ui.pbBack.setEnabled(True)
            self.ui.pbOpenDatabase.setEnabled(False)
            self.ui.pbInfo.setEnabled(True)
            self.ui.pbFrameProgrammingLanguage.setEnabled(True)
            self.ui.pbFrameTypeCreation.setEnabled(False)
            self.ui.pbFrameTypeApplication.setEnabled(False)
            self.ui.pbFrameProjectTutorial.setEnabled(False)
            self.ui.lTitleMain.setText("Type creation")
        
        elif frame_id == 3:
            self.ui.pbGo.setEnabled(True)
            self.ui.pbBack.setEnabled(True)
            self.ui.pbOpenDatabase.setEnabled(False)
            self.ui.pbInfo.setEnabled(True)
            self.ui.pbFrameProgrammingLanguage.setEnabled(True)
            self.ui.pbFrameTypeCreation.setEnabled(True)
            self.ui.pbFrameTypeApplication.setEnabled(False)
            self.ui.pbFrameProjectTutorial.setEnabled(False)
            self.ui.lTitleMain.setText("Type application")
        
        elif frame_id == 4:
            self.ui.pbGo.setEnabled(True)
            self.ui.pbBack.setEnabled(True)
            self.ui.pbOpenDatabase.setEnabled(False)
            self.ui.pbInfo.setEnabled(True)
            self.ui.pbFrameProgrammingLanguage.setEnabled(True)
            self.ui.pbFrameTypeCreation.setEnabled(True)
            self.ui.pbFrameTypeApplication.setEnabled(True)
            self.ui.pbFrameProjectTutorial.setEnabled(False)
            self.ui.lTitleMain.setText("Project tutorial")
        
        elif frame_id == 5:
            self.ui.pbGo.setEnabled(False)
            self.ui.pbBack.setEnabled(True)
            self.ui.pbOpenDatabase.setEnabled(False)
            self.ui.pbInfo.setEnabled(True)
            self.ui.pbFrameProgrammingLanguage.setEnabled(True)
            self.ui.pbFrameTypeCreation.setEnabled(True)
            self.ui.pbFrameTypeApplication.setEnabled(True)
            self.ui.pbFrameProjectTutorial.setEnabled(True)
            self.ui.lTitleMain.setText("Part")


    
    # Open the database file
    def open_file_database(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","SQLite Files (*.db)", options=options)
        
        if file_name:

            with open(data_json, 'r+') as f:
                data = json.load(f)
                data["route_open_database"] = file_name
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            
            with open(list_databases_json, 'r+') as f:
                data = json.load(f)
                data[file_name] = ""
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            
            # We reload the project modules
            self.reload_modules()

            #self.frame_programming_language.get_data()
            self.ui.stackedWidget.setCurrentIndex(1)
            self.frame_programming_language.get_data()
            self.frame_programming_language.insert_frame_id()
            self.enable_disable_buttons()
    




    # Create the database file
    def create_file_database(self):
        self.window = QtWidgets.QFrame()
        uic.loadUi(root_dir+"/view/ui/option_database/form.ui", self.window)
        self.window.show()

        self.window.pbCreateDatabse.clicked.connect(lambda: self.open_directory(self.window.leNameDatabase.text()))
        self.window.pbCancel.clicked.connect(self.window.hide)
    



    # Open the directory where the database is to be created
    def open_directory(self, name_database):

        if self.validation_form_database_window(name_database):

            self.window.hide()
            directory = str(QtWidgets.QFileDialog.getExistingDirectory())

            if directory:
                
                directory_database = directory+"/"+name_database+".db"
                print(directory_database)

                with open(data_json, 'r+') as f:
                    data = json.load(f)
                    data["route_open_database"] = directory_database
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                
                with open(list_databases_json, 'r+') as f:
                    data = json.load(f)
                    data[directory_database] = ""
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()

                # Execute the python file to create the database
                from model import database_open

                self.reload_modules()
                
                self.ui.stackedWidget.setCurrentIndex(1)
                self.frame_programming_language.insert_frame_id()
                self.frame_programming_language.get_data()
                self.enable_disable_buttons()

                
    


    # Open the selected database in the list of recently opened databases
    def open_database(self):

        # Validate that the function is set to True in order to advance to the next window, otherwise a new database 
        # file will have to be created
        if self.frame_option_database.on_clicked():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.frame_programming_language.get_data()
            self.frame_programming_language.insert_frame_id()
            self.enable_disable_buttons()
        



    # We open a window with project information
    def about(self):

        self.window = QtWidgets.QFrame()
        uic.loadUi(root_dir+"/view/ui/main/info.ui", self.window)
        self.window.show()

        icon_python  = config.ICON_PYTHON
        icon_qt = config.ICON_QT

        self.window.lImagePython.setPixmap(QtGui.QPixmap(icon_python))
        self.window.lImageQt.setPixmap(QtGui.QPixmap(icon_qt))

        # Get the version of the application from the .json file
        with open(version_json, 'r') as f:
            version = json.load(f)

        json_str = json.dumps(version)
        str_app_version = json.loads(json_str)
        app_version = str_app_version['app_version'] 


        # We enable external links to display the url as a link and open it in the browser.
        self.window.lRepository.setOpenExternalLinks(True)

        # Create the link to be opened
        urlLink="<a href=\"https://github.com/fersilentt/ProgrammingDirectories\">https://github.com/fersilentt/ProgrammingDirectories</a>"

        self.window.lLicence.setText("ProgrammingDirectories is distributed under \n the GNU License (GPL) version 3.")
        self.window.lConstruction.setText("ProgrammingDirectories is built with \n Python 3.8 and Qt5.")
        self.window.lDeveloped.setText("Developed by Fersilent.")
        self.window.lVersion.setText(app_version)
        self.window.lRepository.setText("Repository: "+urlLink)

        self.window.pbClose.clicked.connect(self.window.hide)
    




    def settings(self):
        self.window = QtWidgets.QFrame()
        uic.loadUi(root_dir+"/view/ui/main/settings.ui", self.window)
        self.window.show()
        #self.window.update()

        # We get the status of the updates
        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_search_updates = json.loads(json_str)
        search_updates = str_search_updates['search_updates']

        # We send the status of the updates to the checkbox
        if search_updates == "True":
            self.window.cbSearchUpdate.setChecked(True)
        else:
            self.window.cbSearchUpdate.setChecked(False)

        self.window.pbSaveSettings.clicked.connect(lambda: self.save_settings(str(self.window.cbSearchUpdate.isChecked())))
        self.window.pbSaveSettings.clicked.connect(self.window.hide)




    def save_settings(self, search_update):

        if search_update != "True":
            self.frame_option_database.clear_update_message()
            
        with open(data_json, 'r+') as f:
            data = json.load(f)
            data["search_updates"] = search_update
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 





 


    

    # Reload the CRUD modules that we imported in order to so that when the database is changed, the data will 
    # be updated automatically
    def reload_modules(self):
        import importlib

        import model.database_open

        import controller.programming_language.list
        import controller.programming_language.count
        import controller.programming_language.insert
        import controller.programming_language.update
        import controller.programming_language.delete
        import controller.programming_language.search
        import controller.programming_language.count_search

        import controller.type_creation.list
        import controller.type_creation.count
        import controller.type_creation.insert
        import controller.type_creation.update
        import controller.type_creation.delete
        import controller.type_creation.info

        import controller.type_application.list
        import controller.type_application.count
        import controller.type_application.insert
        import controller.type_application.update
        import controller.type_application.delete
        import controller.type_application.info

        import controller.project_tutorial.list
        import controller.project_tutorial.count
        import controller.project_tutorial.insert
        import controller.project_tutorial.update
        import controller.project_tutorial.delete
        import controller.project_tutorial.search
        import controller.project_tutorial.count_search
        import controller.project_tutorial.info

        importlib.reload(model.database_open)
        
        importlib.reload(controller.programming_language.list)
        importlib.reload(controller.programming_language.count)
        importlib.reload(controller.programming_language.insert)
        importlib.reload(controller.programming_language.update)
        importlib.reload(controller.programming_language.delete)
        importlib.reload(controller.programming_language.search)
        importlib.reload(controller.programming_language.count_search)

        importlib.reload(controller.type_creation.list)
        importlib.reload(controller.type_creation.count)
        importlib.reload(controller.type_creation.insert)
        importlib.reload(controller.type_creation.update)
        importlib.reload(controller.type_creation.delete)
        importlib.reload(controller.type_creation.info)

        importlib.reload(controller.type_application.list)
        importlib.reload(controller.type_application.count)
        importlib.reload(controller.type_application.insert)
        importlib.reload(controller.type_application.update)
        importlib.reload(controller.type_application.delete)
        importlib.reload(controller.type_application.info)

        importlib.reload(controller.project_tutorial.list)
        importlib.reload(controller.project_tutorial.count)
        importlib.reload(controller.project_tutorial.insert)
        importlib.reload(controller.project_tutorial.update)
        importlib.reload(controller.project_tutorial.delete)
        importlib.reload(controller.project_tutorial.search)
        importlib.reload(controller.project_tutorial.count_search)
        importlib.reload(controller.project_tutorial.info)


                
    
    # Validate that the database name is not empty
    def validation_form_database_window(self, name_database):
        if(len(name_database) == 0):
            self.window.lMessageForm.setText('<font color="red">Database name is required</font>')
        else:
            return name_database
    



    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec()

