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





class Help:

    # Creamos una sesion
    Session = sessionmaker(bind=engine)
    session = Session()


    # Creamos 1 arreglo vacio para almacenar la informacion que obtendremos
    # al recorrer el for
    programming_language_name = []
    type_creation_name = []
   



    # Abrimos el archivo .txt que contiene e id de la tabla Type Application, esto lo 
    # hacemos ya que al regresar a nuestra ventana debemos obtener este id para que se
    # muestren los datos correctamente
    f_tc = open('id-window-tc.txt', 'r')
    file_contents_tc = f_tc.read()
    f_tc.close()




   







    # Realizamos la consulta de los campos que tienen relacion mediante un join y  lo
    # almacenamos en una variable

    # desc() = aqui le indicamos que ordene la consulta en forma descendente por el campo que hemos establecido 
    data_pl = session.query(TypeCreation, ProgrammingLanguage).join(TypeCreation).filter(TypeCreation.id_programming_language == file_contents_tc).all()


   


   

   





    # Recorremos el objeto donde almacena la informacion, para obtener el lenguaje de programacion

    # [:1] = aqui le indicamos que solo obtenga el primer dato que recorra el for
    for type_creation, programming_language in data_pl[:1]:

        # Creamos un nuevo arreglo, llenos de arreglos obtenidos de los datos
        # que vamos obteniendo del for

        # append = permite crear un arreglo a partir de la obtencion de datos del for
        programming_language_name.append(programming_language.name)



    








    # Almacenamos el primer dato obtenida del for en una variable, para despues usarla
    valor_pl = programming_language_name[0]
    
