import imp
from setuptools import find_packages, setup
from typing import List



# Declaring variables for setup functions

PROJECT_NAME="Housing-predictor"
VERSION="0.0.1"
AUTHER="Wrushabh Gonnade"
DESCRIPTION="Machine learning Project for Housing Prediction"
PACKAGES=['housing']
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    '''
    Description: This function is going to return list of requirements mentioned
    in the requirements.txt file
    
    return this function is going to return a list that contains library names of libraries
     mentioned in the requirements.txt file
    '''

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHER,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()


)

if __name__=="__main__":
    print(get_requirements_list())
