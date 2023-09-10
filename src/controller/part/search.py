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


           
        # Abrimos el archivo .txt que contiene el id del dato que hemos seleccionado en la ventana
        # anterior
        f = open('id-window.txt', 'r')
        id_window = f.read()
        f.close()



        # Creamos la sesion
        Session = sessionmaker(bind=engine)
        session = Session()
        

        # Creamos arreglos vacios para almacenar la informacion que obtendremos
        # al recorrer el for
        id = []
        name = []
        repository = []
        youtube_video = []
        id_part = []
        name_project_tutorial = []
        id_project_tutorial = []
        

        
        # Realizamos la consulta de los campos que tienen relacion mediante un join y  lo
        # almacenamos en una variable, ademas aqui realizamos la busquema mediante varios 
        # campos, aqui usamos un like como en SQL , pero buscamos por varios campos usando 
        # or, como lo hariamos en SQL

        # all() = esto permite obtener toda la lista de datos que tiene similitud
        # or_( = esto indica que la conulta va usar OR y no AND
        # {} = esto permite agregar un valor dentro del mensaje
        # format() = permite pasarle un valor dentro de las llaves {}
        # data = aqui va el dato por el cual se va a buscar en la base de datos
        #query = session.query(Part, ProjectTutorial).join(Part).filter(and_(Part.name.like('%{}%'.format(data)) , Part.id_project_tutorial == id_window )).all()
        query = session.query(Part, ProjectTutorial).join(Part).filter(or_(Part.name.like('%{}%'.format(data)))).filter(Part.id_project_tutorial == id_window).all()

        for part, project_tutorial in query:
            
            id.append(part.id)
            name.append(part.name)
            repository.append(part.repository)
            youtube_video.append(part.youtube_video)
            id_part.append(part.id_part)
            name_project_tutorial.append(project_tutorial.name)
            id_project_tutorial.append(project_tutorial.id)

        
        
        # Creamos un nuevo arreglo con la lista de arreglos obtenidos
        # para despues recorrerlos y mostrarlos en la vista
        my_list = [(id), (name), (repository), (youtube_video), (id_part), (name_project_tutorial), (id_project_tutorial)]




        # Retornamos el arreglo nuevo con la lista de arreglos con la finalidad
        # de importarlo despues
        return my_list
