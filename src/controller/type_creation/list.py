from sqlalchemy.orm import sessionmaker


import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
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
        name_programming_language = []
        id_programming_language = []
        


        # Realizamos la consulta de los campos que tienen relacion mediante un join y  lo
        # almacenamos en una variable

        # desc() = aqui le indicamos que ordene la consulta en forma descendente por el campo que hemos establecido 
        data = session.query(TypeCreation, ProgrammingLanguage).join(TypeCreation).filter(
            TypeCreation.id_programming_language == id_window).order_by(TypeCreation.name.desc()).all()




        # Recorremos el objeto donde almacena la informacion 

        # type_creation = variable que almacena los datos obtenidos de nuestra consulta 
        for type_creation, programming_language in data:
            
            # Creamos un nuevo arreglo, llenos de arreglos obtenidos de los datos
            # que vamos obteniendo del for

            # append = permite crear un arreglo a partir de la obtencion de datos del for
            id.append(type_creation.id)
            name.append(type_creation.name)
            name_programming_language.append(programming_language.name)
            id_programming_language.append(programming_language.id)
            


        # Creamos un nuevo arreglo con la lista de arreglos obtenidos
        # para despues recorrerlos y mostrarlos en la vista
        my_list = [(id), (name), (name_programming_language), (id_programming_language)]
          
           


        # Retornamos el arreglo nuevo con la lista de arreglos con la finalidad
        # de importarlo despues
        return my_list
    

    
    
 