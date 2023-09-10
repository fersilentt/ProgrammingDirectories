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







class Insert:

    # Creamos una funcion que va a insertar los datos
    def add_data(
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
        id):


        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()


        # Create objects  
        project_tutorial = ProjectTutorial(
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
            id)

        session.add(project_tutorial)

        
        # Hacemos un commit en la base de datos
        session.commit()
