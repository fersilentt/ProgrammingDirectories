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
 
        type_application = session.query(TypeApplication).filter(TypeApplication.id == id)
        type_application.update({TypeApplication.name: name})

        session.commit()
