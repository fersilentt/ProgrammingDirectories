from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class List:


    def list_data():
        
        f = open('id-window.txt', 'r')
        id_window = f.read()
        f.close()

        Session = sessionmaker(bind=engine)
        session = Session()

        id = []
        name = []
        repository = []
        youtube_video = []
        id_part = []
        name_project_tutorial = []   
        id_project_tutorial = []
        
        
        data = session.query(Part, ProjectTutorial).join(Part).filter(
            Part.id_project_tutorial == id_window).order_by(Part.id_part.asc()).all()


        for part, project_tutorial in data:
            id.append(part.id)
            name.append(part.name)
            repository.append(part.repository)
            youtube_video.append(part.youtube_video)
            id_part.append(part.id_part)
            name_project_tutorial.append(project_tutorial.name)
            id_project_tutorial.append(project_tutorial.id)
            
            
        my_list = [(id), (name), (repository), (youtube_video), (id_part), (name_project_tutorial), (id_project_tutorial)]
          
        return my_list
    

    
    
 