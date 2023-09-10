from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine



class Count:


    def count_rows():
        
        Session = sessionmaker(bind=engine)
        session = Session()

        # Contamos la cantidad de filas en nuestra tabla
        count_rows = session.query(ProgrammingLanguage).count()
          
        return count_rows