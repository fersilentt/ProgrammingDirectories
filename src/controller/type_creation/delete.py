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

        type_creation = session.query(TypeCreation).filter(TypeCreation.id == id)
        type_creation.delete()

        session.commit()