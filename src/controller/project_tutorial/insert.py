from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine



class Insert:

    def add_data(
        name,
        programming_language_version, 
        framework, 
        graphical_interface, 
        data_base,
        data_base_version, 
        orm, 
        virtual_environment, 
        architecture, 
        cloud_server,
        number_project_tutorial,
        id):

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            project_tutorial = ProjectTutorial(
                name,
                programming_language_version, 
                framework, 
                graphical_interface, 
                data_base,
                data_base_version, 
                orm, 
                virtual_environment, 
                architecture,
                cloud_server, 
                number_project_tutorial,
                id)

            session.add(project_tutorial)
            session.commit()

        finally:
            session.close()
