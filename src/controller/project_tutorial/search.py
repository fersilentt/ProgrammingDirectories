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
        framework = []
        graphical_interface = []
        data_base = []
        orm = []
        virtual_environment = []
        architecture = []
        cloud_server = []
        name_type_application = []
        

        try:
            query = session.query(ProjectTutorial, TypeApplication).join(ProjectTutorial).filter(or_(
                ProjectTutorial.name.like('%{}%'.format(data)))).all()
            
            for project_tutorial, type_application in query:
                id.append(project_tutorial.id)
                name.append(project_tutorial.name)
                framework.append(project_tutorial.framework)
                graphical_interface.append(project_tutorial.graphical_interface)
                data_base.append(project_tutorial.data_base)
                orm.append(project_tutorial.orm)
                virtual_environment.append(project_tutorial.virtual_environment)
                architecture.append(project_tutorial.architecture)
                cloud_server.append(project_tutorial.cloud_server)
                name_type_application.append(type_application.name)

            my_list = [(id), 
            (name), 
            (framework), 
            (graphical_interface), 
            (data_base), (orm), 
            (virtual_environment),
            (architecture),
            (cloud_server),
            (name_type_application)]
        
        finally:
            session.close()

        return my_list
