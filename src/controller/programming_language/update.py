from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class Update:

    # Creamos una funcion que va actualizar los datos
    def update_data(id, name):

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            programming_language = session.query(ProgrammingLanguage).filter(ProgrammingLanguage.id == id)
            programming_language.update({ProgrammingLanguage.name: name})

            session.commit()

        finally:
            session.close()