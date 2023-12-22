from sqlalchemy.orm import sessionmaker



# We import this module to get an absolute path to our project, 
# in order to import the images for  our buttons
import os


# We import this module to be able to inert the path, where the CRUD 
# files are located, in this way we will be able to import our files 
# independently of any folder where they are located.
import sys

# os.path.abspath("src") = we get the absolute path of the project and then we import the files
file = os.path.abspath("src")

# We add the absolute path of our project, so that it recognizes the path of importing of the files 
# that make the CRUD
sys.path.insert(0, file)



# We import the classes where a CRUD is going to be made
from model.database_open import *

# We import the variable that contains the path where the database will be created. the database will 
# be created
from model.database_open import engine






'''
Session = sessionmaker(bind=engine)
session = Session()

for programming_language in session.query(ProgrammingLanguage).order_by(ProgrammingLanguage.name.desc()):
    print(programming_language.id, programming_language.name)
    data = [programming_language.id, programming_language.name]
'''




class List:


    def list_data():
        
        #engine = create_engine('sqlite:///student.db', echo=True)


        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()


        # We create empty arrays to store the information that we will obtain when traversing the for
        id = []
        name = []
        

        # We create an exception handling to close the database connection once the transaction has been 
        # executed to prevent the application from collapsing due to excessive requests to the database
        try:
            # We traverse the object where the information is stored 

            # programming_language = variable storing the data obtained from our query 
            # desc() = here we tell it to sort the query in descending order by the field we have set up 
            for programming_language in session.query(ProgrammingLanguage).order_by(ProgrammingLanguage.name.desc()):
                
                # We create a new array, filled with arrays obtained from the data we get from the for we 
                # get from the for

                # append = allows you to create an array from the data retrieved from the for
                id.append(programming_language.id)
                name.append(programming_language.name)
                

            
            # We create a new array with the list of arrays we have obtained and then traverse and display 
            # them in the view
            my_list = [(id), (name)]

        finally:
            session.close()

        # We return the new array with the list of arrays in order to import it later
        return my_list
    

    
    
 