from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine



class Insert:

    def add_data(name, id):

        Session = sessionmaker(bind=engine)
        session = Session()

        type_application = TypeApplication(name, id)
        session.add(type_application)

        session.commit()
