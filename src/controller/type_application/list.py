from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine



class List:

    def list_data():

        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window = str_id_window['window_table_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        id = []
        name = []
        name_type_creation = []
        id_type_creation = []
        
        try:
            data = session.query(TypeApplication, TypeCreation).join(TypeApplication).filter(
                TypeApplication.id_type_creation == id_window).order_by(TypeApplication.name.desc()).all()

            for type_application, type_creation in data:
                id.append(type_application.id)
                name.append(type_application.name)
                name_type_creation.append(type_creation.name)
                id_type_creation.append(type_creation.id)
                
            my_list = [(id), (name), (name_type_creation), (id_type_creation)]

        finally:
            session.close()
           
        return my_list
    

    
    
 