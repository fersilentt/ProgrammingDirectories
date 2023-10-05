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
        
        try:
            for programming_language in session.query(ProgrammingLanguage).filter(or_(
                ProgrammingLanguage.name.like('%{}%'.format(data)))).all():

                id.append(programming_language.id)
                name.append(programming_language.name)

            my_list = [(id), (name)]
        
        finally:
            session.close()

        return my_list
