from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class List:

    def list_data():
        
        with open('src/data.json', 'r') as f:
            data = json.load(f)

        json_str = json.dumps(data)
        str_id_window = json.loads(json_str)
        id_window = str_id_window['window_table_id']

        Session = sessionmaker(bind=engine)
        session = Session()

        id = []
        name = []
        programming_language_version = []
        framework = []
        graphical_interface = []
        data_base = []
        data_base_version = []
        orm = []
        virtual_environment = []
        architecture = []
        cloud_server = []
        number_project_tutorial = []
        name_type_application = []
        id_type_application = []
        
        
        data = session.query(ProjectTutorial, TypeApplication).join(ProjectTutorial).filter(
            ProjectTutorial.id_type_application == id_window).order_by(ProjectTutorial.number_project_tutorial.asc()).all()


        for project_tutorial, type_application in data:

            id.append(project_tutorial.id)
            name.append(project_tutorial.name)
            programming_language_version.append(project_tutorial.programming_language_version)
            framework.append(project_tutorial.framework)
            graphical_interface.append(project_tutorial.graphical_interface)
            data_base.append(project_tutorial.data_base)
            data_base_version.append(project_tutorial.data_base_version)
            orm.append(project_tutorial.orm)
            virtual_environment.append(project_tutorial.virtual_environment)
            architecture.append(project_tutorial.architecture)
            cloud_server.append(project_tutorial.cloud_server)
            number_project_tutorial.append(project_tutorial.number_project_tutorial)
            name_type_application.append(type_application.name)
            id_type_application.append(type_application.id)
            


        my_list = [(id), 
        (name),
        (programming_language_version), 
        (framework), 
        (graphical_interface), 
        (data_base), 
        (data_base_version),
        (orm), 
        (virtual_environment),
        (architecture),
        (cloud_server),
        (number_project_tutorial),
        (name_type_application),
        (id_type_application)]
          
           
        return my_list
    

    
    
 