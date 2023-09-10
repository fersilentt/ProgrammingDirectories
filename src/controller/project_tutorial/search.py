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








class Search:


    # Creamos una funcion que va buscar los datos

    # data = este va a ser el dato por el cual se va a buscar en la base de datos el
    #        cual vamos a pasarle desde la caja de texto
    def search_data(data):

        

        # Creamos la sesion
        Session = sessionmaker(bind=engine)
        session = Session()
        

        # Creamos arreglos vacios para almacenar la informacion que obtendremos
        # al recorrer el for
        id = []
        name = []
        framework = []
        graphical_interface = []
        data_base = []
        orm = []
        virtual_environment = []
        architecture = []
        cloud_server = []
        name_type_application = []
        

        
        # Realizamos la consulta de los campos que tienen relacion mediante un join y  lo
        # almacenamos en una variable, ademas aqui realizamos la busquema mediante varios 
        # campos, aqui usamos un like como en SQL , pero buscamos por varios campos usando 
        # or, como lo hariamos en SQL

        # all() = esto permite obtener toda la lista de datos que tiene similitud
        # or_( = esto indica que la conulta va usar OR y no AND
        # {} = esto permite agregar un valor dentro del mensaje
        # format() = permite pasarle un valor dentro de las llaves {}
        # data = aqui va el dato por el cual se va a buscar en la base de datos
        query = session.query(ProjectTutorial, TypeApplication).join(ProjectTutorial).filter(or_(
            ProjectTutorial.name.like('%{}%'.format(data)))).all()
        
        for project_tutorial, type_application in query:
            
            id.append(project_tutorial.id)
            name.append(project_tutorial.name)
            framework.append(project_tutorial.framework)
            graphical_interface.append(project_tutorial.graphical_interface)
            data_base.append(project_tutorial.data_base)
            orm.append(project_tutorial.orm)
            virtual_environment.append(project_tutorial.virtual_environment)
            architecture.append(project_tutorial.architecture)
            cloud_server.append(project_tutorial.cloud_server)
            name_type_application.append(type_application.name)

        
        
        # Creamos un nuevo arreglo con la lista de arreglos obtenidos
        # para despues recorrerlos y mostrarlos en la vista
        my_list = [(id), 
        (name), 
        (framework), 
        (graphical_interface), 
        (data_base), (orm), 
        (virtual_environment),
        (architecture),
        (cloud_server),
        (name_type_application)]




        # Retornamos el arreglo nuevo con la lista de arreglos con la finalidad
        # de importarlo despues
        return my_list
