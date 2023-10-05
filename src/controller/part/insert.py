from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine



class Insert:

    def add_data(name, repository, youtube_video, id_part, id):

        Session = sessionmaker(bind=engine)
        session = Session()
 
        try:
            part = Part(name, repository, youtube_video, id_part, id)
            session.add(part)

            session.commit()
        
        finally:
            session.close()
    