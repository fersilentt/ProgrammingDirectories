from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class Update:

    def update_data(id, name):

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            type_creation = session.query(TypeCreation).filter(TypeCreation.id == id)
            type_creation.update({TypeCreation.name: name})

            session.commit()
        
        finally:
            session.close()
