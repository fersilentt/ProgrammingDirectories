from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine

import config
data_json = config.DATA_JSON


class Count:

    def count_rows():

        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window = str_id_window['window_table_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            count_rows = session.query(TypeApplication, TypeCreation).join(TypeApplication).filter(
                TypeApplication.id_type_creation == id_window).count()

        finally:
            session.close()
          
        return count_rows