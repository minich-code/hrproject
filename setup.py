# import necessary modules 
from setuptools import setup, find_packages
from typing import List 

# Define a constant for the hyphen-e-dot string 
HYPHEN_E_DOT = '-e .'

# Define function to get the list of requiremenst from the requirements.txt file 
# This list will return a list of the requirements
def get_requirements(file_path:str)->List[str]:
    # Intiotialize an empty list tha will store the requirements 
    requirements = []
    # Open the specified file path 
    with open(file_path) as file_obj:
        # Read the lines from the requirements.txt file 
        requirements = file_obj.readlines()
        # Remove the newline characters 
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove the -e . string from the requirements list 
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    # Return the requiremenst 
    return requirements

setup(
    name = 'My_ml_project', # Specify the name of the project
    version = '0.1',  # Specify the version of the project
    author = 'Minich', # Specify the author of the project
    author_email = 'minichworks@gmail.com', # Specify the email of the author
    description = 'A machine learning project for predicting employee perfomance', # Specify the description of the project
    packages = find_packages(), # Automatically find packages in the project directory

    # Specify the dependencies required for the project by parsing a requirements file 
    install_requires = get_requirements('requirements.txt')

)



