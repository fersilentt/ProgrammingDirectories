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
        str_id_window_programming_language  = json.loads(json_str)
        id_window_programming_language = str_id_window_programming_language['window_programming_language_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        name_programming_language = []

        try:
            data = session.query(TypeCreation, ProgrammingLanguage).join(TypeCreation).filter(
            TypeCreation.id_programming_language == id_window_programming_language).all()

            # [:1] = aqui le indicamos que solo obtenga el primer dato que recorra el for
            for type_creation, programming_language in data[:1]:
                name_programming_language.append(programming_language.name)

            # Almacenamos el primer dato obtenido del for en una variable
            info_name_programming_language = name_programming_language[0]
        
        finally:
            session.close()
            
        

        return info_name_programming_language

#sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached, connection timed out, timeout 30.00 (Background on this error at: https://sqlalche.me/e/20/3o7r)
#24

    
    