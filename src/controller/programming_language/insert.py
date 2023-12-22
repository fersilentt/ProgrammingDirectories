from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class Insert:

    # We create a function that will insert the data
    def add_data(name):
       
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            programming_language = ProgrammingLanguage(name)
            session.add(programming_language)

            # We commit to the database
            session.commit()
        
        finally:
            session.close()
