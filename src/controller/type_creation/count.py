from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

import json

import model.database_open
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

        try:
            # We make the relation with the table and get the amount of data according to the filtered id
            count_rows = session.query(model.database_open.TypeCreation, model.database_open.ProgrammingLanguage).join(model.database_open.TypeCreation).filter(
                model.database_open.TypeCreation.id_programming_language == id_window).count()

        finally:
            session.close()
          
        return count_rows