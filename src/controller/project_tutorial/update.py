from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine


class Update:

    def update_data(
        id, 
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
        number_project_tutorial):

        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            project_tutorial = session.query(ProjectTutorial).filter(ProjectTutorial.id == id)
            project_tutorial.update({ProjectTutorial.name: name})
            project_tutorial.update({ProjectTutorial.programming_language_version: programming_language_version})
            project_tutorial.update({ProjectTutorial.framework: framework})
            project_tutorial.update({ProjectTutorial.name: name})
            project_tutorial.update({ProjectTutorial.graphical_interface: graphical_interface})
            project_tutorial.update({ProjectTutorial.data_base: data_base})
            project_tutorial.update({ProjectTutorial.data_base_version: data_base_version})
            project_tutorial.update({ProjectTutorial.orm: orm})
            project_tutorial.update({ProjectTutorial.virtual_environment: virtual_environment})
            project_tutorial.update({ProjectTutorial.architecture: architecture})
            project_tutorial.update({ProjectTutorial.cloud_server: cloud_server})
            project_tutorial.update({ProjectTutorial.number_project_tutorial: number_project_tutorial})

            session.commit()

        finally:
            session.close()
