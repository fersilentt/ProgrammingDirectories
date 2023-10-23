from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine

class Insert:

    def add_data(name, id_programming_language):

        Session = sessionmaker(bind=engine)
        session = Session()
 
        try:
            type_creation = TypeCreation(name, id_programming_language)
            session.add(type_creation)

            session.commit()
        finally:
            session.close()
