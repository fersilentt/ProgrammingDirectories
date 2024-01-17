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
        
        
        # We open the .json file and its field containing the id of the data we have selected in the previous window

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
            # We perform the query of the fields that are related by means of a join and we store it in a variable 
            # stored in a variable
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
    

    
    
 