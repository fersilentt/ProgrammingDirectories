from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine

import config
data_json = config.DATA_JSON

class Info:

    def list_info():
        
        with open(data_json, 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window_project_tutorial = json.loads(json_str)
        id_window_project_tutorial = str_id_window_project_tutorial['window_project_tutorial_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        name_project_tutorial = []           
        
        try:

            for project_tutorial in session.query(ProjectTutorial).filter(ProjectTutorial.id == id_window_project_tutorial):
                name_project_tutorial.append(project_tutorial.name)

            info_name_project_tutorial = name_project_tutorial[0]


        finally:
            session.close()
             
          
        return info_name_project_tutorial
    