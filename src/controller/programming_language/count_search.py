from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine



class CountSearch:

    def count_rows_search(data):
        
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            count_rows_search = session.query(ProgrammingLanguage).filter(or_(
                ProgrammingLanguage.name.like('%{}%'.format(data)))).count()
        finally:
            session.close()
            
        return count_rows_search