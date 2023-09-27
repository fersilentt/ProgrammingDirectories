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
        str_id_window_type_application = json.loads(json_str)
        id_window_type_application = str_id_window_type_application['window_type_application_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        name_type_application = []

        data = session.query(ProjectTutorial, TypeApplication).join(ProjectTutorial).filter(
            ProjectTutorial.id_type_application == id_window_type_application).all()

        for project_tutorial, type_application in data[:1]:
            name_type_application.append(type_application.name)

        info_name_type_application = name_type_application[0]  
           
        return info_name_type_application