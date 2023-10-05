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
            type_application = session.query(TypeApplication).filter(TypeApplication.id == id)
            type_application.delete()

            session.commit()
            
        finally:
            session.close()