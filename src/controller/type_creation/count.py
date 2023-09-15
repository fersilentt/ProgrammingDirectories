from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class Count:

    def count_rows():

        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window = str_id_window['window_table_id']

        
        Session = sessionmaker(bind=engine)
        session = Session()

        
        # Realizamos la relacion con la tabla y obtenemos la cantidad de datos de acuerdo al id filtradp
        count_rows = session.query(TypeCreation, ProgrammingLanguage).join(TypeCreation).filter(
            TypeCreation.id_programming_language == id_window).count()
          
        return count_rows