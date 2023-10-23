from sqlalchemy.orm import sessionmaker
import json

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine



class List:

    def list_data():
        
        
        # Abrimos el archivo .json y su campo que contiene el id del dato que hemos seleccionado en la ventana
        # anterior

        # Load the data into an element
        with open('src/data.json', 'r') as f:
            data = json.load(f)

        # Dumps the json object into an element
        json_str = json.dumps(data)

        # Load the json to a string
        str_id_window = json.loads(json_str)

        # We get the id of the window field
        id_window = str_id_window['window_table_id']




        Session = sessionmaker(bind=engine)
        session = Session()


        id = []
        name = []
        name_programming_language = []
        id_programming_language = []
        

        try:
            # Realizamos la consulta de los campos que tienen relacion mediante un join y  lo
            # almacenamos en una variable
            data = session.query(TypeCreation, ProgrammingLanguage).join(TypeCreation).filter(
                TypeCreation.id_programming_language == id_window).order_by(TypeCreation.name.desc()).all()

            for type_creation, programming_language in data:
        
                id.append(type_creation.id)
                name.append(type_creation.name)
                name_programming_language.append(programming_language.name)
                id_programming_language.append(programming_language.id)
                
            my_list = [(id), (name), (name_programming_language), (id_programming_language)]

        finally:
            session.close()
         
          
        return my_list
    

    
    
 