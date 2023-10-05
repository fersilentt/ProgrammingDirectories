from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine

class Info:

    def list_info():
        
        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window_project_tutorial = json.loads(json_str)
        id_window_project_tutorial = str_id_window_project_tutorial['window_project_tutorial_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        name_project_tutorial = []           
        
        try:
            data = session.query(Part, ProjectTutorial).join(Part).filter(
                Part.id_project_tutorial == id_window_project_tutorial).all()

            for part, project_tutorial in data[:1]:
                name_project_tutorial.append(project_tutorial.name)                       

            info_name_project_tutorial = name_project_tutorial[0] 

        finally:
            session.close()
             
          
        return info_name_project_tutorial
    