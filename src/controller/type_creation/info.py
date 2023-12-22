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
        str_id_window_programming_language = json.loads(json_str)
        id_window_programming_language = str_id_window_programming_language['window_programming_language_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        name_programming_language = []

        try:

            # [:1] = here we tell it to only get the first data that runs through the for
            # for type_creation, programming_language in data[:1]:

            for programming_language in session.query(ProgrammingLanguage).filter(ProgrammingLanguage.id == id_window_programming_language):
                name_programming_language.append(programming_language.name)

            # We store the first data obtained from the for in a variable
            info_name_programming_language = name_programming_language[0]
        
        finally:
            session.close()

        return info_name_programming_language


    
    