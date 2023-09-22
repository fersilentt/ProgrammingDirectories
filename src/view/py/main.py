import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

import json

import sys
import os
file = os.path.abspath("src")
sys.path.insert(0, file)

from view.py.programming_language import FrameProgrammingLanguage
#from view.py.part import FramePart



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi(file+"/view/ui/main.ui",self)



         # Creamos los iconos para los botones
        icon_open_database  = QtGui.QPixmap(os.path.abspath("src/static/open_database.svg"))
        icon_create_database  = QtGui.QPixmap(os.path.abspath("src/static/create_database.svg"))
        icon_go  = QtGui.QPixmap(os.path.abspath("src/static/go.svg"))
        icon_back  = QtGui.QPixmap(os.path.abspath("src/static/back.svg"))
    
        self.pbOpenDatabase.setIcon(QtGui.QIcon(icon_open_database))
        self.pbCreateDatabase.setIcon(QtGui.QIcon(icon_create_database))
        self.pbGo.setIcon(QtGui.QIcon(icon_go))
        self.pbBack.setIcon(QtGui.QIcon(icon_back))
        

        # Cargamos el Frame con el que va a arrancar la aplicacion lo almacenamos en variables
        self.frame_programming_language= FrameProgrammingLanguage()
        

        # Agregamos el Frame a stackedWidget, para que pueda visualizarse
        self.stackedWidget.addWidget(self.frame_programming_language)

        '''
        self.frame_part= FramePart()
        self.stackedWidget.addWidget(self.frame_part)
        '''
        

        # Ejecutamos las funciones en los botones del menu principal
        self.pbGo.clicked.connect(self.change_frame_go)
        self.pbBack.clicked.connect(self.change_frame_back)

        





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
        if frame_id_plus == 1:
            
            # Ejecutamos la funcion del primer Frame la cual va a obtener el id de la fila 
            # seleccionada en la tabla y de esta manera que la siguiente ventana muestre los
            # datos de acuerdo a la relacion de ese id
            self.frame_programming_language.go_window()

            # Ejecutamos la clase del siguiente Frame a donde nos vamos a mover, lo realizamos de 
            # esta menra ya que si lo importamos desde las librerias principales se va a insertar
            # los id del frame de forma automatica y ya no podremos movernos como queremos
            from view.py.type_creation import FrameTypeCreation
            self.frame_type_creation= FrameTypeCreation()
            self.stackedWidget.addWidget(self.frame_type_creation)
            self.stackedWidget.setCurrentIndex(1)


        elif frame_id_plus == 2:
            
            self.frame_type_creation.go_window()
            
            from view.py.type_application import FrameTypeApplication
            self.frame_type_application= FrameTypeApplication()
            self.stackedWidget.addWidget(self.frame_type_application)
            self.stackedWidget.setCurrentIndex(2)
        
        elif frame_id_plus == 3:
            
            self.frame_type_application.go_window()
            
            from view.py.project_tutorial import FrameProjectTutorial
            self.frame_project_tutorial= FrameProjectTutorial()
            self.stackedWidget.addWidget(self.frame_project_tutorial)
            self.stackedWidget.setCurrentIndex(3)

            
        
        elif frame_id_plus == 4:
            
            self.frame_project_tutorial.go_window()
            
            from view.py.part import FramePart
            self.frame_part= FramePart()
            self.stackedWidget.addWidget(self.frame_part)
            self.stackedWidget.setCurrentIndex(4)

            self.pbGo.setEnabled(False)


        #self.stackedWidget.setCurrentIndex(0)






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

        if frame_id_less == 3:

            self.frame_part.back_window()

            from view.py.project_tutorial import FrameProjectTutorial
            self.frame_project_tutorial= FrameProjectTutorial()
            self.stackedWidget.addWidget(self.frame_project_tutorial)
            self.stackedWidget.setCurrentIndex(3)

            self.pbGo.setEnabled(True)








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