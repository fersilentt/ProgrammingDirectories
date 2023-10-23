import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import uic

import json

import sys
import os
file = os.path.abspath("src")
sys.path.insert(0, file)

# Importamos las clases de los Frames que se van a mostrar en esta clase principal
from view.py.option_database import FrameOptionDatabase
from view.py.programming_language import FrameProgrammingLanguage
from view.py.type_creation import FrameTypeCreation
from view.py.type_application import FrameTypeApplication
from view.py.project_tutorial import FrameProjectTutorial
from view.py.part import FramePart







class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi(file+"/view/ui/main/main.ui",self)

         # Creamos los iconos para los botones
        icon_open_database  = QtGui.QPixmap(os.path.abspath("src/static/open_database.svg"))
        icon_create_database  = QtGui.QPixmap(os.path.abspath("src/static/create_database.svg"))
        icon_go  = QtGui.QPixmap(os.path.abspath("src/static/go.svg"))
        icon_back  = QtGui.QPixmap(os.path.abspath("src/static/back.svg"))
        icon_frame  = QtGui.QPixmap(os.path.abspath("src/static/frame.svg"))
        icon_info  = QtGui.QPixmap(os.path.abspath("src/static/info.svg"))
    
        self.pbOpenDatabase.setIcon(QtGui.QIcon(icon_open_database))
        self.pbCreateDatabase.setIcon(QtGui.QIcon(icon_create_database))
        self.pbGo.setIcon(QtGui.QIcon(icon_go))
        self.pbBack.setIcon(QtGui.QIcon(icon_back))
        self.pbFrameProgrammingLanguage.setIcon(QtGui.QIcon(icon_frame))
        self.pbFrameTypeCreation.setIcon(QtGui.QIcon(icon_frame))
        self.pbFrameTypeApplication.setIcon(QtGui.QIcon(icon_frame))
        self.pbFrameProjectTutorial.setIcon(QtGui.QIcon(icon_frame))
        self.pbInfo.setIcon(QtGui.QIcon(icon_info))
        

        # Cargamos los Frames en variables
        self.frame_option_database= FrameOptionDatabase()
        self.frame_programming_language= FrameProgrammingLanguage()
        self.frame_type_creation= FrameTypeCreation()
        self.frame_type_application= FrameTypeApplication()
        self.frame_project_tutorial= FrameProjectTutorial()
        self.frame_part= FramePart()
        

        # Agregamos los Frames a stackedWidget, para que pueda visualizarse
        self.stackedWidget.addWidget(self.frame_option_database)
        self.stackedWidget.addWidget(self.frame_programming_language)
        self.stackedWidget.addWidget(self.frame_type_creation)
        self.stackedWidget.addWidget(self.frame_type_application)
        self.stackedWidget.addWidget(self.frame_project_tutorial)
        self.stackedWidget.addWidget(self.frame_part)


        # Deshabilitamos o habilitamos los botones del menu
        self.enable_disable_buttons()


        # Mostramos un mensaje al pasar el mouse sobre el boton
        self.pbOpenDatabase.setToolTip("Open database")
        self.pbCreateDatabase.setToolTip("Create database")
        self.pbGo.setToolTip("Next frame")
        self.pbBack.setToolTip("Previous frame")
        self.pbFrameProgrammingLanguage.setToolTip("Frame Programming Language")
        self.pbFrameTypeCreation.setToolTip("Frame Type Creation")
        self.pbFrameTypeApplication.setToolTip("Frame Type Application")
        self.pbFrameProjectTutorial.setToolTip("Frame Project Tutorial")
      

        # Ejecutamos las funciones en los botones del menu principal
        self.pbOpenDatabase.clicked.connect(self.open_file_database)
        self.pbCreateDatabase.clicked.connect(self.close_database)
        self.pbGo.clicked.connect(self.change_frame_go)
        self.pbBack.clicked.connect(self.change_frame_back)
        self.pbInfo.clicked.connect(self.window_info_modal)
        self.pbFrameProgrammingLanguage.clicked.connect(lambda:self.change_frame_button(1))
        self.pbFrameTypeCreation.clicked.connect(lambda:self.change_frame_button(2))
        self.pbFrameTypeApplication.clicked.connect(lambda:self.change_frame_button(3))
        self.pbFrameProjectTutorial.clicked.connect(lambda:self.change_frame_button(4))
        

        





    # Creamos esta funcion para cambiar de frame hacia delante
    def change_frame_go(self):

        # Obtenemos el id del frame abriendo el archivo .json
        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_frame_id = json.loads(json_str)
        frame_id = str_frame_id['frame_id']

        # Aumentamos en 1 el id del frame para moverse al siguiente frame de acuerdo
        # a su valor
        frame_id_plus = frame_id+1

        # Realizamos una validacion del id del frame aumentado, para que el boton sepa
        # que frame ejecutar
        if frame_id_plus == 2:
            # Ejecutamos la funcion del primer Frame la cual va a obtener el id de la fila 
            # seleccionada en la tabla y de esta manera que la siguiente ventana muestre los
            # datos de acuerdo a la relacion de ese id
            if self.frame_programming_language.go_window():
                # Cargamos el siguiente Frame de acuerdo a la su posicion
                self.stackedWidget.setCurrentIndex(2)
                # Ejecutamos esta funcon del Frame que cargamos para que inserte el id del Frame
                self.frame_type_creation.insert_frame_id()
                # Actualizamos la lista del Frame que cargamos para que no exista conflicto con la 
                # informacion desplegada al avanzar o retroceder con el boton
                self.frame_type_creation.get_data() 
                self.enable_disable_buttons()

        elif frame_id_plus == 3:
            if self.frame_type_creation.go_window():       
                self.stackedWidget.setCurrentIndex(3)
                self.frame_type_application.insert_frame_id()
                self.frame_type_application.get_data()
                self.enable_disable_buttons()
        
        elif frame_id_plus == 4:         
            if self.frame_type_application.go_window():
                self.stackedWidget.setCurrentIndex(4)
                self.frame_project_tutorial.insert_frame_id()
                self.frame_project_tutorial.get_data() 
                self.enable_disable_buttons()       
        
        elif frame_id_plus == 5:
            if self.frame_project_tutorial.go_window():
                self.stackedWidget.setCurrentIndex(5)
                self.frame_part.insert_frame_id()
                self.frame_part.get_data()
                self.enable_disable_buttons()









    # Creamos esta funcion para cambiar de frame hacia atras
    def change_frame_back(self):

        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_frame_id = json.loads(json_str)
        frame_id = str_frame_id['frame_id']

        # Disminuimos en 1 el id del frame para moverse al anterior frame de acuerdo
        # a su valor
        frame_id_less = frame_id-1

        if frame_id_less == 4:
            self.frame_part.back_window()
            self.stackedWidget.setCurrentIndex(4)
            self.frame_project_tutorial.insert_frame_id()
            self.frame_project_tutorial.get_data() 
            self.enable_disable_buttons()
        
        elif frame_id_less == 3:
            self.frame_project_tutorial.back_window()
            self.stackedWidget.setCurrentIndex(3)
            self.frame_type_application.insert_frame_id()
            self.frame_type_application.get_data()
            self.enable_disable_buttons()
 
        
        elif frame_id_less == 2:
            self.frame_type_application.back_window()
            self.stackedWidget.setCurrentIndex(2)
            self.frame_type_creation.insert_frame_id()
            self.frame_type_creation.get_data()
            self.enable_disable_buttons()

        
        elif frame_id_less == 1:
            self.frame_type_creation.back_window()
            self.stackedWidget.setCurrentIndex(1)
            self.frame_programming_language.insert_frame_id()
            self.frame_programming_language.get_data()
            self.enable_disable_buttons()





    # Creamos esta funcion para mostrar la informacion de los frames anteriores seleccionados
    def window_info_modal(self):
        self.window = QtWidgets.QMainWindow()
        uic.loadUi(file+"/view/ui/main/info.ui", self.window)
        self.window.show()

        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_frame_id = json.loads(json_str)
        frame_id = str_frame_id['frame_id']

      
        self.window.pbClose.clicked.connect(self.window.hide)

        # Agregamos negrita a los labels
        self.window.lTextProgrammingLanguage.setStyleSheet("font-weight: bold")
        self.window.lTextTypeCreation.setStyleSheet("font-weight: bold")
        self.window.lTextTypeApplication.setStyleSheet("font-weight: bold")
        self.window.lTextProjectTutorial.setStyleSheet("font-weight: bold")

        from controller.type_creation.info import Info as class_type_creation_info
        from controller.type_application.info import Info as class_type_application_info
        from controller.project_tutorial.info import Info as class_project_tutorial_info
        from controller.part.info import Info as class_part_info
        
        info_name_programming_language = class_type_creation_info.list_info()
        info_name_type_creation = class_type_application_info.list_info()
        info_name_type_application = class_project_tutorial_info.list_info()
        info_name_project_tutorial = class_part_info.list_info()

        
        # De acuerdo en el frame que se encuentre va a mostrar la informacion de los labels
        if frame_id == 1:
            self.window.lProgrammingLanguage.setText(info_name_programming_language)
            self.window.lTypeCreation.setText("None")
            self.window.lTypeApplication.setText("None")
            self.window.lProjectTutorial.setText("None")
        
        elif frame_id == 2:
            self.window.lProgrammingLanguage.setText(info_name_programming_language)
            self.window.lTypeCreation.setText(info_name_type_creation)
            self.window.lTypeApplication.setText("None")
            self.window.lProjectTutorial.setText("None")
        
        elif frame_id == 3:
            self.window.lProgrammingLanguage.setText(info_name_programming_language)
            self.window.lTypeCreation.setText(info_name_type_creation)
            self.window.lTypeApplication.setText(info_name_type_application)
            self.window.lProjectTutorial.setText("None")
        
        elif frame_id == 4:
            self.window.lProgrammingLanguage.setText(info_name_programming_language)
            self.window.lTypeCreation.setText(info_name_type_creation)
            self.window.lTypeApplication.setText(info_name_type_application)
            self.window.lProjectTutorial.setText(info_name_project_tutorial)

        


        



    # Creamos esta funcion para ejecutar el frame respectivo de acuerdo a su id
    def change_frame_button(self, frame_id_button):

        if frame_id_button == 1:
            self.stackedWidget.setCurrentIndex(1)
            self.frame_programming_language.insert_frame_id()
            self.enable_disable_buttons()
        
        elif frame_id_button == 2:
            self.stackedWidget.setCurrentIndex(2)
            self.frame_type_creation.insert_frame_id()
            self.enable_disable_buttons()

        elif frame_id_button == 3:
            self.stackedWidget.setCurrentIndex(3)
            self.frame_type_application.insert_frame_id()
            self.enable_disable_buttons()
        
        elif frame_id_button == 4:
            self.stackedWidget.setCurrentIndex(4)
            self.frame_project_tutorial.insert_frame_id()
            self.enable_disable_buttons()








    # Creamos esta funcion para habilitar o deshabilitar los botones de la ventana principal
    # de acuerdo al id del frame
    def enable_disable_buttons(self):

        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_frame_id = json.loads(json_str)
        frame_id = str_frame_id['frame_id']

        if frame_id == 0:
            self.pbGo.setEnabled(False)
            self.pbBack.setEnabled(False)
            self.pbInfo.setEnabled(False)
            self.pbFrameProgrammingLanguage.setEnabled(False)
            self.pbFrameTypeCreation.setEnabled(False)
            self.pbFrameTypeApplication.setEnabled(False)
            self.pbFrameProjectTutorial.setEnabled(False)

        elif frame_id == 1:
            self.pbGo.setEnabled(True)
            self.pbBack.setEnabled(False)
            self.pbInfo.setEnabled(False)
            self.pbFrameProgrammingLanguage.setEnabled(False)
            self.pbFrameTypeCreation.setEnabled(False)
            self.pbFrameTypeApplication.setEnabled(False)
            self.pbFrameProjectTutorial.setEnabled(False)
            self.lTitleMain.setText("Programming language")

        elif frame_id == 2:
            self.pbGo.setEnabled(True)
            self.pbBack.setEnabled(True)
            self.pbInfo.setEnabled(True)
            self.pbFrameProgrammingLanguage.setEnabled(True)
            self.pbFrameTypeCreation.setEnabled(False)
            self.pbFrameTypeApplication.setEnabled(False)
            self.pbFrameProjectTutorial.setEnabled(False)
            self.lTitleMain.setText("Type creation")
        
        elif frame_id == 3:
            self.pbGo.setEnabled(True)
            self.pbBack.setEnabled(True)
            self.pbInfo.setEnabled(True)
            self.pbFrameProgrammingLanguage.setEnabled(True)
            self.pbFrameTypeCreation.setEnabled(True)
            self.pbFrameTypeApplication.setEnabled(False)
            self.pbFrameProjectTutorial.setEnabled(False)
            self.lTitleMain.setText("Type application")
        
        elif frame_id == 4:
            self.pbGo.setEnabled(True)
            self.pbBack.setEnabled(True)
            self.pbInfo.setEnabled(True)
            self.pbFrameProgrammingLanguage.setEnabled(True)
            self.pbFrameTypeCreation.setEnabled(True)
            self.pbFrameTypeApplication.setEnabled(True)
            self.pbFrameProjectTutorial.setEnabled(False)
            self.lTitleMain.setText("Project tutorial")
        
        elif frame_id == 5:
            self.pbGo.setEnabled(False)
            self.pbBack.setEnabled(True)
            self.pbInfo.setEnabled(True)
            self.pbFrameProgrammingLanguage.setEnabled(True)
            self.pbFrameTypeCreation.setEnabled(True)
            self.pbFrameTypeApplication.setEnabled(True)
            self.pbFrameProjectTutorial.setEnabled(True)
            self.lTitleMain.setText("Part")


    
    # Abrimos el archivo de base de datos
    def open_file_database(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","SQLite Files (*.db)", options=options)
        if file_name:

            with open('src/data.json', 'r+') as f:
                data = json.load(f)
                data["route_open_database"] = file_name
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            
            self.reload_modules()

            #self.stackedWidget.setCurrentIndex(0)
            #self.stackedWidget.removeWidget(self.frame_programming_language)
            self.frame_programming_language.get_data()
            self.stackedWidget.setCurrentIndex(1)
            self.frame_programming_language.get_data()
            self.frame_programming_language.insert_frame_id()
            self.enable_disable_buttons()
    

    '''
    # Abrimos el archivo de base de datos
    def open_file_database(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        file_name, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","SQLite Files (*.db)", options=options)
        if file_name:
            
            with open('src/data.json', 'r+') as f:
                data = json.load(f)
                data["route_open_database"] = file_name
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
            
            with open('src/data.json', 'r') as f:
                data = json.load(f)
                json_str = json.dumps(data)
                str_frame_id = json.loads(json_str)
                frame_id = str_frame_id['frame_id']
            
            if frame_id == 0:
                print("primera forma")
                #self.stackedWidget.setCurrentIndex(0)
                #self.stackedWidget.removeWidget(self.frame_programming_language)
                self.stackedWidget.setCurrentIndex(1)
                self.frame_programming_language.get_data()
                self.frame_programming_language.insert_frame_id()
                self.enable_disable_buttons()
            else:
                print("segunda forma")
                self.stackedWidget.setCurrentIndex(1)
                self.frame_programming_language.get_data_c()
                self.frame_programming_language.insert_frame_id()
                self.enable_disable_buttons()
    '''
    




    # Creamos el archivo de base de datos
    def create_file_database(self):
        self.window = QtWidgets.QMainWindow()
        uic.loadUi(file+"/view/ui/option_database/form.ui", self.window)
        self.window.show()

        self.window.pbCreateDatabse.clicked.connect(lambda: self.open_directory(self.window.leNameDatabase.text()))
        self.window.pbCancel.clicked.connect(self.window.hide)
    

    # Abrimos el directorio donde se va a crear la base de datos
    def open_directory(self, name_database):

        if self.validation_form_database_window(name_database):

            self.window.hide()
            directory = str(QtWidgets.QFileDialog.getExistingDirectory())

            if directory:
                
                directory_database = directory+"/"+name_database+".db"
                print(directory_database)

                with open('src/data.json', 'r+') as f:
                    data = json.load(f)
                    data["route_create_database"] = directory_database
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()

                # Ejecutamos el archivo python para que se cree la base de datos
                from model import database_create
            
                self.stackedWidget.setCurrentIndex(1)
                self.frame_programming_language.insert_frame_id()
                self.frame_programming_language.get_data()
                self.enable_disable_buttons()
    

    def close_database(self):
        self.stackedWidget.setCurrentIndex(0)
        self.enable_disable_buttons()
    

    # Creamos una funcion para recargar los modulos del CRUD que importamos con la finalidad
    # de que cuando se cambie la base de datos, los datos se actualicen automaticamente
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

        import controller.type_application.list
        import controller.type_application.count
        import controller.type_application.insert
        import controller.type_application.update
        import controller.type_application.delete

        import controller.project_tutorial.list
        import controller.project_tutorial.count
        import controller.project_tutorial.insert
        import controller.project_tutorial.update
        import controller.project_tutorial.delete
        import controller.project_tutorial.search
        import controller.project_tutorial.count_search

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

        importlib.reload(controller.type_application.list)
        importlib.reload(controller.type_application.count)
        importlib.reload(controller.type_application.insert)
        importlib.reload(controller.type_application.update)
        importlib.reload(controller.type_application.delete)

        importlib.reload(controller.project_tutorial.list)
        importlib.reload(controller.project_tutorial.count)
        importlib.reload(controller.project_tutorial.insert)
        importlib.reload(controller.project_tutorial.update)
        importlib.reload(controller.project_tutorial.delete)
        importlib.reload(controller.project_tutorial.search)
        importlib.reload(controller.project_tutorial.count_search)


                
    



    def validation_form_database_window(self, name_database):
        if(len(name_database) == 0):
            self.window.lMessageForm.setText('<font color="red">Database name is required</font>')
        else:
            return name_database
    
                



app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
#widget.setFixedWidth(400)
#widget.setFixedHeight(300)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")