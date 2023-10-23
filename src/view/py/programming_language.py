import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox, QAbstractItemView
from PyQt5.uic import loadUi
from PyQt5 import uic

# Agregamos esta libreria para poder mostrar enteros en nuestra
# tabla usando Roles
from PyQt5.QtCore import Qt

# Importamos este modulo para trabajat con objetos json
import json





# Importamos este modulo para poder inertar el path, de donde se encuentran 
# los archivos del CRUD, de esta manera podremos importar nuestros archivos
# independientemmente de cualquier carpeta de donde se encuentren
import sys

# Importamos este modulo para obtener una ruta absoluta de
# nuestro proyecto, para poder importar las imagenes para 
# nuestros botones
import os

# os.path.abspath("src") = obtenemos la ruta absoluta del proyecto para desepues importar
#                          los archivos
file = os.path.abspath("src")

# Agregamoso la ruta absoluta de nuestro proyeto, para que reconozca la ruta de importacion
# de los archivos que realizan el CRUD
sys.path.insert(0, file)



import importlib









class FrameProgrammingLanguage(QtWidgets.QFrame):

    def __init__(self):
        super(FrameProgrammingLanguage,self).__init__()
        # Importamos el archivo .ui llamando a la ruta aboluta que anetriormente hemos creado
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

        # Aqui establecemos el tamaño que va a tener cada columna de acuerdo
        # a su posicion, pero en este caso lo comentamos para que quede en
        # su forma original
        #self.tableWidget.setColumnWidth(0, 250)
        #self.tableWidget.setColumnWidth(1, 100)
        #self.tableWidget.setColumnWidth(2, 350)
        
        # Enviamos los nombres de las cabeceras que va a tener nuestra tabla,
        # reemplazando a las caberceras en el caso que ya las tuviera
        self.tableWidget.setHorizontalHeaderLabels(["Id","Name"])

        # Agregamos esto para poder seleccionar toda la fila en lugar de seleccionar celda por celda
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        #self.tableWidget.verticalHeader().setVisible(False)
        # Ordenamos de forma ascendente y descendente con un clic todas las columnas de la tabla
        self.tableWidget.setSortingEnabled(True)

        # Ocultamos la columna 0 de la tabla
        self.tableWidget.setColumnHidden(0,True)



        # Creamos los iconos para los botones

        # Obtenemos la ruta de la imagen para despues agregarla al boton
        icon_add  = QtGui.QPixmap(os.path.abspath("src/static/add.svg"))
        icon_update  = QtGui.QPixmap(os.path.abspath("src/static/update.svg"))
        icon_delete  = QtGui.QPixmap(os.path.abspath("src/static/delete.svg"))
        
        # Agregamos la imagen al boton
        self.pbAdd.setIcon(QtGui.QIcon(icon_add))
        self.pbEdit.setIcon(QtGui.QIcon(icon_update))
        self.pbDelete.setIcon(QtGui.QIcon(icon_delete))
        #self.pbAdd.setIconSize(QtCore.QSize(200,200))


        # Ejecutamos las funciones del CRUD
        self.pbAdd.clicked.connect(lambda: self.add_update_window_modal(0))
        self.pbEdit.clicked.connect(lambda: self.add_update_window_modal(1))
        self.pbDelete.clicked.connect(self.delete_window)
        self.leSearch.textChanged.connect(self.scan_q_line_edit)

        # Realizamos una limpieza del label que actua como mensaje
        self.lMessageList.setText("")

 


        







    # Creamos la ventana para agregar y actualizar los datos
    def add_update_window_modal(self, id_window_modal):

        # Validamos si el id del formulario es 0 sera para insertar, 1 sera para actualizar
        if id_window_modal != 0:

            # Obtenemos los datos de la fila seleccionada
            r = self.tableWidget.currentRow()

            if r == -1:
                self.lMessageList.setText('<font color="red">Please select a record</font>')
            else:
                # Ejecutamos la ventana modal y la abrimos
                self.window = QtWidgets.QMainWindow()
                uic.loadUi(file+"/view/ui/programming_language/form.ui", self.window)
                self.window.show()

                # Obtemos los datos de la fila de acuerdo a su posicion
                id = self.tableWidget.item(r,0).text()
                name = self.tableWidget.item(r,1).text()

                # Enviamos los datos a las cajas de texto
                self.window.leName.setText(name)

                # Cambiamos el nombre del boton
                self.window.pbAddUpdate.setText("Update")
                
                # Enviamos los datos para actualizar
                self.window.pbAddUpdate.clicked.connect(lambda: self.update_data(id, self.window.leName.text()))


        else:
            self.window = QtWidgets.QMainWindow()
            uic.loadUi(file+"/view/ui/programming_language/form.ui", self.window)
            self.window.show()

            self.window.pbAddUpdate.setText("Add")
            self.window.pbAddUpdate.clicked.connect(lambda: self.add_data(self.window.leName.text()))




    # Creamos la ventana para eliminar los datos
    def delete_window(self): 

        r = self.tableWidget.currentRow()
        id = self.tableWidget.item(r,0).text()

        # Mostramos un mensaje de informacion para indicar si se desea eliminar o no el dato
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



    # Insertamos el id del Frame, para que sea identificado
    def insert_frame_id(self):
        with open('src/data.json', 'r+') as f:
            data = json.load(f)
            data["frame_id"] = 1
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate() 
        



    # Obtenemos el id de la tabla para que la siguiente ventana cargue
    def go_window(self):
        
        r = self.tableWidget.currentRow()

        if r == -1:
            self.lMessageList.setText('<font color="red">Please select a record</font>')
            return False
        else: 
            id = self.tableWidget.item(r,0).text()

            # Editamos los campos de nuestro objeto json para almacenar el id de la tabla que se va a obtener
            with open('src/data.json', 'r+') as f:
                data = json.load(f)
                # Aqui editamos el valor del campo "window_table_id" y lo reemplazamos por el id de la tabla
                data["window_table_id"] = id
                data["window_programming_language_id"] = id
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate() 
            return True
    

    
    
        


   






    # FUNCIONES PARA REALIZAR EL CRUD 

    # Creamos una funcion para obtener la lista de datos
    def get_data(self):
        import controller.programming_language.list
        import controller.programming_language.count

        #importlib.reload(controller.programming_language.list)
        #importlib.reload(controller.programming_language.count)
        #self.reload_modules()
        
        # LLamamos a la funcion list_word(), que va a traer la lista de
        # estudiantes de la base de datos
        lista = controller.programming_language.list.List.list_data()
        count_rows = controller.programming_language.count.Count.count_rows()


        # Establecemos en 0 el valor que incrementa cada fila en nuestra tabla
        tablerow=0

        # Establecemos el numero de registros que vamos a obteber de nuestra consulta
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(count_rows)
        

        # LLenamos los datos obtenidos de la consulta en la tabla
        for id,name in zip(*lista): 

            # Creamos este codigo para mostrar enteros en nuestra tabla usando Roles
            # si no usamos este codigo no podremos ver los numeros en nuestra tabla
            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, id)
            
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(item))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(name))

            # Incrementamos en 1 la fila de nuestra tabla
            tablerow+=1

        '''
        # Enviamos la posicion de la fila que queremos que se preseleccione
        list_selection = [0]
        self.select_rows(list_selection)
        '''
    


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





    # Creamos una funcion para insertar los datos
    def add_data(self, name):  

        import controller.programming_language.insert
        #self.reload_modules()

        # LLamamos a la funcion de validacion para comprobar que las cajas de texto no esten vacias
        if self.validation_add_update_window(name):

            # Insertamos los datos
            controller.programming_language.insert.Insert.add_data(name)
            # Ocultamos la ventana
            self.window.hide()
            # Mostramos un mensaje  con un color
            self.lMessageList.setText('<font color="green">Data added successfully</font>')
            # Actualizamos la lista de datos
            self.get_data()



    # Creamos una funcion para actualizar los datos
    def update_data(self, id, name):

        import controller.programming_language.update

        if self.validation_add_update_window(name):

            controller.programming_language.update.Update.update_data(id, name)
            self.window.hide()
            self.lMessageList.setText('<font color="green">Data updated successfully</font>')
            self.get_data()





    # Creamos una funcion para eliminar los datos
    def delete_data(self, id):

        import controller.programming_language.delete

        controller.programming_language.delete.Delete.delete_data(id)
        self.lMessageList.setText('<font color="green">Data deleted successfully</font>')
        self.get_data()
    



    # Creamos una funcion para buscar los datos
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

    




    # Creamos una funcion que permite obtener el valor que ingresemos en la
    # caja de texto de una forma rapida

    # event = contains the text of the line edit, we could also test
    def scan_q_line_edit(self, event):
        
        # Validamos que el dato ingresado en la caja de texto sea buscado en la base de datos
        if event:
            self.search_data(event)
        # Caso contrario mostraremos toda la lista de datos
        else:
            self.get_data_general_search()
            



    
    









    # FUNCIONES QUE VAN A VALIDAR LAS CAJAS DE TEXTO


    # Creamos una funcion que va a permitir validar que las cajas de texto no esten vacias
    # en el formulario de agregar estudiante
    def validation_add_update_window(self, name):

        # Validamos que las cajas de texto no no esten vacias

        # len = metodo que permite obtener la longitud de un elemento
        # == 0 = aqui le indicamos que la longitud del valor ingresado sea igual a 0
        if(len(name) == 0):
            self.window.lMessageForm.setText('<font color="red">Name is required</font>')

        # Caso contrario retornamos los valores de los datos
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
