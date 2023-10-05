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




'''
Session = sessionmaker(bind=engine)
session = Session()

for programming_language in session.query(ProgrammingLanguage).order_by(ProgrammingLanguage.name.desc()):
    print(programming_language.id, programming_language.name)
    data = [programming_language.id, programming_language.name]
'''




class List:


    def list_data():
        
        #engine = create_engine('sqlite:///student.db', echo=True)


        # Creamos una sesion
        Session = sessionmaker(bind=engine)
        session = Session()


        # Creamos arreglos vacios para almacenar la informacion que obtendremos
        # al recorrer el for
        id = []
        name = []
        

        # Creamos un manejo de exepciones para cerrar la conexion de la base de datos un vez ejecutada la transaccion
        # y asi evitar que la aplicacion colapse por exesivas peticiones a la base de datos
        try:
            # Recorremos el objeto donde almacena la informacion 

            # programming_language = variable que almacena los datos obtenidos de nuestra consulta 
            # desc() = aqui le indicamos que ordene la consulta en forma descendente por el campo que hemos establecido 
            for programming_language in session.query(ProgrammingLanguage).order_by(ProgrammingLanguage.name.desc()):
                
                # Creamos un nuevo arreglo, llenos de arreglos obtenidos de los datos
                # que vamos obteniendo del for

                # append = permite crear un arreglo a partir de la obtencion de datos del for
                id.append(programming_language.id)
                name.append(programming_language.name)
                

            
            # Creamos un nuevo arreglo con la lista de arreglos obtenidos
            # para despues recorrerlos y mostrarlos en la vista
            my_list = [(id), (name)]

        finally:
            session.close()
          
        
  

        # Retornamos el arreglo nuevo con la lista de arreglos con la finalidad
        # de importarlo despues
        return my_list
    

    
    
 