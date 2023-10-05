from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine

class Info:


    def list_info():

        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window_type_creation  = json.loads(json_str)
        id_window_type_creation = str_id_window_type_creation['window_type_creation_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        name_type_creation = []

        try:
            data = session.query(TypeApplication, TypeCreation).join(TypeApplication).filter(
                TypeApplication.id_type_creation == id_window_type_creation).all()

            for type_application, type_creation in data[:1]:
                name_type_creation.append(type_creation.name)

            info_name_type_creation = name_type_creation[0]
            
        finally:
            session.close()
                  
        return info_name_type_creation
    

    
    
 