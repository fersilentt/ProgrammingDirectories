from sqlalchemy.orm import sessionmaker



# Importamos este modulo para obtener una ruta absoluta de
# nuestro proyecto, para poder importar las imagenes para 
# nuestros botones
import os


# Importamos este modulo para poder inertar el path, de donde se encuentran 
# los archivos del CRUD, de esta manera podremos importar nuestros archivos
# independientemmente de cualquier carpeta de donde se encuentren
import sys

# os.path.abspath("src") = obtenemos la ruta absoluta del proyecto para desepues importar
#                          los archivos
file = os.path.abspath("src")

# Agregamoso la ruta absoluta de nuestro proyeto, para que reconozca la ruta de importacion
# de los archivos que realizan el CRUD
sys.path.insert(0, file)




# Importamos las clases donde se va a realizar un CRUD
from model.database_open import *


# Importamos la variable que conetiene la ruta de donde se creara
# la base de datos para evitar
from model.database_open import engine








class List:


    def list_data():
        
        # Abrimos el archivo .txt que contiene el id del dato que hemos seleccionado en la ventana
        # anterior
        f = open('id-window.txt', 'r')
        id_window = f.read()
        f.close()


        # Creamos una sesion
        Session = sessionmaker(bind=engine)
        session = Session()


        # Creamos arreglos vacios para almacenar la informacion que obtendremos
        # al recorrer el for
        id = []
        name = []
        programming_language_version = []
        framework = []
        graphical_interface = []
        data_base = []
        data_base_version = []
        orm = []
        virtual_environment = []
        architecture = []
        cloud_server = []
        number_project_tutorial = []
        name_type_application = []
        id_type_application = []
        
        
        


        # Realizamos la consulta de los campos que tienen relacion mediante un join y  lo
        # almacenamos en una variable

        # desc() = aqui le indicamos que ordene la consulta en forma descendente por el campo que hemos establecido 
        data = session.query(ProjectTutorial, TypeApplication).join(ProjectTutorial).filter(
            ProjectTutorial.id_type_application == id_window).order_by(ProjectTutorial.number_project_tutorial.asc()).all()




        # Recorremos el objeto donde almacena la informacion 

        # project_tutorial = variable que almacena los datos obtenidos de nuestra consulta 
        for project_tutorial, type_application in data:
            
            # Creamos un nuevo arreglo, llenos de arreglos obtenidos de los datos
            # que vamos obteniendo del for

            # append = permite crear un arreglo a partir de la obtencion de datos del for
            id.append(project_tutorial.id)
            name.append(project_tutorial.name)
            programming_language_version.append(project_tutorial.programming_language_version)
            framework.append(project_tutorial.framework)
            graphical_interface.append(project_tutorial.graphical_interface)
            data_base.append(project_tutorial.data_base)
            data_base_version.append(project_tutorial.data_base_version)
            orm.append(project_tutorial.orm)
            virtual_environment.append(project_tutorial.virtual_environment)
            architecture.append(project_tutorial.architecture)
            cloud_server.append(project_tutorial.cloud_server)
            number_project_tutorial.append(project_tutorial.number_project_tutorial)
            name_type_application.append(type_application.name)
            id_type_application.append(type_application.id)
            


        # Creamos un nuevo arreglo con la lista de arreglos obtenidos
        # para despues recorrerlos y mostrarlos en la vista
        my_list = [(id), 
        (name),
        (programming_language_version), 
        (framework), 
        (graphical_interface), 
        (data_base), 
        (data_base_version),
        (orm), 
        (virtual_environment),
        (architecture),
        (cloud_server),
        (number_project_tutorial),
        (name_type_application),
        (id_type_application)]
          
           


        # Retornamos el arreglo nuevo con la lista de arreglos con la finalidad
        # de importarlo despues
        return my_list
    

    
    
 