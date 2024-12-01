from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class Update:


    def update_data(id, name, repository, youtube_video, number_part):

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            part = session.query(Part).filter(Part.id == id)
            part.update({Part.name: name})
            part.update({Part.repository: repository})
            part.update({Part.youtube_video: youtube_video})
            part.update({Part.number_part: number_part})

            session.commit()
        
        finally:
            session.close()
