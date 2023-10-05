from sqlalchemy.orm import sessionmaker

import os
import sys
file = os.path.abspath("src")
sys.path.insert(0, file)

from model.database_open import *
from model.database_open import engine

class Search:

    def search_data(data):

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
        

        
        # Realizamos la consulta de los campos que tienen relacion mediante un join y  lo
        # almacenamos en una variable, ademas aqui realizamos la busquema mediante varios 
        # campos, aqui usamos un like como en SQL , pero buscamos por varios campos usando 
        # or, como lo hariamos en SQL

        # all() = esto permite obtener toda la lista de datos que tiene similitud
        # or_( = esto indica que la conulta va usar OR y no AND
        # {} = esto permite agregar un valor dentro del mensaje
        # format() = permite pasarle un valor dentro de las llaves {}
        # data = aqui va el dato por el cual se va a buscar en la base de datos
        #query = session.query(Part, ProjectTutorial).join(Part).filter(and_(Part.name.like('%{}%'.format(data)) , Part.id_project_tutorial == id_window )).all()
        query = session.query(Part, ProjectTutorial).join(Part).filter(or_(Part.name.like('%{}%'.format(data)))).filter(Part.id_project_tutorial == id_window).all()

        for part, project_tutorial in query:
            
            id.append(part.id)
            name.append(part.name)
            repository.append(part.repository)
            youtube_video.append(part.youtube_video)
            id_part.append(part.id_part)
            name_project_tutorial.append(project_tutorial.name)
            id_project_tutorial.append(project_tutorial.id)

        my_list = [(id), (name), (repository), (youtube_video), (id_part), (name_project_tutorial), (id_project_tutorial)]

        return my_list
