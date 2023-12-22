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

        try:
            # We count the number of rows in our table
            count_rows = session.query(ProgrammingLanguage).count()
        finally:
            session.close()
          
        return count_rows