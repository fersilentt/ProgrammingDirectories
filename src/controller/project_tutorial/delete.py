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
 
        project_tutorial = session.query(ProjectTutorial).filter(ProjectTutorial.id == id)
        project_tutorial.delete()

        session.commit()