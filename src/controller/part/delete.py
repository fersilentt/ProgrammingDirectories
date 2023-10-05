from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine

class Delete:

    def delete_data(id):

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            part = session.query(Part).filter(Part.id == id)
            part.delete()

            session.commit()
        
        finally:
            session.close()