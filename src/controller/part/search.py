from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class Search:

    def search_data(data):

        Session = sessionmaker(bind=engine)
        session = Session()

        id = []
        name = []
        repository = []
        youtube_video = []
        id_part = []
        name_project_tutorial = []   
        id_project_tutorial = []
        
        try:
            data = session.query(Part, ProjectTutorial).join(Part).filter(or_(
                Part.name.like('%{}%'.format(data)))).all()

            for part, project_tutorial in data:
                id.append(part.id)
                name.append(part.name)
                repository.append(part.repository)
                youtube_video.append(part.youtube_video)
                id_part.append(part.id_part)
                name_project_tutorial.append(project_tutorial.name)
                id_project_tutorial.append(project_tutorial.id)   
                
            my_list = [(id), (name), (repository), (youtube_video), (id_part), (name_project_tutorial), (id_project_tutorial)]
        
        finally:
            session.close()

          
        return my_list
    
